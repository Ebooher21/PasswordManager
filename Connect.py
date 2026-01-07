from tkinter import *
import mysql.connecter
from mysql.connector import Error
from UI import *

class Connect:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connection_check(self):

        if self.connection and self.connection.is_connected():
            print('Already Connected')
            return self.connection
        try:

            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )

            print("Connection Successful")
            return self.connection

        except Error as err:
            print(f"Error: {err}")
            return None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('Database Connection Closed')

    # execute query
    def execute_query(self, query, credentials=None):
        try:
            cursor = self.database.cursor()
            cursor.execute(query, credentials)
            self.database.commit()
            print("query succesful")
            cursor.close()
        except Error as err:
            print(f"Error: {err}")

    # retrieve users passwords
    def find_query(self, query, username, table):
        try:
            cursor = self.database.cursor()
            cursor.execute(query, username)
            acc = cursor.fetchall()
            for row in acc:
                website = row[0]
                email = row[1]
                username = row[2]
                password2 = row[3]
                table.insert("", "end", values=(website, email, username, password2))
        except Error:
            UI.find_query_error(self.connection)
            return None

    def read_query(self, query, credentials):
        try:
            cursor = self.database.cursor()

            accind = 0
            unvar = credentials[0]
            pvar = credentials[1]

            if unvar == "" or pvar == "":
                UI.read_query_empty()
            else:
                cursor.execute(query)
                acc = cursor.fetchall()
                for row in acc:
                    userID = row[0]
                    password1 = row[1]
                    if userID == unvar:
                        if password1 == pvar:
                            accind += 1
                            UI.successful_login()

                        if password1 != pvar:
                            accind += 1
                            UI.incorrect_password()

                if accind == 0:
                    UI.account_not_found()

        except Error as err:
            print(f"Error: {err}")
            return None

    def check_query(self, query, credentials):
        try:
            cursor = self.connection.cursor()

            accind = 0
            usr = credentials[0]
            passwrd = credentials[1]

            if usr == "" or passwrd == "":
                UI.read_query_empty()

            else:
                cursor.execute(query)
                acc = cursor.fetchall()
                for row in acc:
                    userID = row[0]
                    password = row[1]

                    if usr == userID:
                        UI.user_exists_error()

                        if password == passwrd:
                            return

                        accind += 1
                        return

                    if passwrd == password:
                        UI.password_unavailable()
                        accind += 1
                        return

                if accind == 0:
                    self.new_credentials(usr, passwrd)

        except Error as err:
            print(f"Error: {err}")

    def multi_query(self, query1, query2, credentials):
        try:
            cursor = self.database.cursor()
            cursor.execute(query2, credentials)
            cursor.execute(query1, credentials)
            self.database.commit()
            cursor.close()
            print("Query Successful")

        except Error as err:
            print(f"Error: {err}")
            return None

    def exist_credentials(self, username, password):
        unvar = username.get()
        pvar = password.get()

        checkCredentials = "SELECT * FROM account;"
        credentials = (unvar, pvar)
        self.read_query(checkCredentials, credentials)

    # creates a new account
    def new_credentials(self, unvar, pvar):
        newAccount = "INSERT INTO account (userID, password1) VALUES (%s, %s);"
        credentials = (unvar, pvar)
        self.execute_query(newAccount, credentials)

    # checks username and password
    def cred_check(self, unvar, pvar):
        usr = unvar.get()
        pswd = pvar.get()
        checuser = "SELECT * FROM account;"
        cred = (usr, pswd)
        self.check_query(checuser, cred)

    def findwebcredentials(self, unvar, table):
        # statement won't accept a StringVar or string so it had to be set to a list
        username = unvar.get()
        usrlist = [username]
        findAcc = "SELECT website, email, username, password2 FROM passwords WHERE userID = %s;"
        user = (usrlist)
        self.find_query(findAcc, user, table)

    def cngPass(self, pvar, newpVar):
        password = pvar.get()
        newpassword = newpVar.get()

        if newpassword == "":
            UI.read_query_empty()

        else:
            UI.account_settings_widget_destroy()
            cngpass = "UPDATE account SET password1 = %s WHERE password1 = %s;"
            accps = (newpassword, password)
            self.execute_query(cngpass, accps)

    def ePSub(self, aPVar, webVar, table):
        global unvar
        password = aPVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editP = "UPDATE passwords SET password2 = %s WHERE userID = %s AND website = %s;"
        pslst = (password, usrID, website)
        self.execute_query(editP, pslst)

    def eUSub(self, aUVar, webVar, table):
        global unvar
        username = aUVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editU = "UPDATE passwords SET username = %s WHERE userID = %s AND website = %s;"
        usrs = (username, usrID, website)
        self.execute_query(editU, usrs)

    def eESub(self, aEVar, webVar, table):
        global unvar
        email = aEVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editE = "UPDATE passwords SET email = %s WHERE userID = %s AND website = %s;"
        emls = (email, usrID, website)
        self.execute_query(editE, emls)

    def delCredentials(self, unvar, webVar, table):
        # gathers info
        user = unvar.get()
        website = webVar.get()

        if website == "":
            UI.read_query_empty()

        else:
            UI.manager_widget_destroy()
            # sets up SQL statement
            delcred = "DELETE FROM passwords WHERE userID = %s AND website = %s;"
            usracc = (user, website)
            self.execute_query(delcred, usracc)
            for row in table.get_children():
                if table.item(row, 'values')[0] == website:
                    table.delete(table.selection_set()[table.index(row)])
            # table.delete(table.selection()[table.index(website)])

    # query delete function for account - couldn't do a INNER JOIN statement, had to use two seperate statements
    def delete_account(self, unvar):
        user = unvar.get()
        user2 = [user]
        delacc1 = "DELETE FROM account WHERE userID = %s;"
        delacc2 = "DELETE FROM passwords WHERE userID = %s;"
        userid = (user2)
        self.multi_query(delacc1, delacc2, userid)

    def applyPassMain(self, pvar, newpVar):
        password = pvar.get()
        newpassword = newpVar
        UI.new_password_widget_destroy()
        cngpass = "UPDATE account SET password1 = %s WHERE password1 = %s;"
        accps = (newpassword, password)
        self.execute_query(cngpass, accps)

    # def applyPassSecondary():
     #   return None