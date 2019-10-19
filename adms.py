from PyInquirer import prompt
from tabulate import tabulate
import mysql.connector

print ("""╔═╗╦╦═╗╦  ╦╔╗╔╔═╗  ╔╦╗╔╗\n╠═╣║╠╦╝║  ║║║║║╣    ║║╠╩╗\n╩ ╩╩╩╚═╩═╝╩╝╚╝╚═╝  ═╩╝╚═╝""")

def inTimeFormat(timeStr):
    t = timeStr.split(':')
    if len(t) != 3:
        return False
    for p in t:
        if len(p) != 2 or not p.isdigit():
            return False
    h,m,s = int(t[0]),int(t[1]),int(t[2])
    if (h < 0 or h > 23) or (m < 0 or m > 59) or (s < 0 or s > 59):
        return False
    return True


def receptionistView(mydb):
    print("Receptionist login successful.")
    while True:
        print('')
        dbcursor = mydb.cursor()
        recqs = [
            {
                'type': 'list',
                'name': 'recchoice',
                'message': 'What do you want to do?',
                'choices': [
                    { 'name': 'Create a new passenger record', 'value': 'a' },
                    { 'name': 'Update the details of an existing passenger record', 'value': 'b' },
                    { 'name': 'Using departure airport IATA code and arrival airport IATA code, view all available flights in a particular time period', 'value': 'c' },
                    { 'name': 'Generate ticket record for a particular passenger for a particular flight', 'value': 'd' },
                    { 'name': 'Using departure airport IATA code and arrival airport IATA code, view the cheapest flight', 'value': 'e' },
                    { 'name': 'View flight history of a particular passenger', 'value': 'f' },
                    { 'name': 'Cancel a particular ticket record', 'value': 'g' },
                    { 'name': 'Log out', 'value': 'h' }
                ]
            }
        ]
        alpha = prompt(recqs)['recchoice']
        if alpha == 'a':
            a_qs = [  
                {
                    'type': 'input',
                    'name': 'name',
                    'message': 'Please enter full name:',
                    'validate':lambda x: len(x) > 0 and len(x) <= 30
                },
                {
                    'type': 'input',
                    'name': 'cnic',
                    'message': 'Please enter cnic (13 digits):',
                    'validate': lambda x: len(x) == 13 and x.isdigit() 
                },
                {
                    'type': 'input',
                    'name': 'phone',
                    'message': 'Please enter phone (e.g. 923314385434):',
                    'validate': lambda x: len(x) == 12 and x.isdigit()
                },
                {
                    'type': 'input',
                    'name': 'address',
                    'message': 'Please enter address:',
                    'validate': lambda x: len(x) <= 80
                },
                {
                    'type': 'input',
                    'name': 'nationality',
                    'message': 'Please enter nationality:',
                    'validate': lambda x: x.isalpha() and len(x) <= 20
                },
            ]
            ans = prompt(a_qs)
            sql = 'insert into passenger values(%s,%s,%s,%s,%s)'
            val = (ans['name'],ans['cnic'],ans['phone'],ans['address'],ans['nationality'])
            dbcursor.execute(sql, val)
            mydb.commit()
            print('Passenger record created successfully.')

        elif alpha == 'b':
            b_qs = [  
                {
                    'type': 'input',
                    'name': 'cnic',
                    'message': 'Please enter cnic for the record you wish to update (13 digits):',
                    'validate': lambda x: len(x) == 13 and x.isdigit() 
                },
                {
                    'type': 'input',
                    'name': 'name',
                    'message': 'Please enter full name:',
                    'validate':lambda x: len(x) > 0 and len(x) <= 30
                },
                {
                    'type': 'input',
                    'name': 'phone',
                    'message': 'Please enter phone (e.g. 923314385434):',
                    'validate': lambda x: len(x) == 12 and x.isdigit()
                },
                {
                    'type': 'input',
                    'name': 'address',
                    'message': 'Please enter address:',
                    'validate': lambda x: len(x) <= 80
                },
                {
                    'type': 'input',
                    'name': 'nationality',
                    'message': 'Please enter nationality:',
                    'validate': lambda x: x.isalpha() and len(x) <= 20
                },
            ]
            ans = prompt(b_qs)
            sql = 'update passenger set p_name = "%s", p_phone = "%s", p_address = "%s", p_nationality = "%s" where p_cnic = "%s";'
            val = (ans['name'],ans['phone'],ans['address'],ans['nationality'], ans['cnic'])
            dbcursor.execute(sql%val)
            mydb.commit()
            print('Passenger record updated successfully.')

        elif alpha == 'c':
            c_qs = [
                {
                    'type': 'input',
                    'name': 'deptAirport',
                    'message': 'Please enter departure airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'arrAirport',
                    'message': 'Please enter arrival airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'startTime',
                    'message': 'Please enter earliest time for the time period (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                },
                {
                    'type': 'input',
                    'name': 'endTime',
                    'message': 'Please enter latest time for the time period (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                }
            ]
            ans = prompt(c_qs)
            sql = 'select * from flight where departure_airport = "%s" and arrival_airport = "%s" and departure_time >= "%s" and departure_time <= "%s";'
            val = (ans['deptAirport'],ans['arrAirport'],ans['startTime'],ans['endTime'])
            dbcursor.execute(sql% val)
            result = dbcursor.fetchall()
            h = ['flight_id','departure_airport','arrival_airport','departure_time','arrival_time','fare','airplane']
            print(tabulate(result, headers=h, tablefmt='psql'))

        elif alpha == 'd':
            d_qs = [
                {
                    'type': 'input',
                    'name': 'cnic',
                    'message': 'Please enter passenger cnic (13 digits):',
                    'validate': lambda x: len(x) == 13 and x.isdigit() 
                },
                {
                    'type': 'input',
                    'name': 'flight_id',
                    'message': 'Please enter flight ID (5 chars):',
                    'validate': lambda x: len(x) == 5
                },
            ]
            ans = prompt(d_qs)
            sql = 'insert into ticket(ticket_dt, p_cnic, flight_id) values(now(),"%s","%s")'
            val = (ans['cnic'],ans['flight_id'])
            # check whether these exist first in passenger and flight
            dbcursor.execute(sql% val)
            mydb.commit()
            print('Ticket successfully generated with ID:',dbcursor.lastrowid)

        elif alpha == 'e':
            e_qs = [  # further questions for e
                {
                    'type': 'input',
                    'name': 'deptAirport',
                    'message': 'Please enter departure airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'arrAirport',
                    'message': 'Please enter arrival airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                }
            ]
            ans = prompt(e_qs)
            sql = 'select * from flight where fare = (select min(fare) from flight where departure_airport = "%s" and arrival_airport="%s");'
            val = (ans['deptAirport'],ans['arrAirport'])
            dbcursor.execute(sql%val)
            result = dbcursor.fetchall()
            h = ['flight_id','departure_airport','arrival_airport','departure_time','arrival_time','fare','airplane']
            print(tabulate(result, headers=h, tablefmt='psql'))


        elif alpha == 'f':
            f_qs = [  # further questions for e
                {
                    'type': 'input',
                    'name': 'cnic',
                    'message': 'Please enter cnic of passenger to view their flight history (13 digits):',
                    'validate': lambda x: len(x) == 13 and x.isdigit()
                }
            ]
            ans = prompt(f_qs)
            sql = 'select ticket_id,flight.flight_id,departure_airport,arrival_airport,departure_time,arrival_time,fare,airplane from (ticket join flight) where ticket.flight_id = flight.flight_id and p_cnic="'+ans['cnic']+'";'
            dbcursor.execute(sql)
            result = dbcursor.fetchall()
            h = ['ticket_id','flight_id','departure_airport','arrival_airport','departure_time','arrival_time','fare','airplane']
            print(tabulate(result, headers=h, tablefmt='psql'))

        elif alpha == 'g':
            g_qs = [  
                {
                    'type': 'input',
                    'name': 'ticket_id',
                    'message': 'Please enter ticket ID for the ticket to cancel (3 digits):',
                    'validate': lambda x: len(x) == 3 and x.isdigit()
                }
            ]
            tid = prompt(g_qs)['ticket_id']
            sql = 'delete from ticket where ticket_id = "%s";'
            dbcursor.execute(sql%tid)
            mydb.commit()
            print('Ticket with ticket_id %s was successfully cancelled.' % tid)

        elif alpha == 'h':
            return
    




def adminView(mydb):
    print("Admin login successful.")
    dbcursor = mydb.cursor()
    while True:
        print('')
        adminqs = [
            {
                'type': 'list',
                'name': 'adminchoice',
                'message': 'What do you want to do?',
                'choices': [
                    { 'name': 'Add a new flight record, with the required details', 'value': 'a' },
                    { 'name': 'Update details of an existing flight record', 'value': 'b' },
                    { 'name': 'Cancel a particular flight record', 'value': 'c' },
                    { 'name': 'View all flights landing and taking off for a particular airport on that day', 'value': 'd' },
                    { 'name': 'View every table of the database in tabular form', 'value': 'e' },
                    { 'name': 'Log out', 'value': 'f' }
                ]
            }
        ]

        alpha = prompt(adminqs)['adminchoice']
        if alpha == 'a':
            a_qs = [  
                {
                    'type': 'input',
                    'name': 'flight_id',
                    'message': 'Please enter flight ID (5 chars):',
                    'validate': lambda x: len(x) == 5
                },
                {
                    'type': 'input',
                    'name': 'departure_airport',
                    'message': 'Please enter departure airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'arrival_airport',
                    'message': 'Please enter arrival airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'departure_time',
                    'message': 'Please enter departure time (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                },
                {
                    'type': 'input',
                    'name': 'arrival_time',
                    'message': 'Please enter arrival time (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                },
                {
                    'type': 'input',
                    'name': 'fare',
                    'message': 'Please enter flight fare:',
                    'validate': lambda x : x.isdigit()
                },
                {
                    'type': 'input',
                    'name': 'airplane',
                    'message': 'Please enter airplane name (7 chars e.g. ANJ-415):',
                    'validate': lambda x : len(x) == 7
                }
            ]

            ans = prompt(a_qs)
            sql = 'insert into flight values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d,\'%s\');'
            val = (ans['flight_id'], ans['departure_airport'],ans['arrival_airport'],ans['departure_time'],ans['arrival_time'],int(ans['fare']),ans['airplane'])
            dbcursor.execute(sql%val)
            mydb.commit()
            print('Flight record created successfully.')

        elif alpha == 'b':
            b_qs = [  
                {
                    'type': 'input',
                    'name': 'flight_id',
                    'message': 'Please enter flight ID to update details for (5 chars):',
                    'validate': lambda x: len(x) == 5
                },
                {
                    'type': 'input',
                    'name': 'departure_airport',
                    'message': 'Please enter departure airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'arrival_airport',
                    'message': 'Please enter arrival airport IATA (3 alpha):',
                    'validate':lambda x: len(x) == 3 and x.isalpha()
                },
                {
                    'type': 'input',
                    'name': 'departure_time',
                    'message': 'Please enter departure time (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                },
                {
                    'type': 'input',
                    'name': 'arrival_time',
                    'message': 'Please enter arrival time (HH:MM:SS):',
                    'validate': lambda x : inTimeFormat(x)
                },
                {
                    'type': 'input',
                    'name': 'fare',
                    'message': 'Please enter flight fare:',
                    'validate': lambda x : x.isdigit()
                },
                {
                    'type': 'input',
                    'name': 'airplane',
                    'message': 'Please enter airplane name (7 chars e.g. ANJ-415):',
                    'validate': lambda x : len(x) == 7
                }
            ]
            ans = prompt(b_qs)
            sql = 'update flight set departure_airport = "%s", arrival_airport = "%s", departure_time = "%s", arrival_time = "%s", fare = %d, airplane = "%s" where flight_id = "%s";'
            val = (ans['departure_airport'],ans['arrival_airport'],ans['departure_time'],ans['arrival_time'],int(ans['fare']),ans['airplane'], ans['flight_id'])
            dbcursor.execute(sql%val)
            mydb.commit()
            print('Flight record for flight ID %s updated.' % ans['flight_id'])

        elif alpha == 'c':
            c_qs = [  
                {
                    'type': 'input',
                    'name': 'flight_id',
                    'message': 'Please enter flight ID for the flight to cancel (5 chars):',
                    'validate': lambda x: len(x) == 5
                }
            ]
            fid = prompt(c_qs)['flight_id']
            sql = 'delete from flight where flight_id = "%s";'
            dbcursor.execute(sql%fid)
            sql = 'delete from ticket where flight_id = "%s";'
            dbcursor.execute(sql%fid)
            mydb.commit()
            print('Flight and corresponding tickets successfully cancelled.')

        elif alpha == 'd':
            d_qs = [  
                {
                    'type': 'input',
                    'name': 'airport',
                    'message': 'Please enter airport IATA (3 alpha):',
                    'validate': lambda x: len(x) == 3 and x.isalpha()
                }
            ]
            airport = prompt(d_qs)['airport']
            sql = 'select * from flight where departure_airport = "%s" or arrival_airport = "%s";'
            dbcursor.execute(sql%(airport,airport))
            result = dbcursor.fetchall()
            h = ['flight_id','departure_airport','arrival_airport','departure_time','arrival_time','fare','airplane']
            print(tabulate(result, headers=h, tablefmt='psql'))

        elif alpha == 'e':
            e_qs = [ 
                {
                'type': 'list',
                'name': 'tablechoice',
                'message': 'Which table do you want to view?',
                'choices': ['flight','passenger','ticket','logindata']
                }
            ]

            tableName = prompt(e_qs)['tablechoice']
            sql = 'select * from %s;'
            dbcursor.execute(sql%tableName)
            result = dbcursor.fetchall()
            if tableName == 'flight':
                h = ['flight_id','departure_airport','arrival_airport','departure_time','arrival_time','fare','airplane']
            elif tableName == 'passenger':
                h = ['p_name','p_cnic','p_phone','p_address','p_nationality']
            elif tableName == 'ticket':
                h = ['ticket_id', 'ticket_dt', 'p_cnic', 'flight_id']
            elif tableName == 'logindata':
                h = ['login_id', 'login_role', 'login_user', 'login_pass']
            print(tabulate(result, headers=h, tablefmt='psql'))

        elif alpha == 'f':
            return
  
def main():
    mydb = mysql.connector.connect(user='zoraiz', host='localhost', password='zoraiz123', database='airlineDB')
    print(mydb)
    dbcursor = mydb.cursor()

    print("Welcome to the Airline DB Management System!")
    while True:
        loginqs = [
            {
                'type': 'list',
                'name': 'RorA',
                'message': 'Are you a receptionist or admin?:',
                'choices': [{'name': 'Receptionist', 'value':'R'}, {'name':'Admin','value':'A'}],
            },
            {
                'type': 'input',
                'message': 'Username:',
                'name': 'user'
            },
            {
                'type': 'password',
                'message': 'Password:',
                'name': 'password'
            }
        ]
        
        ans = prompt(loginqs)
        #ans = {'RorA':'R', 'user':'zoraiz', 'password':'zoraiz123'}
        #ans = {'RorA':'A', 'user':'admin', 'password':'admin123'}
        opt = ans['RorA']
        
        sql = 'select count(*) from logindata where login_role = "%s" and login_user = "%s" and login_pass = "%s";'
        val = (opt, ans['user'], ans['password'])
        dbcursor.execute(sql%val)
        logindata = dbcursor.fetchone()
        
        if logindata[0] != 0: # a record for that login information was found
            if (opt == 'A'):
                adminView(mydb)
            else:
                receptionistView(mydb)
        else:
            print("Invalid login details. Please try again.")

if __name__== "__main__":
    main()
