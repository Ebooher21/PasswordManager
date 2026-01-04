import mysql.connecter
from mysql.connector import Error

class Connect:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connectioncheck(self):

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
    def exquery(self, query, credentials=None):
        try:
            cursor = self.database.cursor()
            cursor.execute(query, credentials)
            self.database.commit()
            print("query succesful")
            cursor.close()
        except Error as err:
            print(f"Error: {err}")

    # retrieve users passwords
    def fndquery(self, query, username, table):
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
            manpass.noAccLbl = ttk.Label(manpass, text="No accounts for this user...")
            manpass.noAccLbl.pack(padx=2, pady=2)
            return None

    def rdquery(self, query, credentials):
        try:
            cursor = self.database.cursor()
            if hasattr(welcome, 'incPass'):
                welcome.incPass.destroy()
            if hasattr(welcome, 'noacc'):
                welcome.noacc.destroy()
            if hasattr(welcome, 'emptyEntry'):
                welcome.emptyEntry.destroy()

            accind = 0
            unvar = credentials[0]
            pvar = credentials[1]

            if unvar == "" or pvar == "":
                welcome.emptyEntry = ttk.Label(welcome, text="Entry boxes cannot be empty!")
                welcome.emptyEntry.pack()
            else:
                cursor.execute(query)
                acc = cursor.fetchall()
                for row in acc:
                    userID = row[0]
                    password1 = row[1]
                    if userID == unvar:
                        if password1 == pvar:
                            accind += 1
                            mainmenu()
                            widgedestroy(welcome.loginlbl, welcome.usernamelbl,
                                         welcome.username, welcome.passwordlbl,
                                         welcome.password, welcome.loginbtn,
                                         welcome.nulbl, welcome.nubtn)

                        if password1 != pvar:
                            welcome.incPass = ttk.Label(welcome, text="Incorrect password!")
                            welcome.incPass.pack()
                            accind += 1

                if accind == 0:
                    welcome.noacc = ttk.Label(welcome, text="Account doesn't exist")
                    welcome.noacc.pack()

        except Error as err:
            print(f"Error: {err}")
            return None

    def checkque(self, query, credentials):
        cursor = self.connection.cursor()
        try:
            if hasattr(caframe, 'usrexists'):
                caframe.usrexists.destroy()
            if hasattr(caframe, 'pasexists'):
                caframe.pasexists.destroy()
            if hasattr(caframe, 'emptyEntry'):
                caframe.emptyEntry.destroy()

            accind = 0
            usr = credentials[0]
            passwrd = credentials[1]

            if usr == "" or passwrd == "":
                caframe.emptyEntry = ttk.Label(caframe, text="Entry boxes cannot be empty!")
                caframe.emptyEntry.pack()
            else:
                cursor.execute(query)
                acc = cursor.fetchall()
                for row in acc:
                    userID = row[0]
                    password = row[1]
                    if usr == userID:
                        caframe.usrexists = ttk.Label(caframe, text="User already exists!")
                        caframe.usrexists.pack()
                        if password == passwrd:
                            break
                        accind += 1
                        break
                    if passwrd == password:
                        caframe.pasexists = ttk.Label(caframe, text="Password Unavailable")
                        caframe.pasexists.pack()
                        accind += 1
                        break
                if accind == 0:
                    newcredentials(usr, passwrd)
                    mainmenu()
                    widgedestroy(caframe.calbl, caframe.setunlbl,
                                 caframe.setun, caframe.setpslbl, caframe.setps,
                                 caframe.cabtn, caframe.returnLogin)
        except Error as err:
            print(f"Error: {err}")

    def multiquery(self, query1, query2, credentials):
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

    def existcredentials(self, username, password):
        unvar = username.get()
        pvar = password.get()

        checkCredentials = "SELECT * FROM account;"
        credentials = (unvar, pvar)
        rdquery(checkCredentials, credentials)

    # creates a new account
    def newcredentials(self, unvar, pvar):
        newAccount = "INSERT INTO account (userID, password1) VALUES (%s, %s);"
        credentials = (unvar, pvar)
        exquery(newAccount, credentials)

    # checks username and password
    def credcheck(self, unvar, pvar):
        usr = unvar.get()
        pswd = pvar.get()
        checuser = "SELECT * FROM account;"
        cred = (usr, pswd)
        checkque(checuser, cred)

    def findwebcredentials(self, unvar, table):
        # statement won't accept a StringVar or string so it had to be set to a list
        username = unvar.get()
        usrlist = [username]
        findAcc = "SELECT website, email, username, password2 FROM passwords WHERE userID = %s;"
        user = (usrlist)
        fndquery(findAcc, user, table)

    def cngPass(self, pvar, newpVar):
        password = pvar.get()
        newpassword = newpVar.get()
        if hasattr(accsett, 'emptyEntry'):
            accsett.emptyEntry.destroy()
        if newpassword == "":
            accsett.emptyEntry = ttk.Label(accsett, text="Entry boxes cannot be empty!")
            accsett.emptyEntry.pack(padx=2, pady=2)
        else:
            widgedestroy(accsett.newpassLbl,
                         accsett.newpassEntry,
                         accsett.newpassBtn)
            cngpass = "UPDATE account SET password1 = %s WHERE password1 = %s;"
            accps = (newpassword, password)
            exquery(cngpass, accps)

    def ePSub(self, aPVar, webVar, table):
        global unvar
        password = aPVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editP = "UPDATE passwords SET password2 = %s WHERE userID = %s AND website = %s;"
        pslst = (password, usrID, website)
        exquery(editP, pslst)

    def eUSub(self, aUVar, webVar, table):
        global unvar
        username = aUVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editU = "UPDATE passwords SET username = %s WHERE userID = %s AND website = %s;"
        usrs = (username, usrID, website)
        exquery(editU, usrs)

    def eESub(self, aEVar, webVar, table):
        global unvar
        email = aEVar.get()
        usrID = unvar.get()
        website = webVar.get()
        editE = "UPDATE passwords SET email = %s WHERE userID = %s AND website = %s;"
        emls = (email, usrID, website)
        exquery(editE, emls)

    def delCredentials(self, unvar, webVar, table):
        # gathers info
        user = unvar.get()
        website = webVar.get()
        if hasattr(manpass, 'emptyEntry'):
            manpass.emptyEntry.destroy()
        if website == "":
            manpass.emptyEntry = ttk.Label(manpass, text="Entry boxes cannot be empty!")
            manpass.emptyEntry.pack(padx=2, pady=2)
        else:
            widgedestroy(manpass.webLbl, manpass.webEntry, manpass.webBtn, manpass.cancelBtn)
            # sets up SQL statement
            delcred = "DELETE FROM passwords WHERE userID = %s AND website = %s;"
            usracc = (user, website)
            exquery(delcred, usracc)
            for row in table.get_children():
                if table.item(row, 'values')[0] == website:
                    table.delete(table.selection_set()[table.index(row)])
            # table.delete(table.selection()[table.index(website)])

    # query delete function for account - couldn't do a INNER JOIN statement, had to use two seperate statements
    def delAccount(self, unvar):
        user = unvar.get()
        user2 = [user]
        delacc1 = "DELETE FROM account WHERE userID = %s;"
        delacc2 = "DELETE FROM passwords WHERE userID = %s;"
        userid = (user2)
        multiquery(delacc1, delacc2, userid)

    def applyPassMain(self, pvar, newpVar):
        password = pvar.get()
        newpassword = newpVar
        widgedestroy(npFrame.npLbl,
                     npFrame.npUse)
        cngpass = "UPDATE account SET password1 = %s WHERE password1 = %s;"
        accps = (newpassword, password)
        exquery(cngpass, accps)

    # def applyPassSecondary():
     #   return None