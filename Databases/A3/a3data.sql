CREATE TABLE vendor 
	(Vno CHAR(5) PRIMARY KEY,
	Vname CHAR(20),
	City CHAR(20),
	Vbalance FLOAT(2));
	
INSERT INTO vendor VALUES ('V1', 'Sears', 'Toronto', 200.00),
						  ('V2', 'Walmart', 'Waterloo', 671.05),
						  ('V3', 'Esso', 'Windsor', 0.00),
						  ('V4', 'Esso', 'Waterloo', 225.00);

CREATE TABLE customer
	(Account CHAR(5) PRIMARY KEY,
	Cname CHAR(20),
	Province CHAR(20),
	Cbalance FLOAT(2),
	Crlimit INTEGER);
	
INSERT INTO customer VALUES ('A1', 'Smith', 'ONT', 2515.00, 2000),
							('A2', 'Jones', 'BC', 2014.00, 2500),
							('A3', 'Doc', 'ONT', 150.00, 1000);

CREATE TABLE transaction 
	(Tno CHAR(5) PRIMARY KEY,
	Vno CHAR(5),
	Account CHAR(5),
	T_Date DATE,
	Amount FLOAT(2));
	
INSERT INTO transaction VALUES ('T1', 'V2', 'A1', '2019-07-15', 1325.00),
							   ('T2', 'V2', 'A3', '2018-12-16', 1900.00),
							   ('T3', 'V3', 'A1', '2019-09-01', 2500.00),
							   ('T4', 'V4', 'A2', '2019-03-20', 1613.00),
							   ('T5', 'V4', 'A3', '2019-07-31', 3312.00);
