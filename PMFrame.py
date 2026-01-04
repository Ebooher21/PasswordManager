import os
import mysql.connector
from mysql.connector import Error



def rdquery(credentialsdb, query, credentials):
    cursor = credentialsdb.cursor()
    try:
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
            welcome.emptyEntry = ttk.Label(welcome, text = "Entry boxes cannot be empty!")
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
                        welcome.incPass = ttk.Label(welcome, text= "Incorrect password!")
                        welcome.incPass.pack()
                        accind += 1

            if accind == 0:
                welcome.noacc = ttk.Label(welcome, text= "Account doesn't exist")
                welcome.noacc.pack()

    except Error as err:
        print(f"Error: {err}")

def existcredentials(username, password, credentialsdb):
    unvar = username.get()
    pvar = password.get()

    checkCredentials = "SELECT * FROM account;"
    credentials = (unvar, pvar)
    rdquery(credentialsdb, checkCredentials, credentials)

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



def cngPass(credentialsdb,pvar,newpVar):
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
        accps = (newpassword,password)
        exquery(credentialsdb, cngpass,accps)



def eUSub(aUVar, webVar, table):
    global unvar
    username = aUVar.get()
    usrID = unvar.get()
    website = webVar.get()
    editU = "UPDATE passwords SET username = %s WHERE userID = %s AND website = %s;"
    usrs = (username, usrID, website)
    exquery(credentialsdb, editU, usrs)

def eESub(aEVar, webVar, table):
    global unvar
    email = aEVar.get()
    usrID = unvar.get()
    website = webVar.get()
    editE = "UPDATE passwords SET email = %s WHERE userID = %s AND website = %s;"
    emls = (email, usrID, website)
    exquery(credentialsdb, editE, emls)

def editPass(webVar,table):
    manpass.passEnt = ttk.Entry(manpass, textvariable= aPVar)
    manpass.passEnt.pack()
    manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                  command=lambda: [ePSub(aPVar, webVar, table),widgedestroy(manpass.passEnt,manpass.edsubmit)])
    manpass.edsubmit.pack(pady=2)
    manpass.passEnt.delete(0, END)
    PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

def ePSub(aPVar, webVar, table):
    global unvar
    password = aPVar.get()
    usrID = unvar.get()
    website = webVar.get()
    editP = "UPDATE passwords SET password2 = %s WHERE userID = %s AND website = %s;"
    pslst = (password,usrID,website)
    exquery(credentialsdb,editP,pslst)



def webCredentials(unvar, webVar, usrVar, emlVar, pasVar, table):
    userID = unvar.get()
    website = webVar.get()
    username = usrVar.get()
    email = emlVar.get()
    password = pasVar.get()
    if hasattr(manpass, 'emptyEntry'):
        manpass.emptyEntry.destroy()
    if website == "" or username == "" or email == "" or password == "":
        manpass.emptyEntry = ttk.Label(manpass, text = "Entry boxes cannot be empty!")
        manpass.emptyEntry.pack(padx=2, pady=2)
    else:
        widgedestroy(manpass.weblbl, manpass.webentry,
                             manpass.usrlbl, manpass.usrentry,
                             manpass.emllbl, manpass.emlentry,
                             manpass.paslbl, manpass.pasentry,
                             manpass.submitBtn, manpass.cancelBtn)
        pasAcc = "INSERT INTO passwords (userID, website, email, username, password2) VALUES (%s, %s, %s, %s, %s);"
        credentials = (userID, website, email, username, password)
        exquery(credentialsdb, pasAcc, credentials)

        manpass.table.insert("","end", values=(website,email,username,password))

def deleteCredbtn(table):
    global unvar
    # user prompt
    manpass.webLbl = ttk.Label(manpass, text="Enter the website credentials you would like to delete:")
    manpass.webLbl.pack(padx=2, pady=2)
    manpass.webEntry = ttk.Entry(manpass, textvariable=webVar, width=30)
    manpass.webEntry.pack(padx=2, pady=2)
    manpass.webBtn = ttk.Button(manpass, text="Submit",
                            command=lambda:delCredentials(credentialsdb,unvar,webVar,table))
    manpass.webBtn.pack(padx=2, pady=2)
    manpass.cancelBtn = ttk.Button(manpass, text="cancel",
                                   command=lambda:widgedestroy(manpass.webLbl,
                                                               manpass.webEntry,
                                                               manpass.webBtn,
                                                               manpass.cancelBtn))
    manpass.cancelBtn.pack()
    manpass.webEntry.delete(0,END)
    PMWin.bind('<Return>', lambda event: manpass.webBtn.invoke())

def delCredentials(credentialsdb, unvar, webVar,table):
    #gathers info
    user = unvar.get()
    website = webVar.get()
    if hasattr(manpass, 'emptyEntry'):
        manpass.emptyEntry.destroy()
    if website == "":
        manpass.emptyEntry = ttk.Label(manpass, text = "Entry boxes cannot be empty!")
        manpass.emptyEntry.pack(padx=2, pady=2)
    else:
        widgedestroy(manpass.webLbl, manpass.webEntry, manpass.webBtn, manpass.cancelBtn)
        #sets up SQL statement
        delcred = "DELETE FROM passwords WHERE userID = %s AND website = %s;"
        usracc = (user, website)
        exquery(credentialsdb,delcred,usracc)
        for row in table.get_children():
            if table.item(row, 'values')[0] == website:
                table.delete(table.selection_set()[table.index(row)])
        #table.delete(table.selection()[table.index(website)])

#query delete function for account - couldn't do a INNER JOIN statement, had to use two seperate statements
def delAccount(credentialsdb,unvar):
    user = unvar.get()
    user2 = [user]
    delacc1 = "DELETE FROM account WHERE userID = %s;"
    delacc2 = "DELETE FROM passwords WHERE userID = %s;"
    userid = (user2)
    multiquery(credentialsdb, delacc1, delacc2, userid)


def applyPassMain(credentialsdb,pvar,newpVar):
    password = pvar.get()
    newpassword = newpVar
    widgedestroy(npFrame.npLbl,
                 npFrame.npUse)
    cngpass = "UPDATE account SET password1 = %s WHERE password1 = %s;"
    accps = (newpassword,password)
    exquery(credentialsdb, cngpass,accps)

def applyPassSecondary():
    pass


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
