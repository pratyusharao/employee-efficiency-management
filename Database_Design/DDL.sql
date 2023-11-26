--- create database employee;
--- use employee;
CREATE TABLE Employee
(
  Id INT,
  Fname VARCHAR(10) ,
  Mname VARCHAR(10),
  Lname VARCHAR(10),
  DOB DATE ,
  Score FLOAT ,
  PRIMARY KEY (Id)
);

CREATE TABLE Room
(
  Room_no INT ,
  Time FLOAT ,
  Id INT ,
  PRIMARY KEY (Room_no),
  FOREIGN KEY (Id) REFERENCES Employee(Id)
);

CREATE TABLE Feedback
(
  Feedback VARCHAR(10) ,
  Score FLOAT ,
  Date DATE ,
  Id INT ,
  FOREIGN KEY (Id) REFERENCES Employee(Id),
  FOREIGN KEY (Id) REFERENCES Employee(Id)
);

CREATE TABLE Employee_Email
(
  Email VARCHAR(10) ,
  Id INT ,
  PRIMARY KEY (Email, Id),
  FOREIGN KEY (Id) REFERENCES Employee(Id)
);