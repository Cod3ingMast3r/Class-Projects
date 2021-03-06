CREATE TABLE IF NOT EXISTS EMPLOYEE 
	(FNAME VARCHAR(20), 
	 MINIT CHAR(1),
	 LNAME VARCHAR(20) NOT NULL,
	 SSN CHAR(9) PRIMARY KEY DEFAULT '999999999',
	 BDATE DATE, 
	 ADDRESS VARCHAR(50),
	 SEX ENUM('M','F'), 
	 SALARY DECIMAL(10,2), 
	 SUPERSSN CHAR(9), 
	 DNO INTEGER);
     
CREATE TABLE IF NOT EXISTS DEPARTMENT 
	(DNAME VARCHAR(20) UNIQUE,
	DNUMBER INTEGER PRIMARY KEY DEFAULT 0, MGRSSN CHAR(9), 
	MGRSTARTDATE DATE);

CREATE TABLE IF NOT EXISTS DEPT_LOCATIONS     	(DNUMBER INTEGER, 
	DLOCATION VARCHAR(50),
	 PRIMARY KEY (DNUMBER, DLOCATION));
     
CREATE TABLE IF NOT EXISTS PROJECT 
	(PNAME VARCHAR(20) UNIQUE, 
	PNUMBER INTEGER PRIMARY KEY DEFAULT 0, PLOCATION VARCHAR(20),
	 DNUM INTEGER);

CREATE TABLE IF NOT EXISTS WORKS_ON 
	(ESSN CHAR(9),
	 PNO INTEGER,
	 HOURS DECIMAL(4,2),
	 PRIMARY KEY (ESSN, PNO));

CREATE TABLE IF NOT EXISTS DEPENDENT 
	(ESSN CHAR(9), 
	DEPENDENT_NAME VARCHAR(20), 
	SEX ENUM('m','f'), 
	BDATE DATE, 
	RELATIONSHIP VARCHAR(9),
	PRIMARY KEY (DEPENDENT_NAME, ESSN));

INSERT INTO EMPLOYEE VALUES
('James','E','Borg','888665555','1937-11-10','450 Stone, Houston, TX','M',55000.00,'987654321',1),
('Franklin','T','Wong','333445555','1955-12-08','638 Voss, Houston, TX','M',40000.00,'888665555',5),
('Jennifer','S','Wallace','987654321','1941-06-20','291 Berry, Bellaire, TX','F',43000.00,'888665555',4),
('John','B','Smith','123456789','1965-01-09','731 Fondren, Houston, TX','M',30000.00,'333445555',5),
('Alicia','J','Zelaya','999887777','1968-01-19','3321 Castle, Spring, TX','F',25000.00,'987654321',4),
('Ramesh','K','Narayan','666884444','1962-09-15','975 Fire Oak, Humble, TX','M',38000.00,'333445555',5),
('Joyce','A','English','453453453','1972-07-31','5631 Rice, Houston, TX','F',25000.00,'333445555',5),
('Ahmad','V','Jabbar','987987987','1969-03-29','980 Dallas, Houston, TX','M',25000.00,'987654321',4);

INSERT INTO DEPARTMENT VALUES
	('Headquarters',1,'888665555','1981-06-19'),
	('Administration',4,'987654321','1995-01-01'),
	('Research',5,'333445555','1988-05-22');
    
INSERT INTO PROJECT VALUES
	('ProductX',1,'Bellaire',5),
	('ProductY', 2,'Sugarland',5),
	('ProductZ', 3,'Houston',5),
	('Computerization',10,'Stafford',4),
	('Reorganization',20,'Houston',1),
	('Newbenefits',30,'Stafford',4);
    
INSERT INTO DEPT_LOCATIONS VALUES
	(1,'Houston'),
	(4,'Stafford'),
	(5,'Bellaire'),
	(5,'Sugarland'),
	(5,'Houston');
    
INSERT INTO WORKS_ON VALUES
('123456789',1,32.5),
('123456789',2,7.5),
('666884444',3,40.0),
('453453453',1,20.0),
('453453453',2,20.0),
('333445555',2,10.0),
('333445555',3,10.0),
('333445555',10,10.0),
('333445555',20,10.0),
('999887777',10,10.0),
('999887777',30,30.0),
('987987987',10,35.0),
('987987987',30,5.0),
('987654321',20,15.0),
('987654321',30,20.0),
('888665555',20,0.0);

INSERT INTO DEPENDENT VALUES
('123456789','Alice','F','1988-12-30','DAUGHTER'),
('123456789','Elizabeth','F','1967-05-05','SPOUSE'),
('123456789','Michael','M','1988-01-04','SON'),
('333445555','Alice','F','1986-04-05','DAUGHTER'),
('333445555','Joy','F','1958-05-03','SPOUSE'),
('333445555','Theodore','M','1983-10-25','SON'),
('987654321','Abner','M','1942-02-28','SPOUSE');

ALTER TABLE EMPLOYEE
	ADD CONSTRAINT SUPERVISOR FOREIGN KEY (SUPERSSN) REFERENCES EMPLOYEE(SSN)
	ON UPDATE SET NULL ON DELETE SET NULL,
	ADD CONSTRAINT WORKING_DEPT FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNUMBER)
	ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE DEPARTMENT
	 ADD CONSTRAINT MANAGES FOREIGN KEY (MGRSSN) REFERENCES EMPLOYEE(SSN)
	 ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE PROJECT
	 ADD CONSTRAINT PROJ_DEPT FOREIGN KEY (DNUM) REFERENCES DEPARTMENT(DNUMBER)
	 ON UPDATE CASCADE ON DELETE SET NULL;

ALTER TABLE DEPT_LOCATIONS
	 ADD CONSTRAINT FOR_DEPT FOREIGN KEY (DNUMBER) REFERENCES DEPARTMENT(DNUMBER)
	 ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE DEPENDENT
	 ADD CONSTRAINT DPEND_WRKER FOREIGN KEY (ESSN) REFERENCES EMPLOYEE(SSN)
	  ON UPDATE CASCADE ON DELETE CASCADE;