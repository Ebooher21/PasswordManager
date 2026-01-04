import os
import mysql.connector
from mysql.connector import Error

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
