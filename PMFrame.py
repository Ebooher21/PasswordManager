from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
import random
import string

def connectioncheck(host_name, usr_name, us_password, cu_database):
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

def exquery(credentialsdb, query, credentials= None):
    cursor = credentialsdb.cursor()
    try:
        cursor.execute(query, credentials)
        credentialsdb.commit()
        print("query succesful")
        cursor.close()
    except Error as err:
        print(f"Error: {err}")

def newcredentials(unvar,pvar,credentialsdb):
    newAccount = "INSERT INTO account (userID, password1) VALUES (%s, %s);"
    credentials = (unvar, pvar)
    exquery(credentialsdb, newAccount, credentials)

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

def credcheck(credentialsdb, unvar, pvar):
    usr = unvar.get()
    pswd = pvar.get()
    checuser = "SELECT * FROM account;"
    cred = (usr,pswd)
    checkque(credentialsdb, checuser, cred)

def createaccount():
    #removes empty space of welcome frame widgets
    welcome.pack_forget()
    caframe.pack()

    if hasattr(caframe, 'usrexists'):
        caframe.usrexists.destroy()
    if hasattr(caframe, 'pasexists'):
        caframe.pasexists.destroy()
    if hasattr(caframe, 'emptyEntry'):
        caframe.emptyEntry.destroy()

    caframe.calbl = ttk.Label(caframe, text="New Account Credentials")
    caframe.calbl.pack(side=TOP, padx=20, pady=20)

    caframe.setunlbl = ttk.Label(caframe, text="Enter a username")
    caframe.setunlbl.pack(side=TOP, padx=2, pady=2)

    caframe.setun = ttk.Entry(caframe, textvariable=unvar, width=30)
    caframe.setun.pack(side=TOP, padx=2, pady=2)

    caframe.setpslbl = ttk.Label(caframe, text="Enter a password")
    caframe.setpslbl.pack(side=TOP, padx=2, pady=2)

    caframe.setps = ttk.Entry(caframe, show ="*", textvariable=pvar, width=30)
    caframe.setps.pack(side=TOP, padx=2, pady=2)

    caframe.cabtn = ttk.Button(caframe, text="Create Account",
                           command = lambda: credcheck(credentialsdb,unvar,pvar))
    caframe.cabtn.pack(side=TOP, padx=2, pady=2)

    # clears the entry textbox after the information is submitted
    caframe.setun.delete(0,END)
    caframe.setps.delete(0,END)

    # binds the Enter key to the button
    PMWin.bind('<Return>', lambda event: caframe.cabtn.invoke())

    caframe.returnLogin = ttk.Button(caframe, text="Return to the Login screen",
                                     command= lambda: [welcomeFrame(),
                                                       widgedestroy(caframe.calbl,caframe.setunlbl,
                                                           caframe.setun,caframe.setpslbl,caframe.setps,
                                                           caframe.cabtn,caframe.returnLogin)])
    caframe.returnLogin.pack(padx=20, pady=20)

def mainmenu():
    if caframe:
        caframe.pack_forget()
    if welcome:
        welcome.pack_forget()
    if npFrame:
        npFrame.pack_forget()
    if manpass:
        manpass.pack_forget()
    if accsett:
        accsett.pack_forget()
    mainMenu.pack()

    mainMenu.welcomeMes = ttk.Label(mainMenu, text="Super Cool Main Menu")
    mainMenu.welcomeMes.pack(padx=20, pady=20)

    mainMenu.managePassButton = ttk.Button(mainMenu, text="Current Passwords",
                                           command= lambda:[managepassword(),widgedestroy(mainMenu.welcomeMes,
                                                                    mainMenu.managePassButton,mainMenu.newPass,
                                                                    mainMenu.accsettings,mainMenu.signoutBtn)])
    mainMenu.managePassButton.pack(padx=5, pady=5)

    mainMenu.newPass = ttk.Button(mainMenu, text="Password Generator",
                                  command= lambda:[newpassword(),widgedestroy(mainMenu.welcomeMes,
                                                                    mainMenu.managePassButton,mainMenu.newPass,
                                                                    mainMenu.accsettings,mainMenu.signoutBtn)])
    mainMenu.newPass.pack(padx=5, pady=5)

    mainMenu.accsettings = ttk.Button(mainMenu, text="Account Settings",
                                      command= lambda: [accountsett(),widgedestroy(mainMenu.welcomeMes,
                                                                    mainMenu.managePassButton,mainMenu.newPass,
                                                                    mainMenu.accsettings,mainMenu.signoutBtn)])
    mainMenu.accsettings.pack(padx=5, pady=5)

    mainMenu.signoutBtn = ttk.Button(mainMenu, text="Sign Out",
                                     command= lambda: [welcomeFrame(),widgedestroy(mainMenu.welcomeMes,
                                                                    mainMenu.managePassButton,mainMenu.newPass,
                                                                    mainMenu.accsettings,mainMenu.signoutBtn)])
    mainMenu.signoutBtn.pack(padx=5, pady=5)

