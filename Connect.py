import os
import mysql.connecter
from mysql.connector import Error

class Connect:

    def connectioncheck(self, host_name, usr_name, us_password, cu_database):
        credentialsdb = None
        try:
            credentialsdb = mysql.connector.connect(
                host = host_name,
                user = usr_name,
                password = us_password,
                database = cu_database
            )

            print("connected")
        except Error as err:
            print(f"Error: {err}")
        return credentialsdb

    def exquery(self, credentialsdb, query, credentials=None):
        cursor = credentialsdb.cursor()
        try:
            cursor.execute(query, credentials)
            credentialsdb.commit()
            print("query succesful")
            cursor.close()
        except Error as err:
            print(f"Error: {err}")

    def newcredentials(self, unvar, pvar, credentialsdb):
        newAccount = "INSERT INTO account (userID, password1) VALUES (%s, %s);"
        credentials = (unvar, pvar)
        exquery(credentialsdb, newAccount, credentials)

    def credcheck(self, credentialsdb, unvar, pvar):
        usr = unvar.get()
        pswd = pvar.get()
        checuser = "SELECT * FROM account;"
        cred = (usr, pswd)
        checkque(credentialsdb, checuser, cred)

    def fndquery(self, credentialsdb, query, username, table):
        cursor = credentialsdb.cursor()
        try:
            cursor.execute(query, username)
            acc = cursor.fetchall()
            for row in acc:
                website = row[0]
                email = row[1]
                username = row[2]
                password2 = row[3]
                table.insert("", "end", values=(website, email, username, password2))

        except Error:
            manpass.noAccLbl = ttk.Label(manpass, text="No accounts for this user...")
            manpass.noAccLbl.pack(padx=2, pady=2)

    def findwebcredentials(self, credentialsdb, unvar, table):
        # statement won't accept a StringVar or string so it had to be set to a list
        username = unvar.get()
        usrlist = [username]
        findAcc = "SELECT website, email, username, password2 FROM passwords WHERE userID = %s;"
        user = (usrlist)
        fndquery(credentialsdb, findAcc, user, table)

    def multiquery(self, credentialsdb, query1, query2, credentials):
        cursor = credentialsdb.cursor()
        try:
            cursor.execute(query2, credentials)
            cursor.execute(query1, credentials)
            credentialsdb.commit()
            print("query succesful")
            cursor.close()
        except Error as err:
            print(f"Error: {err}")