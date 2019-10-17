DROP TABLE IF EXISTS LOGINDATA;
DROP TABLE IF EXISTS PASSENGER;
DROP TABLE IF EXISTS TICKET;
DROP TABLE IF EXISTS FLIGHT;

--Login for receptionist and admin
CREATE TABLE IF NOT EXISTS LOGINDATA (
    login_id int unsigned auto_increment,
    login_role char (1) not null, --'A' or 'R'
    login_user varchar (20) not null,
    login_pass varchar (8) not null,
    primary key (login_id)
);

--Create Views for -- Admin and -- Receptionist
--Need function to print a row, then a table in tabular form.

--Receptionist can add these, update these
CREATE TABLE IF NOT EXISTS PASSENGER (
    p_name varchar (20) not null,
    p_cnic varchar (13) not null,
    p_phone varchar (13),
    p_address varchar (30),
    p_nationality varchar (20),
    primary key (p_cnic)
);

--cancel a ticket record -- delete

CREATE TABLE IF NOT EXISTS TICKET (
    ticket_id int unsigned auto_increment,
    ticket_dt datetime,
    p_cnic varchar (13), -- select * from ticket where p_id == 'given' -- flight history 
    flight_id char(7),
    ticket_status varchar (10),
    primary key (ticket_id),
    foreign key (p_cnic) references passenger(p_cnic)
    foreign key (flight_id) references flight(flight_id)
);

--Admin can add these, update these, cancel these -- would have to remove corresponding tickets as well from the tickets table
CREATE TABLE IF NOT EXISTS FLIGHT (
    flight_id char(7),
    departure_airport char(3) not null, --IATA
    arrival_airport char(3) not null, --IATA
    departure_dt datetime, -- View all flights landing and taking off for a particular airport on that day.
    arrival_dt datetime,
    totalseats smallint unsigned, -- total seats
    fare int unsigned, -- Receptionist -- select flight with minimum flight_price
    airplane char(7),
    primary key (flight_id)
);

ALTER TABLE ticket auto_increment=100; 

INSERT INTO logindata ('R','zoraiz','zoraiz123')
INSERT INTO logindata ('A','admin','admin123')
INSERT INTO logindata ('R','rmanager','rmanager123')
INSERT INTO logindata ('R','recep','recep123')
INSERT INTO logindata ('R','recep2','recep456')
INSERT INTO logindata ('A','pakairline','Pakistan123')
INSERT INTO logindata ('A','amanager','amanager123')
INSERT INTO logindata ('R','recep3','recep789')
INSERT INTO logindata ('A','adminta','ta123')

INSERT INTO flight ('PK299','LHR','ISB','2019-10-17 03:20:00','2019-10-17 03:20:00',50,13500,'PIA-410')
INSERT INTO flight ('PK300','LHR','KHI','2019-10-17 23:00:00','2019-10-17 03:20:00',60,13000,'PIA-411')
INSERT INTO flight ('PK301','KHI','LHR','2019-10-17 03:20:00','2019-10-17 03:20:00',50,11000,'PIA-412')
INSERT INTO flight ('PK302','LHR','KHI','2019-10-17 03:20:00','2019-10-17 03:20:00',50,23500,'PIA-413')
INSERT INTO flight ('PK303','KHI','ISB','2019-10-17 03:20:00','2019-10-17 03:20:00',60,12500,'PIA-414')
INSERT INTO flight ('PK304','LHR','KHI','2019-10-17 03:20:00','2019-10-17 03:20:00',50,23000,'PIA-415')
INSERT INTO flight ('PK305','KHI','ISB','2019-10-17 03:20:00','2019-10-17 03:20:00',50,53000,'PIA-416')
INSERT INTO flight ('PK306','LHR','KHI','2019-10-17 03:20:00','2019-10-17 03:20:00',70,13000,'PIA-417')
INSERT INTO flight ('PK307','ISB','KHI','2019-10-17 03:20:00','2019-10-17 03:20:00',50,43000,'PIA-418')
INSERT INTO flight ('PK308','LHR','ISB','2019-10-17 03:20:00','2019-10-17 03:20:00',80,12000,'PIA-419')

INSERT INTO passenger ('Zoraiz Qureshi','35202-9878403-1','03314385434','Lahore, Pakistan','Pakistani')
INSERT INTO passenger ('Ev Puller','11221-6594610-2','','18505 Namekagon Circle','Pakistani')
INSERT INTO passenger ('Sidonia McCawley','60748-4648801-0','','7259 Blaine Lane','Pakistani')
INSERT INTO passenger ('Thadeus Lorentz','13516-8369631-0','','0069 Cardinal Place','Pakistani')
INSERT INTO passenger ('Florie Beechcraft','36263-7474830-4','','0828 Walton Drive','Pakistani')
INSERT INTO passenger ('Randall Edgett','90021-6757081-2','','867 Meadow Ridge Plaza','Pakistani')
INSERT INTO passenger ('Yolanda Ondra','29645-3327571-4','','916 South Center','Pakistani')
INSERT INTO passenger ('Becca Sketch','92597-5463857-5','','7 Ridgeway Street','Pakistani')
INSERT INTO passenger ('Fernando Gildersleeve','71992-0945356-5','','9011 Autumn Leaf Avenue','Pakistani')
INSERT INTO passenger ('Ferrel Morgue','52010-2601019-9','','Clifton, Karachi','Pakistani')


INSERT INTO ticket ('2019-10-17 23:20:07','52010-2601019-9','PK209')
INSERT INTO ticket ('2019-10-17 23:25:02','35202-9878403-1','PK300')
INSERT INTO ticket ('2019-10-17 23:30:10','92597-5463857-5','PK209')
INSERT INTO ticket ('2019-10-17 23:35:00','90021-6757081-2','PK305')
INSERT INTO ticket ('2019-10-17 23:40:00','71992-0945356-5','PK306')
INSERT INTO ticket ('2019-10-17 23:45:03','60748-4648801-0','PK209')
INSERT INTO ticket ('2019-10-17 23:47:00','36263-7474830-4','PK305')
INSERT INTO ticket ('2019-10-17 23:49:09','13516-8369631-0','PK300')
INSERT INTO ticket ('2019-10-17 23:52:00','11221-6594610-2','PK303')
INSERT INTO ticket ('2019-10-17 23:56:11','29645-3327571-4','PK300')


--flight_duration time as DATEDIFF(day, arrdt, deptdt), -- derived
--each table must have more than ten tuples