#function for the manage password page
def managepassword():
    mainMenu.pack_forget()
    manpass.pack()

    manpass.manlabel = ttk.Label(manpass, text="Here are your current passwords")
    manpass.manlabel.pack(padx=10, pady=10)

    findwebcredentials(credentialsdb, unvar)

    manpass.editbtn = ttk.Button(manpass, text="Edit an Account", command= lambda:webcredentry())
    manpass.editbtn.pack(padx=2, pady=2)

    manpass.addAccBtn = ttk.Button(manpass, text="Add a new Website Account", command=addWeb)
    manpass.addAccBtn.pack(padx=2, pady=2)

    manpass.deleteBtn = ttk.Button(manpass, text= "Delete an Account", command= lambda:deleteCredbtn())
    manpass.deleteBtn.pack(padx=2, pady=2)

    manpass.returnMM1 = ttk.Button(manpass, text="Return to Main Menu",
                                   command= lambda: [mainmenu(), widgedestroy(manpass.manlabel,
                                                                            manpass.editbtn,
                                                                            manpass.addAccBtn,
                                                                            manpass.deleteBtn,
                                                                            manpass.returnMM1,
                                                                            manpass.websitelbl,
                                                                            manpass.emaillbl,
                                                                            manpass.usrlbl,
                                                                            manpass.password)])
    manpass.returnMM1.pack(pady=2)

def accountsett():
    mainMenu.pack_forget()
    accsett.pack()

    global unvar
    global pvar
    accsett.inLbl = ttk.Label(accsett, text="Account Settings")
    accsett.inLbl.pack(pady=20)

    accsett.usredit = ttk.Button(accsett, text="Change Username", command=lambda:cngUserEntry(unvar))
    accsett.usredit.pack(pady=5)

    accsett.psedit = ttk.Button(accsett, text="Change Password", command=lambda:cngPassEntry(pvar))
    accsett.psedit.pack(pady=5)

    accsett.delacc = ttk.Button(accsett, text="Delete Account", command=lambda:warningmess(unvar))
    accsett.delacc.pack(pady=5)

    accsett.returnmm = ttk.Button(accsett, text="Return to the Main Menu",
                                  command= lambda: [mainmenu(),
                                                    widgedestroy(accsett.inLbl,accsett.usredit,
                                                                 accsett.psedit,accsett.delacc,
                                                                 accsett.returnmm)])
    accsett.returnmm.pack(pady=10)

def cngUserEntry(unvar):
    accsett.newusrnameLbl = ttk.Label(accsett, text="Enter your new username:")
    accsett.newusrnameLbl.pack(padx=2, pady=2)
    accsett.newusrnameEntry = ttk.Entry(accsett, textvariable= newunVar,width=30)
    accsett.newusrnameEntry.pack(padx=2, pady=2)
    accsett.newusrnameBtn = ttk.Button(accsett,text="Submit",
                                   command=lambda: [cngUser(credentialsdb,unvar,newunVar),
                                                    widgedestroy(accsett.newusrnameLbl,accsett.newusrnameEntry,
                                                                 accsett.newusrnameBtn,accsett.cancelBtn)])
    accsett.newusrnameBtn.pack(padx=2, pady=2)
    accsett.cancelBtn = ttk.Button(accsett, text="Cancel",
                                   command=lambda:
                                   widgedestroy(accsett.newusrnameLbl,
                                                accsett.newusrnameEntry,
                                                accsett.newusrnameBtn,
                                                accsett.cancelBtn))
    accsett.cancelBtn.pack(padx=2, pady=2)
    # clears the entry textbox after the information is submitted
    accsett.newusrnameEntry.delete(0,END)
    # binds the Enter key to the button
    PMWin.bind('<Return>', lambda event: accsett.newusrnameBtn.invoke())

