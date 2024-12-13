CREATE DATABASE CredentialsDB;
USE CredentialsDB;

CREATE TABLE account(
	userID  VARCHAR(30) NOT NULL,
  password1   VARCHAR(30) NOT NULL,
PRIMARY KEY (userID));

CREATE TABLE passwords(
   website     VARCHAR(30) NOT NULL,
   userID      VARCHAR(30) NOT NULL,
   email       VARCHAR(50),
   password2       VARCHAR(30) NOT NULL,
PRIMARY KEY (website, userID),
FOREIGN KEY (userID) REFERENCES account(userID));