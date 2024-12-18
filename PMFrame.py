from tkinter import *
import os
import mysql.connector
from mysql.connector import Error
import random
import string

def connectioncheck(host_name, usr_name, us_password, cu_database):
    credentialsdb = None
    try:
        credentialsdb = mysql.connector.connect(
            host=host_name,
            user= usr_name,
            password=us_password,
            database=cu_database
        )

        print("connected")
    except Error as err:
        print(f"Error: {err}")
    return credentialsdb

def rdquery(credentialsdb, query, credentials):
    cursor = credentialsdb.cursor()
    try:
        if hasattr(welcome, 'incPass'):
            welcome.incPass.destroy()
        if hasattr(welcome, 'noacc'):
            welcome.noacc.destroy()
        accind = 0
        unvar = credentials[0]
        pvar = credentials[1]
        cursor.execute(query)
        acc = cursor.fetchall()
        for row in acc:
            userID = row[0]
            password1 = row[1]
            if userID == unvar:
                if password1 == pvar:
                    accind += 1
                    mainmenu()

                if password1 != pvar:
                    welcome.incPass = Label(welcome, text= "Incorrect password!")
                    welcome.incPass.pack()
                    accind += 1

        if accind == 0:
            welcome.noacc = Label(welcome, text= "Account doesn't exist")
            welcome.noacc.pack()

    except Error as err:
        print(f"Error: {err}")

def existcredentials(username, password, credentialsdb):
    unvar = username.get()
    pvar = password.get()

    checkCredentials = "SELECT * FROM account;"
    credentials = (unvar, pvar)
    rdquery(credentialsdb, checkCredentials, credentials)

def exquery(credentialsdb, query, credentials= None):
    cursor = credentialsdb.cursor()
    try:
        cursor.execute(query, credentials)
        credentialsdb.commit()
        print("query succesful")
        cursor.close()
    except Error as err:
        print(f"Error: {err}")

def newcredentials(setun,setps,credentialsdb):
    unvar = setun.get()
    pvar = setps.get()

    newAccount = "INSERT INTO account (userID, password1) VALUES (%s, %s);"
    credentials = (unvar, pvar)
    exquery(credentialsdb, newAccount, credentials)

def createaccount():
    #removes welcome frame & widgets
    welcome.pack_forget()
    #shows create account frame and widgets
    caframe.pack()

    for widget in caframe.winfo_children():
        widget.destroy()

    caframe.calbl = Label(caframe, text="New Account Credentials")
    caframe.calbl.pack(side=TOP, padx=0, pady=0)

    caframe.setunlbl = Label(caframe, text="Enter a username")
    caframe.setunlbl.pack(side=TOP, padx=1, pady=0)

    caframe.setun = Entry(caframe, textvariable=unvar, width=30)
    caframe.setun.pack(side=TOP, padx=1, pady=1)

    caframe.setpslbl = Label(caframe, text="Enter a password")
    caframe.setpslbl.pack(side=TOP, padx=2, pady=0)

    caframe.setps = Entry(caframe, show ="*", textvariable=pvar, width=30)
    caframe.setps.pack(side=TOP, padx=2, pady=1)

    caframe.cabtn = Button(caframe, text="Create Account", command = lambda: [newcredentials(setun, setps, credentialsdb), mainmenu()])
    caframe.cabtn.pack(side=TOP, padx=3, pady=0)

    caframe.returnLogin = Button(caframe, text="Return to the Login screen", command= returnwelcome)
    caframe.returnLogin.pack()

def mainmenu():
    #hides login or create account frame
    if welcome:
        welcome.pack_forget()
    if caframe:
        caframe.pack_forget()
    #shows mainmenu frame
    mainMenu.pack()

    #replaces frame
    for widget in mainMenu.winfo_children():
        widget.destroy()

    mainMenu.welcomeMes = Label(mainMenu, text="Welcome to the Super Cool Password Manager")
    mainMenu.welcomeMes.pack()

    mainMenu.managePassButton = Button(mainMenu, text="Current Passwords", command= managepassword)
    mainMenu.managePassButton.pack()

    mainMenu.newPass = Button(mainMenu, text="Password Generator", command= newpassword)
    mainMenu.newPass.pack()

    mainMenu.signoutBtn = Button(mainMenu, text="Sign Out", command= returnwelcome)
    mainMenu.signoutBtn.pack()