def cngPassEntry(pvar):
    accsett.newpassLbl = ttk.Label(accsett, text="Enter your new password:")
    accsett.newpassLbl.pack(padx=2, pady=2)
    accsett.newpassEntry = ttk.Entry(accsett, textvariable=newpVar,width= 30)
    accsett.newpassEntry.pack(padx=2, pady=2)
    accsett.newpassBtn = ttk.Button(accsett, text="Submit",
                                command=lambda: [cngPass(credentialsdb,pvar,newpVar),
                                                 widgedestroy(accsett.newpassLbl,accsett.newpassEntry,
                                                              accsett.cancelBtn)])
    accsett.newpassBtn.pack(padx=2, pady=2)
    accsett.cancelBtn = ttk.Button(accsett, text="Cancel",
                                   command=lambda:
                                   widgedestroy(accsett.newpassLbl,
                                                accsett.newpassEntry,
                                                accsett.newpassBtn,
                                                accsett.cancelBtn))
    accsett.cancelBtn.pack(padx=2, pady=2)
    # clears the entry textbox after the information is submitted
    accsett.newpassEntry.delete(0,END)
    # binds the Enter key to the button
    PMWin.bind('<Return>', lambda event: accsett.newpassBtn.invoke())

def cngUser(credentialsdb,unvar,newunVar):
    user = unvar.get()
    newuser = newunVar.get()
    if hasattr(accsett, 'emptyEntry'):
        accsett.emptyEntry.destroy()
    if newuser == "":
        accsett.emptyEntry = ttk.Label(accsett, text="Entry boxes cannot be empty!")
        accsett.emptyEntry.pack()
    else:
        widgedestroy(accsett.newusrnameLbl,
                     accsett.newusrnameEntry,
                     accsett.newusrnameBtn)
        cngusr = "UPDATE account SET userID = %s WHERE userID = %s;"
        acc = (newuser, user)
        exquery(credentialsdb,cngusr,acc)

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

def warningmess(unvar):
    choice = messagebox.askyesno("Delete Account", "Are you sure?")
    if choice:
        #probably a password verification will be implemented here
        delAccount(credentialsdb,unvar)
        welcomeFrame()
    else:
        print("will change soon")

def fndquery(credentialsdb, query, username):
    cursor = credentialsdb.cursor()
    try:
        cursor.execute(query, username)
        acc = cursor.fetchall()
        for row in acc:
            website = row[0]
            email = row[1]
            username = row[2]
            password2 = row[3]
            manpass.websitelbl = ttk.Label(manpass, text= website)
            manpass.websitelbl.pack(padx=10, pady=10)
            manpass.emaillbl = ttk.Label(manpass, text= "Email: "+ email)
            manpass.emaillbl.pack(padx=2, pady=2)
            manpass.usrlbl = ttk.Label(manpass, text= "Username: "+ username)
            manpass.usrlbl.pack(padx=2, pady=2)
            manpass.password = ttk.Label(manpass, text= "Password: "+ password2)
            manpass.password.pack(padx=2, pady=2)
    except Error:
        manpass.noAccLbl = ttk.Label(manpass, text="No accounts for this user...")
        manpass.noAccLbl.pack(padx=2, pady=2)

def findwebcredentials(credentialsdb, unvar):
    #statement won't accept a StringVar or string so it had to be set to a list
    username = unvar.get()
    usrlist = [username]
    findAcc = "SELECT website, email, username, password2 FROM passwords WHERE userID = %s;"
    user = (usrlist)
    fndquery(credentialsdb, findAcc, user)

def widgedestroy(*args):
    for widget in args:
        widget.destroy()

def editUser(webVar):
    manpass.userEnt = ttk.Entry(manpass, textvariable= aUVar)
    manpass.userEnt.pack()
    manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                  command=lambda: [eUSub(aUVar, webVar),
                                                   widgedestroy(manpass.userEnt,
                                                                manpass.edsubmit)])
    manpass.edsubmit.pack(pady=2)
    manpass.userEnt.delete(0, END)
    PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

