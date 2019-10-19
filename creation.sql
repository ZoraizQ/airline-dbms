DROP DATABASE IF EXISTS airlineDB;
CREATE DATABASE airlineDB;
USE airlineDB;

DROP TABLE IF EXISTS logindata;
DROP TABLE IF EXISTS passenger;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS flight;

CREATE TABLE IF NOT EXISTS logindata ( 
    login_id int unsigned auto_increment,
    login_role char (1) not null, 
    login_user varchar (20) not null,
    login_pass varchar (20) not null,
    primary key (login_id)
);

CREATE TABLE IF NOT EXISTS passenger ( 
    p_name varchar (30) not null,
    p_cnic char (13),
    p_phone char (12),
    p_address varchar (80),
    p_nationality varchar (20),
    primary key (p_cnic)
);

CREATE TABLE IF NOT EXISTS flight ( 
    flight_id char(5),
    departure_airport char(3) not null, 
    arrival_airport char(3) not null, 
    departure_time time,
    arrival_time time,
    fare int unsigned, 
    airplane char(7),
    primary key (flight_id)
);

CREATE TABLE IF NOT EXISTS ticket ( 
    ticket_id int unsigned auto_increment,
    ticket_dt datetime,
    p_cnic char (13), 
    flight_id char(5),
    primary key (ticket_id),
    foreign key (p_cnic) references passenger(p_cnic),
    foreign key (flight_id) references flight(flight_id)
);

ALTER TABLE ticket auto_increment=100; 

INSERT INTO logindata(login_role, login_user, login_pass) VALUES('R','zoraiz','zoraiz123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('A','admin','admin123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('R','rmanager','rmanager123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('R','recep','recep123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('R','recep2','recep456');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('A','pakairline','Pakistan123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('A','amanager','amanager123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('R','recep3','recep789');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('A','adminta','ta123');
INSERT INTO logindata(login_role, login_user, login_pass) VALUES('A','adminta2','ta456');


INSERT INTO flight VALUES('PK299','LHR','ISB','01:20:00','02:20:00',13500,'PIA-410');
INSERT INTO flight VALUES('PK300','LHR','KHI','02:00:00','03:20:00',13000,'PIA-411');
INSERT INTO flight VALUES('PK301','KHI','LHR','03:30:00','04:15:00',11000,'PIA-412');
INSERT INTO flight VALUES('PK302','LHR','KHI','04:00:00','05:00:00',23500,'PIA-413');
INSERT INTO flight VALUES('PK303','KHI','ISB','05:20:00','06:30:00',12500,'PIA-414');
INSERT INTO flight VALUES('PK304','LHR','KHI','06:15:00','07:40:00',23000,'PIA-415');
INSERT INTO flight VALUES('PK305','KHI','ISB','07:20:00','08:20:00',53000,'PIA-416');
INSERT INTO flight VALUES('PK306','LHR','KHI','08:20:00','09:05:00',13000,'PIA-417');
INSERT INTO flight VALUES('PK307','ISB','KHI','09:30:00','10:40:00',43000,'PIA-418');
INSERT INTO flight VALUES('PK308','LHR','ISB','10:00:00','11:15:00',12000,'PIA-419');

INSERT INTO passenger VALUES('Zoraiz Qureshi','3520298784031','923314385434','Lahore, Pakistan','Pakistani');
INSERT INTO passenger VALUES('Ev Puller','1122165946102','928897615295','18505 Namekagon Circle','Pakistani');
INSERT INTO passenger VALUES('Sidonia McCawley','6074846488010','924705907313','7259 Blaine Lane','Pakistani');
INSERT INTO passenger VALUES('Thadeus Lorentz','1351683696310','925175527508','0069 Cardinal Place','Pakistani');
INSERT INTO passenger VALUES('Florie Beechcraft','3626374748304','922563216166','0828 Walton Drive','Pakistani');
INSERT INTO passenger VALUES('Randall Edgett','9002167570812','925167490698','867 Meadow Ridge Plaza','Pakistani');
INSERT INTO passenger VALUES('Yolanda Ondra','2964533275714','924167975704','916 South Center','Pakistani');
INSERT INTO passenger VALUES('Becca Sketch','9259754638575','921713461728','7 Ridgeway Street','Pakistani');
INSERT INTO passenger VALUES('Fernando Gildersleeve','7199209453565','926939494993','9011 Autumn Leaf Avenue','Pakistani');
INSERT INTO passenger VALUES('Ferrel Morgue','5201026010199','925302015331','Clifton, Karachi','Pakistani');

INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:20:07','5201026010199','PK299');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:25:02','3520298784031','PK300');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:30:10','9259754638575','PK299');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:35:00','9002167570812','PK305');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:40:00','7199209453565','PK306');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:45:03','6074846488010','PK299');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:47:00','3626374748304','PK305');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:49:09','1351683696310','PK300');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:52:00','1122165946102','PK303');
INSERT INTO ticket(ticket_dt, p_cnic, flight_id) VALUES('2019-10-17 23:56:11','2964533275714','PK300');