#function for the manage password page
def managepassword():
    #hides the original frame & widgets
    mainMenu.pack_forget()
    #shows new frame & widgets
    manpass.pack()

    #replaces label and button when returned to frame
    for widget in manpass.winfo_children():
        widget.destroy()

    manpass.manlabel = Label(manpass, text="Here are your current passwords")
    manpass.manlabel.pack()

    manpass.returnMM1 = Button(manpass, text="Return to Main Menu", command=mmreturn1)
    manpass.returnMM1.pack()

#function for the generate password page
def newpassword():
    # hides the main menu
    mainMenu.pack_forget()
    # shows password page
    npFrame.pack()

    #replaces widgets when returned to page
    global npLabel
    global superCoolButton
    global returnMM2
    global npLbl
    for widget in npFrame.winfo_children():
        widget.destroy()

    npFrame.npLabel = Label(npFrame, text="Click below to generate your new password!")
    npFrame.npLabel.pack()

    npFrame.superCoolButton = Button(npFrame, text="Press me", width=27, command=generateRanPassword)
    npFrame.superCoolButton.pack()

    npFrame.returnMM2 = Button(npFrame, text="Return to Main Menu", command=mmreturn2)
    npFrame.returnMM2.pack()

#function for the password generator
def generateRanPassword():
    #set password to empty string
    pw = ""
    #loop that chooses random characters for the password
    while len(pw) < 18:
        digit = random.randint(0, 9)
        Uletter = random.choice(string.ascii_uppercase)
        Lletter = random.choice(string.ascii_lowercase)
        RCharacter = random.choice("!@#$%&*?")
        PUse = [str(digit), Uletter, Lletter, RCharacter]
        pw += random.choice(PUse)

    #replaces label when returned to frame or when a new password is generated
    global npLbl
    if hasattr(npFrame, 'npLbl'):
        npFrame.npLbl.destroy()

    npFrame.npLbl = Label(npFrame, text="Your new password is " + pw)
    npFrame.npLbl.pack(side=TOP, pady=20)

#function for the sign out or back to log in button
def returnwelcome():
    #hides the main menu or create account frame
    if mainMenu:
        mainMenu.pack_forget()
    if caframe:
        caframe.pack_forget()
    #shows log in frame
    welcome.pack()

def mmreturn1():
    #hides the password page
    manpass.pack_forget()
    #shows main menu
    mainMenu.pack()

#fucntion for returning to the main menu
def mmreturn2():
    # hides the password generator page
    npFrame.pack_forget()
    # shows main menu
    mainMenu.pack()

#function for the log in frame
def welcomeFrame():
    #hides main menu frame
    mainMenu.pack_forget()
    #shows log in frame
    welcome.pack()

    for widget in welcome.winfo_children():
        widget.destroy()

    welcome.loginlbl = Label(welcome, text="Log In to the Super Cool Password Manager")
    welcome.loginlbl.pack(side=TOP, padx=0, pady=0)

    welcome.usernamelbl = Label(welcome, text="Username")
    welcome.usernamelbl.pack(side=TOP, padx=2, pady=0)

    welcome.username = Entry(welcome, textvariable=unvar, width=30)
    welcome.username.pack(side=TOP, padx=2, pady=1)

    welcome.passwordlbl = Label(welcome, text="Password")
    welcome.passwordlbl.pack(side=TOP, padx=3, pady=0)

    welcome.password = Entry(welcome, show="*", textvariable=pvar, width=30)
    welcome.password.pack(side=TOP, padx=3, pady=1)

    welcome.loginbtn = Button(welcome, text="Log in", command=lambda: existcredentials(unvar, pvar, credentialsdb))
    welcome.loginbtn.pack(side=TOP, padx=4, pady=0)

    welcome.nulbl = Label(welcome, text="New User?")
    welcome.nulbl.pack(side=TOP, padx=5, pady=0)

    welcome.nubtn = Button(welcome, text="Create an Account", command=createaccount)
    welcome.nubtn.pack(side=TOP, padx=5, pady=1)

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

#welcome page
welcome = Frame(PMWin)
welcome.pack()

#account creation page
caframe = Frame(PMWin)
caframe.pack()

#main menu page
mainMenu = Frame(PMWin)
mainMenu.pack()

#password manager frame
manpass = Frame(PMWin)
manpass.pack()

#password generator frame
npFrame = Frame(PMWin)
npFrame.pack()

#call welcome frame
welcomeFrame()

#initate main loop
PMWin.mainloop()