def eUSub(aUVar, webVar):
    username = aUVar.get()
    usms = usrVar.get()
    website = webVar.get()
    editU = "UPDATE passwords SET username = %s WHERE username = %s AND website = %s;"
    usrs = (username, usms, website)
    exquery(credentialsdb, editU, usrs)

def editEmail(webVar):
    manpass.emaillbl = ttk.Label(manpass, text= "Enter a new email:")
    manpass.emaillbl.pack()
    manpass.emailEnt = ttk.Entry(manpass, textvariable= aEVar)
    manpass.emailEnt.pack()
    manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                  command=lambda: [eESub(aEVar,webVar),widgedestroy(manpass.emaillbl,manpass.emailEnt,manpass.edsubmit)])
    manpass.edsubmit.pack(pady=2)
    manpass.emailEnt.delete(0, END)
    PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

def eESub(aEVar, webVar):
    global emlVar
    email = aEVar.get()
    ogeml = emlVar.get()
    website = webVar.get()
    editE = "UPDATE passwords SET email = %s WHERE email = %s AND website = %;"
    emls = (email, ogeml, website)
    exquery(credentialsdb, editE, emls)

def editPass(webVar):
    manpass.passEnt = ttk.Entry(manpass, textvariable= aPVar)
    manpass.passEnt.pack()
    manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                  command=lambda: [ePSub(aPVar, webVar),widgedestroy(manpass.passEnt,manpass.edsubmit)])
    manpass.edsubmit.pack(pady=2)
    manpass.passEnt.delete(0, END)
    PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

def ePSub(aPVar, webVar):
    password = aPVar.get()
    ogpass = pasVar.get()
    website = webVar.get()
    editP = "UPDATE passwords SET password2 = %s WHERE password = %s AND website = %s;"
    pslst = (password,ogpass,website)
    exquery(credentialsdb,editP,pslst)

def specificweb(webVar):
    manpass.edemail = ttk.Button(manpass, text="Change Email", command=lambda: editEmail(webVar))
    manpass.edemail.pack(pady=2)
    manpass.edusr = ttk.Button(manpass, text="Change Username", command=lambda:editUser(webVar))
    manpass.edusr.pack(pady=2)
    manpass.edpass= ttk.Button(manpass, text="Change Password", command=lambda:editPass(webVar))
    manpass.edpass.pack(pady=2)
    manpass.edcancel = ttk.Button(manpass, text="Close",
                                  command=lambda:widgedestroy(manpass.edusr,manpass.edemail,
                                                           manpass.edpass, manpass.edcancel))
    manpass.edcancel.pack(pady=2)

def webcredentry():
    manpass.editlbl = ttk.Label(manpass, text="Enter the website you would like to edit:")
    manpass.editlbl.pack()
    manpass.editentry = ttk.Entry(manpass, textvariable= webVar, width=30)
    manpass.editentry.pack()
    manpass.editbtn = ttk.Button(manpass, text="Submit",
                                 command=lambda:[specificweb(webVar),
                                                 widgedestroy(manpass.editlbl,
                                                              manpass.editentry,
                                                              manpass.editbtn,
                                                              manpass.cancelbtn)])
    manpass.editbtn.pack()
    manpass.cancelbtn = ttk.Button(manpass, text="Cancel",
                                   command=lambda: widgedestroy(manpass.editlbl,
                                                                manpass.editentry,
                                                                manpass.editbtn,
                                                                manpass.cancelbtn))
    manpass.cancelbtn.pack()

    #clears entry box
    manpass.editentry.delete(0,END)
    #binds enter key to button
    PMWin.bind('<Return>', lambda event: manpass.editbtn.invoke())

