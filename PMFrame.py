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
        cursor.execute(query, credentials)
        credentialsdb.commit()
        acc = cursor.fetchone()
        if acc:
            print("were good")
        else:
            print("problem")
        cursor.close()
    except Error as err:
        print(f"Error: {err}")

def existcredentials(username, password, credentialsdb):
    unvar = username.get()
    pvar = password.get()

    checkCredentials = "SELECT userID, password1 FROM account WHERE userID = %s AND password1 = %s;"
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
    welcome.pack_forget()

    caframe.pack()

    calbl = Label(caframe, text="New Account Credentials")
    calbl.pack(side=TOP, padx=0, pady=0)

    setunlbl = Label(caframe, text="Enter a username")
    setunlbl.pack(side=TOP, padx=1, pady=0)

    setun = Entry(caframe, textvariable=unvar, width=30)
    setun.pack(side=TOP, padx=1, pady=1)

    setpslbl = Label(caframe, text="Enter a password")
    setpslbl.pack(side=TOP, padx=2, pady=0)

    setps = Entry(caframe, textvariable=pvar, width=30)
    setps.pack(side=TOP, padx=2, pady=1)

    cabtn = Button(caframe, text="Create Account", command = lambda: [newcredentials(setun, setps, credentialsdb), mainmenu()])
    cabtn.pack(side=TOP, padx=3, pady=0)

def mainmenu():
    #hides login frame
    welcome.pack_forget()
    caframe.pack_forget()
    #shows mainmenu frame
    mainMenu.pack()

    #replaces frame
    if hasattr(welcome, 'loginlbl') and hasattr(welcome, 'usernamelbl') and hasattr(welcome, 'username') and hasattr(
            welcome, 'passwordlbl') and hasattr(welcome, 'password') and hasattr(welcome, 'loginbtn') and hasattr(
        welcome, 'nulbl') and hasattr(welcome, 'nubtn'):
        welcome.loginlbl.destroy()
        welcome.usernamelbl.destory()
        welcome.username.destroy()
        welcome.passwordlbl.destroy()
        welcome.password.destory()
        welcome.loginbtn.destroy()
        welcome.nulbl.destory()
        welcome.nubtn.destory()

    welcomeMes = Label(mainMenu, text="Welcome to the Super Cool Password Manager")
    welcomeMes.pack()

    managePassButton = Button(mainMenu, text="Current Passwords", command=managepassword)
    managePassButton.pack()

    newPass = Button(mainMenu, text="Password Generator", command=newpassword)
    newPass.pack()

#function for the manage password page
def managepassword():
    #hides the original frame & widgets
    mainMenu.pack_forget()
    #shows new frame & widgets
    manpass.pack()

    #replaces label and button when returned to frame
    if hasattr(manpass, 'manlabel') and hasattr(manpass, 'returnMM1'):
        manpass.manlabel.destroy()
        manpass.returnMM1.destroy()

    manpass.manlabel = Label(manpass, text="Here are your current passwords")
    manpass.manlabel.pack()

    manpass.returnMM1 = Button(manpass, text="Return to Main Menu", command=mmreturn1)
    manpass.returnMM1.pack()

def mmreturn1():
    #hides the password page
    manpass.pack_forget()
    #shows main menu
    mainMenu.pack()

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
    if hasattr(npFrame, 'npLabel') and hasattr(npFrame, 'superCoolButton') and hasattr(npFrame,'returnMM2') and hasattr(npFrame,'npLbl'):
        npFrame.npLabel.destroy()
        npFrame.superCoolButton.destroy()
        npFrame.returnMM2.destroy()
        npFrame.npLbl.destroy()

    npFrame.npLabel = Label(npFrame, text="Click below to generate your new password!")
    npFrame.npLabel.pack()

    npFrame.superCoolButton = Button(npFrame, text="Press me", width=27, command=generateRanPassword)
    npFrame.superCoolButton.pack()

    npFrame.returnMM2 = Button(npFrame, text="Return to Main Menu", command=mmreturn2)
    npFrame.returnMM2.pack()

#fucntion for returning to the main menu
def mmreturn2():
    # hides the password generator page
    npFrame.pack_forget()
    # shows main menu
    mainMenu.pack()

#function for the password generator
def generateRanPassword():
    pw = ""
    while len(pw) < 18:
        digit = random.randint(0, 9)
        Uletter = random.choice(string.ascii_uppercase)
        Lletter = random.choice(string.ascii_lowercase)
        RCharacter = random.choice("!@#$%&*?")
        PUse = [str(digit), Uletter, Lletter, RCharacter]
        pw += random.choice(PUse)

    #replaces label when returned to frame - I may mess with this in the future
    global npLbl
    if hasattr(npFrame, 'npLbl'):
        npFrame.npLbl.destroy()

    npFrame.npLbl = Label(npFrame, text="Your new password is " + pw)
    npFrame.npLbl.pack(side=TOP, pady=20)


#uses created environmental variables
db_host = os.environ.get('db_host')
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_database = os.environ.get('db_database')

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

loginlbl = Label(welcome, text="Log In to the Super Cool Password Manager")
loginlbl.pack(side=TOP, padx=0, pady=0)

usernamelbl = Label(welcome, text="Username")
usernamelbl.pack(side=TOP, padx=2, pady=0)

username = Entry(welcome, textvariable=unvar, width=30)
username.pack(side=TOP, padx=2, pady=1)

passwordlbl = Label(welcome, text="Password")
passwordlbl.pack(side=TOP, padx=3, pady=0)

password = Entry(welcome, textvariable=pvar, width=30)
password.pack(side=TOP, padx=3, pady=1)

loginbtn = Button(welcome, text="Log in", command= existcredentials(unvar, pvar, credentialsdb))
loginbtn.pack(side=TOP, padx=4, pady=0)

nulbl = Label(welcome, text="New User?")
nulbl.pack(side=TOP, padx=5, pady=0)

nubtn = Button(welcome, text="Create an Account", command=createaccount)
nubtn.pack(side=TOP, padx=5, pady=1)

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

PMWin.mainloop()