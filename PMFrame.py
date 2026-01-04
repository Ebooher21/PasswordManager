import os
import mysql.connector
from mysql.connector import Error


def checkque(credentialsdb, query, credentials):
    cursor = credentialsdb.cursor()
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
            caframe.emptyEntry = ttk.Label(caframe, text = "Entry boxes cannot be empty!")
            caframe.emptyEntry.pack()
        else:
            cursor.execute(query)
            acc = cursor.fetchall()
            for row in acc:
                userID = row[0]
                password = row[1]
                if usr == userID:
                    caframe.usrexists = ttk.Label(caframe, text= "User already exists!")
                    caframe.usrexists.pack()
                    if password == passwrd:
                        break
                    accind += 1
                    break
                if passwrd == password:
                    caframe.pasexists = ttk.Label(caframe, text= "Password Unavailable")
                    caframe.pasexists.pack()
                    accind += 1
                    break
            if accind == 0:
                newcredentials(usr, passwrd, credentialsdb)
                mainmenu()
                widgedestroy(caframe.calbl, caframe.setunlbl,
                             caframe.setun, caframe.setpslbl, caframe.setps,
                             caframe.cabtn, caframe.returnLogin)
    except Error as err:
        print(f"Error: {err}")

#uses created environmental variables
db_host = os.environ.get('db_host')
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_database = os.environ.get('db_database')

#connection variable so the functions can access the database
credentialsdb = connectioncheck(db_host, db_user, db_password, db_database)

#mainwindow setup
PMWin = Tk()
PMWin.geometry("500x400")
PMWin.title('Super Cool Password Manager')

#set string variables for frame command use
unvar = StringVar()
pvar = StringVar()
webVar = StringVar()
usrVar = StringVar()
emlVar = StringVar()
pasVar = StringVar()
newunVar = StringVar()
newpVar = StringVar()
aUVar = StringVar()
aEVar = StringVar()
aPVar = StringVar()

#welcome page
welcome = ttk.Frame(PMWin)
welcome.pack()

#account creation page
caframe = ttk.Frame(PMWin)
caframe.pack()

#main menu page
mainMenu = ttk.Frame(PMWin)
mainMenu.pack()

#password manager frame
manpass = ttk.Frame(PMWin)
manpass.pack()

#password generator frame
npFrame = ttk.Frame(PMWin)
npFrame.pack()

#account settings frame
accsett = ttk.Frame(PMWin)
accsett.pack()

#call welcome frame
welcomeFrame()

#initate main loop
PMWin.mainloop()
