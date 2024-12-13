CREATE DATABASE CredentialsDB;

CREATE TABLE account(
	userID	varChar(30) NOT NULL,
    password	varChar(30) NOT NULL,
CONSTRAINT account_PK PRIMARY KEY (userID));

CREATE TABLE passwords(
	userID      varChar(30) NOT NULL,
	website		varChar(30) NOT NULL,
    email		varChar(50),
    password	varChar(30) NOT NULL,

CONSTRAINT account_FK FOREIGN key (userID) REFERENCES account(userID));