def addWeb():
    global unvar
    manpass.weblbl = ttk.Label(manpass, text= "Enter the website:")
    manpass.weblbl.pack(padx=2, pady=2)
    manpass.webentry = ttk.Entry(manpass, textvariable=webVar, width=30)
    manpass.webentry.pack(padx=2, pady=2)

    manpass.usrlbl = ttk.Label(manpass, text="Enter the username:")
    manpass.usrlbl.pack(padx=2, pady=2)
    manpass.usrentry = ttk.Entry(manpass, textvariable=usrVar, width=30)
    manpass.usrentry.pack(padx=2, pady=2)

    manpass.emllbl = ttk.Label(manpass, text="Enter the email:")
    manpass.emllbl.pack(padx=2, pady=2)
    manpass.emlentry = ttk.Entry(manpass, textvariable=emlVar, width=30)
    manpass.emlentry.pack(padx=2, pady=2)

    manpass.paslbl = ttk.Label(manpass, text="Enter the password:")
    manpass.paslbl.pack(padx=2, pady=2)
    manpass.pasentry = ttk.Entry(manpass, textvariable=pasVar, width=30)
    manpass.pasentry.pack(padx=2, pady=2)

    manpass.submitBtn = ttk.Button(manpass, text="Submit",
                               command=lambda: webCredentials(unvar, webVar, usrVar, emlVar, pasVar))
    manpass.submitBtn.pack(padx=2, pady=2)

    manpass.cancelBtn = ttk.Button(manpass, text="Cancel",
                                   command= lambda:widgedestroy(manpass.weblbl,
                                                                manpass.webentry, manpass.usrlbl,
                                                                manpass.usrentry,manpass.emllbl,
                                                                manpass.emlentry,manpass.paslbl,
                                                                manpass.pasentry,manpass.submitBtn,
                                                                manpass.cancelBtn))
    manpass.cancelBtn.pack(padx=2, pady=2)

    #clears the entry textbox after the information is submitted
    manpass.webentry.delete(0,END)
    manpass.usrentry.delete(0,END)
    manpass.emlentry.delete(0,END)
    manpass.pasentry.delete(0,END)
    # binds the Enter key to the button
    PMWin.bind('<Return>', lambda event: manpass.submitBtn.invoke())

def webCredentials(unvar, webVar, usrVar, emlVar, pasVar):
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

        #doesn't completely work as inteded but works for now
        manpass.websitelbl = ttk.Label(manpass, text=website)
        manpass.websitelbl.pack(padx=10, pady=10)
        manpass.emaillbl = ttk.Label(manpass, text="Email: " + email)
        manpass.emaillbl.pack(padx=2, pady=2)
        manpass.usrlbl = ttk.Label(manpass, text="Username: " + username)
        manpass.usrlbl.pack(padx=2, pady=2)
        manpass.password = ttk.Label(manpass, text="Password: " + password)
        manpass.password.pack(padx=2, pady=2)

def deleteCredbtn():
    global unvar
    # user prompt
    manpass.webLbl = ttk.Label(manpass, text="Enter the website credentials you would like to delete:")
    manpass.webLbl.pack(padx=2, pady=2)
    manpass.webEntry = ttk.Entry(manpass, textvariable=webVar, width=30)
    manpass.webEntry.pack(padx=2, pady=2)
    manpass.webBtn = ttk.Button(manpass, text="Submit",
                            command=lambda:delCredentials(credentialsdb,unvar,webVar))
    manpass.webBtn.pack(padx=2, pady=2)
    manpass.cancelBtn = ttk.Button(manpass, text="cancel",
                                   command=lambda:widgedestroy(manpass.webLbl,
                                                               manpass.webEntry,
                                                               manpass.webBtn,
                                                               manpass.cancelBtn))
    manpass.cancelBtn.pack()
    manpass.webEntry.delete(0,END)
    PMWin.bind('<Return>', lambda event: manpass.webBtn.invoke())

def delCredentials(credentialsdb, unvar, webVar):
    #gathers info
    user = unvar.get()
    website = webVar.get()
    if hasattr(manpass, 'emptyEntry'):
        manpass.emptyEntry.destroy()
    if website == "":
        manpass.emptyEntry = ttk.Label(manpass, text = "Entry boxes cannot be empty!")
        manpass.emptyEntry.pack(padx=2, pady=2)
    else:
        widgedestroy(manpass.webLbl, manpass.webEntry, manpass.webBtn)
        #sets up SQL statement
        delcred = "DELETE FROM passwords WHERE userID = %s AND website = %s;"
        usracc = (user, website)
        exquery(credentialsdb,delcred,usracc)

def multiquery(credentialsdb,query1,query2,credentials):
    cursor = credentialsdb.cursor()
    try:
        cursor.execute(query2, credentials)
        cursor.execute(query1, credentials)
        credentialsdb.commit()
        print("query succesful")
        cursor.close()
    except Error as err:
        print(f"Error: {err}")

