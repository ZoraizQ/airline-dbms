from PyInquirer import prompt, print_json
import mysql.connector

print ("""╔═╗╦╦═╗╦  ╦╔╗╔╔═╗  ╔╦╗╔╗\n╠═╣║╠╦╝║  ║║║║║╣    ║║╠╩╗\n╩ ╩╩╩╚═╩═╝╩╝╚╝╚═╝  ═╩╝╚═╝""")

def isPairinDict(k, v, d):
    if k in d and v == d[k]:
        return True
    else:
        return False

def receptionistView():
    print("Receptionist login successful.")
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
                { 'name': 'Cancel a particular ticket record', 'value': 'g' }
            ]
        }
    ]
    alpha = prompt(recqs)['recchoice']
    if alpha == 'a':
        a_qs = [  
            {
                'type': 'input',
                'name': 'name',
                'message': 'Please enter full name:'
            },
            {
                'type': 'input',
                'name': 'cnic',
                'message': 'Please enter cnic:'
            },
            {
                'type': 'input',
                'name': 'phone',
                'message': 'Please enter phone:'
            },
            {
                'type': 'input',
                'name': 'address',
                'message': 'Please enter address:'
            },
            {
                'type': 'input',
                'name': 'nationality',
                'message': 'Please enter nationality:'
            },
        ]
        answers = prompt(a_qs)
        print(answers)
    elif alpha == 'b':
        b_qs = [  
            {
                'type': 'input',
                'name': 'name',
                'message': 'Please enter full name:'
            },
            {
                'type': 'input',
                'name': 'cnic',
                'message': 'Please enter cnic:'
            },
            {
                'type': 'input',
                'name': 'phone',
                'message': 'Please enter phone:'
            },
            {
                'type': 'input',
                'name': 'address',
                'message': 'Please enter address:'
            },
            {
                'type': 'input',
                'name': 'nationality',
                'message': 'Please enter nationality:'
            },
        ]
        answers = prompt(b_qs)
    elif alpha == 'e':
        e_qs = [  # further questions for c
            {
                'type': 'input',
                'name': 'deptAirport',
                'message': 'Please enter departure airport:'
            },
            {
                'type': 'input',
                'name': 'arrAirport',
                'message': 'Please enter arrival airport:'
            }
        ]
        answers = prompt(e_qs)
        print(answers)


def adminView():
    print("Admin login successful.")
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
                { 'name': 'View every table of the database in tabular form', 'value': 'e' }
            ]
        }
    ]

    alpha = prompt(adminqs)['adminchoice']
    print(alpha)
    
def main():
    mydb = mysql.connector.connect(user='zoraiz', host='localhost', password='zoraiz123', database='airlineDB')
    print(mydb)
    print("Welcome to the Airline DB Management System!")
    loginqs = [
        {
            'type': 'list',
            'name': 'RorA',
            'message': 'Are you a receptionist or admin?:',
            'choices': ['Receptionist', 'Admin'],
        },
        {
            'type': 'input',
            'message': 'ID:',
            'name': 'id'
        },
        {
            'type': 'password',
            'message': 'Password:',
            'name': 'password'
        }
    ]
    
    answers = prompt(loginqs)
    opt = answers['RorA']
    if opt != 'Receptionist' and opt !='Admin': 
        print("Invalid option.")
        return
    uid, upwd = answers['id'], answers['password']

    admincreds = {"admin":"admin123"} # key is id, value is password
    recepcreds = {"recep":"recep123"}

    if opt == 'Admin':
        if isPairinDict(uid,upwd,admincreds):
            adminView()
        else:
            print("Invalid login details. Please try again.")
    elif opt == 'Receptionist':
        if isPairinDict(uid,upwd,recepcreds):
            receptionistView()
        else:
            print("Invalid login details. Please try again.")

if __name__== "__main__":
    main()
