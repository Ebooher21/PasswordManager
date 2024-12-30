CREATE DATABASE CredentialsDB;
USE CredentialsDB;

CREATE TABLE account(
	userID  VARCHAR(30) NOT NULL,
  password1   VARCHAR(30) NOT NULL,
PRIMARY KEY (userID));

CREATE TABLE passwords(
  accountID   INT AUTO_INCREMENT,
  userID      VARCHAR(30) NOT NULL,
  website     VARCHAR(30) NOT NULL,
  email       VARCHAR(50),
  username    VARCHAR(30),
  password2       VARCHAR(30) NOT NULL,
PRIMARY KEY (accountID),
FOREIGN KEY (userID) REFERENCES account(userID) ON DELETE CASCADE ON UPDATE CASCADE);