#query delete function for account - couldn't do a INNER JOIN statement, had to use two seperate statements
def delAccount(credentialsdb,unvar):
    user = unvar.get()
    user2 = [user]
    delacc1 = "DELETE FROM account WHERE userID = %s;"
    delacc2 = "DELETE FROM passwords WHERE userID = %s;"
    userid = (user2)
    multiquery(credentialsdb, delacc1, delacc2, userid)

#function for the generate password page
def newpassword():
    # hides the main menu
    mainMenu.pack_forget()
    # shows password page
    npFrame.pack()

    npFrame.npLabel = ttk.Label(npFrame, text="Click below to generate your new password!")
    npFrame.npLabel.pack(padx=10, pady=10)

    npFrame.superCoolButton = ttk.Button(npFrame, text="Press me", width=27, command= generateRanPassword)
    npFrame.superCoolButton.pack(padx=2, pady=2)

    npFrame.returnMM2 = ttk.Button(npFrame, text="Return to Main Menu",
                                   command= lambda:[mainmenu(),widgedestroy(npFrame.npLabel,
                                                                     npFrame.superCoolButton,
                                                                     npFrame.returnMM2)])
    npFrame.returnMM2.pack(padx=2, pady=2)

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
    global pvar
    global npLbl
    global npUse
    global npUse2

    if hasattr(npFrame, 'npLbl'):
        npFrame.npLbl.destroy()
    if hasattr(npFrame, 'npUse'):
        npFrame.npUse.destroy()
    if hasattr(npFrame, 'npUse2'):
        npFrame.npUse2.destroy()
    npFrame.npLbl = ttk.Label(npFrame, text="Your new password is " + pw)
    npFrame.npLbl.pack(side=TOP, pady=20)

    npFrame.npUse = ttk.Button(npFrame, text="Update Main Account", command= lambda: applyPassMain(credentialsdb,pvar,pw))
    npFrame.npUse.pack(side=TOP, pady = 10)

    npFrame.npUse2 = ttk.Button(npFrame, text="Update Secondary Profile")
    npFrame.npUse2.pack(side=TOP,pady=10)

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

#function for the log in frame
def welcomeFrame():
    global unvar
    if caframe:
        caframe.pack_forget()
    if mainmenu:
        mainMenu.pack_forget()
    if accsett:
        accsett.pack_forget()
    #shows log in frame
    welcome.pack()

    welcome.loginlbl = ttk.Label(welcome, text="Welcome to the Super Cool Password Manager")
    welcome.loginlbl.pack(side=TOP, padx=20, pady=20)

    welcome.usernamelbl = ttk.Label(welcome, text="Username")
    welcome.usernamelbl.pack(side=TOP, padx=2, pady=2)

    welcome.username = ttk.Entry(welcome, textvariable=unvar, width=30)
    welcome.username.pack(side=TOP, padx=2, pady=2)

    welcome.passwordlbl = ttk.Label(welcome, text="Password")
    welcome.passwordlbl.pack(side=TOP, padx=2, pady=2)

    welcome.password = ttk.Entry(welcome, show="*", textvariable=pvar, width=30)
    welcome.password.pack(side=TOP, padx=2, pady=2)

    welcome.loginbtn = ttk.Button(welcome, text="Log in",
                                  command= lambda: existcredentials(unvar, pvar, credentialsdb))
    welcome.loginbtn.pack(side=TOP, padx=5, pady=5)
    #binds the Enter key to the button
    PMWin.bind('<Return>', lambda event: welcome.loginbtn.invoke())

    welcome.nulbl = ttk.Label(welcome, text="New User?")
    welcome.nulbl.pack(side=TOP, padx=2, pady=2)

    welcome.nubtn = ttk.Button(welcome, text="Create an Account",
                               command=lambda: [createaccount(),
                                                widgedestroy(welcome.loginlbl,welcome.usernamelbl,
                                                             welcome.username,welcome.passwordlbl,
                                                             welcome.password,welcome.loginbtn,
                                                             welcome.nulbl,welcome.nubtn)])
    welcome.nubtn.pack(side=TOP, padx=2, pady=2)

    # clears the entry textbox after the information is submitted
    welcome.username.delete(0,END)
    welcome.password.delete(0,END)

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
