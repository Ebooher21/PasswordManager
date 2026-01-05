from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from Connect import *
import random
import string

class UI:

    def __init__(self, connect):
        self.window = Tk()
        self.connect = connect

        self.frames = {}

        self.setup()
        self.welcome()


    def setup(self):
        self.window.geometry("500x400")
        self.window.title('Super Cool Password Manager')

        container = ttk.Frame(self.window)
        container.pack()

        welcome_frame = ttk.Frame(container)
        create_account_frame = ttk.Frame(container)
        mainMenu = ttk.Frame(container)
        manpass = ttk.Frame(container)


    # function for the log in frame
    def welcome(self):
        global unvar

        if create_account_frame:
            create_account_frame.pack_forget()
        if mainmenu:
            mainMenu.pack_forget()
        if accsett:
            accsett.pack_forget()

        welcome_frame.loginlbl = ttk.Label(welcome_frame, text="welcome_frame to the Super Cool Password Manager")
        welcome_frame.loginlbl.pack(side='top', padx=20, pady=20)

        welcome_frame.usernamelbl = ttk.Label(welcome_frame, text="Username")
        welcome_frame.usernamelbl.pack(side='top', padx=2, pady=2)

        welcome_frame.username = ttk.Entry(welcome_frame, textvariable=unvar, width=30)
        welcome_frame.username.pack(side='top', padx=2, pady=2)

        welcome_frame.passwordlbl = ttk.Label(welcome_frame, text="Password")
        welcome_frame.passwordlbl.pack(side='top', padx=2, pady=2)

        welcome_frame.password = ttk.Entry(welcome_frame, show="*", textvariable=pvar, width=30)
        welcome_frame.password.pack(side='top', padx=2, pady=2)

        welcome_frame.loginbtn = ttk.Button(welcome_frame, text="Log in",
                                      command=lambda: self.connect.existcredentials(unvar, pvar))
        welcome_frame.loginbtn.pack(side='top', padx=5, pady=5)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: welcome_frame.loginbtn.invoke())

        welcome_frame.nulbl = ttk.Label(welcome_frame, text="New User?")
        welcome_frame.nulbl.pack(side='top', padx=2, pady=2)

        welcome_frame.nubtn = ttk.Button(welcome_frame, text="Create an Account",
                                   command=lambda: [createaccount(),
                                                    widgedestroy(welcome_frame.loginlbl, welcome_frame.usernamelbl,
                                                                 welcome_frame.username, welcome_frame.passwordlbl,
                                                                 welcome_frame.password, welcome_frame.loginbtn,
                                                                 welcome_frame.nulbl, welcome_frame.nubtn)])
        welcome_frame.nubtn.pack(side='top', padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        welcome_frame.username.delete(0, END)
        welcome_frame.password.delete(0, END)

    def createaccount(self):
        #removes empty space of welcome_frame frame widgets
        welcome_frame.pack_forget()

        if hasattr(create_account_frame, 'usrexists'):
            create_account_frame.usrexists.destroy()
        if hasattr(create_account_frame, 'pasexists'):
            create_account_frame.pasexists.destroy()
        if hasattr(create_account_frame, 'emptyEntry'):
            create_account_frame.emptyEntry.destroy()

        create_account_frame.pack()

        create_account_frame.calbl = ttk.Label(create_account_frame, text="New Account Credentials")
        create_account_frame.calbl.pack(side='top', padx=20, pady=20)

        create_account_frame.setunlbl = ttk.Label(create_account_frame, text="Enter a username")
        create_account_frame.setunlbl.pack(side=TOP, padx=2, pady=2)

        create_account_frame.setun = ttk.Entry(create_account_frame, textvariable=unvar, width=30)
        create_account_frame.setun.pack(side=TOP, padx=2, pady=2)

        create_account_frame.setpslbl = ttk.Label(create_account_frame, text="Enter a password")
        create_account_frame.setpslbl.pack(side=TOP, padx=2, pady=2)

        create_account_frame.setps = ttk.Entry(create_account_frame, show ="*", textvariable=pvar, width=30)
        create_account_frame.setps.pack(side=TOP, padx=2, pady=2)

        create_account_frame.cabtn = ttk.Button(create_account_frame, text="Create Account",
                               command = lambda: credcheck(unvar,pvar))
        create_account_frame.cabtn.pack(side=TOP, padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        create_account_frame.setun.delete(0,END)
        create_account_frame.setps.delete(0,END)

        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: create_account_frame.cabtn.invoke())

        create_account_frame.returnLogin = ttk.Button(create_account_frame, text="Return to the Login screen",
                                         command= lambda: [welcome_frameFrame(),
                                                           widgedestroy(create_account_frame.calbl,create_account_frame.setunlbl,
                                                               create_account_frame.setun,create_account_frame.setpslbl,create_account_frame.setps,
                                                               create_account_frame.cabtn,create_account_frame.returnLogin)])
        create_account_frame.returnLogin.pack(padx=20, pady=20)


    def mainmenu(self):

        if create_account_frame:
            create_account_frame.pack_forget()
        if welcome_frame:
            welcome_frame.pack_forget()
        if npFrame:
            npFrame.pack_forget()
        if manpass:
            manpass.pack_forget()
        if accsett:
            accsett.pack_forget()

        mainMenu.welcome_frameMes = ttk.Label(mainMenu, text="Super Cool Main Menu")
        mainMenu.welcome_frameMes.pack(padx=20, pady=20)

        mainMenu.managePassButton = ttk.Button(mainMenu, text="Current Passwords",
                                               command=lambda: [managepassword(), widgedestroy(mainMenu.welcome_frameMes,
                                                                                               mainMenu.managePassButton,
                                                                                               mainMenu.newPass,
                                                                                               mainMenu.accsettings,
                                                                                               mainMenu.signoutBtn)])
        mainMenu.managePassButton.pack(padx=5, pady=5)

        mainMenu.newPass = ttk.Button(mainMenu, text="Password Generator",
                                      command=lambda: [newpassword(), widgedestroy(mainMenu.welcome_frameMes,
                                                                                   mainMenu.managePassButton,
                                                                                   mainMenu.newPass,
                                                                                   mainMenu.accsettings,
                                                                                   mainMenu.signoutBtn)])
        mainMenu.newPass.pack(padx=5, pady=5)

        mainMenu.accsettings = ttk.Button(mainMenu, text="Account Settings",
                                          command=lambda: [accountsett(), widgedestroy(mainMenu.welcome_frameMes,
                                                                                       mainMenu.managePassButton,
                                                                                       mainMenu.newPass,
                                                                                       mainMenu.accsettings,
                                                                                       mainMenu.signoutBtn)])
        mainMenu.accsettings.pack(padx=5, pady=5)

        mainMenu.signoutBtn = ttk.Button(mainMenu, text="Sign Out",
                                         command=lambda: [welcome_frameFrame(), widgedestroy(mainMenu.welcome_frameMes,
                                                                                       mainMenu.managePassButton,
                                                                                       mainMenu.newPass,
                                                                                       mainMenu.accsettings,
                                                                                       mainMenu.signoutBtn)])
        mainMenu.signoutBtn.pack(padx=5, pady=5)


    # function for the manage password page
    def managepassword(self):
        mainMenu.pack_forget()

        manpass.manlabel = ttk.Label(manpass, text="Here are your current passwords")
        manpass.manlabel.pack(padx=10, pady=10)

        manpass.table = ttk.Treeview(manpass, columns=("Website", "Email", "Username", "Password"), show="headings")
        manpass.table.heading("Website", text="Website")
        manpass.table.heading("Email", text="Email")
        manpass.table.heading("Username", text="Username")
        manpass.table.heading("Password", text="Password")
        manpass.table.column("Website", width=100)
        manpass.table.column("Email", width=100)
        manpass.table.column("Username", width=100)
        manpass.table.column("Password", width=100)
        # retrieves credentials and insert them into the table
        findwebcredentials(credentialsdb, unvar, manpass.table)
        manpass.table.pack(padx=2, pady=2)

        manpass.editbtn = ttk.Button(manpass, text="Edit an Account", command=lambda: webcredentry(manpass.table))
        manpass.editbtn.pack(padx=2, pady=2)

        manpass.addAccBtn = ttk.Button(manpass, text="Add a new Website Account", command=lambda: addWeb(manpass.table))
        manpass.addAccBtn.pack(padx=2, pady=2)

        manpass.deleteBtn = ttk.Button(manpass, text="Delete an Account", command=lambda: deleteCredbtn(manpass.table))
        manpass.deleteBtn.pack(padx=2, pady=2)

        manpass.returnMM1 = ttk.Button(manpass, text="Return to Main Menu",
                                       command=lambda: [mainmenu(), widgedestroy(manpass.manlabel,
                                                                                 manpass.table,
                                                                                 manpass.editbtn,
                                                                                 manpass.addAccBtn,
                                                                                 manpass.deleteBtn,
                                                                                 manpass.returnMM1)])
        manpass.returnMM1.pack(pady=2)


    def accountsett(self):
        mainMenu.pack_forget()
        accsett.pack()

        global unvar
        global pvar
        accsett.inLbl = ttk.Label(accsett, text="Account Settings")
        accsett.inLbl.pack(pady=20)

        accsett.usredit = ttk.Button(accsett, text="Change Username", command=lambda: cngUserEntry(unvar))
        accsett.usredit.pack(pady=5)

        accsett.psedit = ttk.Button(accsett, text="Change Password", command=lambda: cngPassEntry(pvar))
        accsett.psedit.pack(pady=5)

        accsett.delacc = ttk.Button(accsett, text="Delete Account", command=lambda: warningmess(unvar))
        accsett.delacc.pack(pady=5)

        accsett.returnmm = ttk.Button(accsett, text="Return to the Main Menu",
                                      command=lambda: [mainmenu(),
                                                       widgedestroy(accsett.inLbl, accsett.usredit,
                                                                    accsett.psedit, accsett.delacc,
                                                                    accsett.returnmm)])
        accsett.returnmm.pack(pady=10)

    def cngUserEntry(self, unvar):
        accsett.newusrnameLbl = ttk.Label(accsett, text="Enter your new username:")
        accsett.newusrnameLbl.pack(padx=2, pady=2)
        accsett.newusrnameEntry = ttk.Entry(accsett, textvariable=newunVar, width=30)
        accsett.newusrnameEntry.pack(padx=2, pady=2)
        accsett.newusrnameBtn = ttk.Button(accsett, text="Submit",
                                           command=lambda: [cngUser(unvar, newunVar),
                                                            widgedestroy(accsett.newusrnameLbl, accsett.newusrnameEntry,
                                                                         accsett.newusrnameBtn, accsett.cancelBtn)])
        accsett.newusrnameBtn.pack(padx=2, pady=2)
        accsett.cancelBtn = ttk.Button(accsett, text="Cancel",
                                       command=lambda:
                                       widgedestroy(accsett.newusrnameLbl,
                                                    accsett.newusrnameEntry,
                                                    accsett.newusrnameBtn,
                                                    accsett.cancelBtn))
        accsett.cancelBtn.pack(padx=2, pady=2)
        # clears the entry textbox after the information is submitted
        accsett.newusrnameEntry.delete(0, END)
        # binds the Enter key to the button
        PMWin.bind('<Return>', lambda event: accsett.newusrnameBtn.invoke())

    def cngPassEntry(self, pvar):
        accsett.newpassLbl = ttk.Label(accsett, text="Enter your new password:")
        accsett.newpassLbl.pack(padx=2, pady=2)
        accsett.newpassEntry = ttk.Entry(accsett, textvariable=newpVar, width=30)
        accsett.newpassEntry.pack(padx=2, pady=2)
        accsett.newpassBtn = ttk.Button(accsett, text="Submit",
                                        command=lambda: [cngPass(pvar, newpVar),
                                                         widgedestroy(accsett.newpassLbl, accsett.newpassEntry,
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
        accsett.newpassEntry.delete(0, END)
        # binds the Enter key to the button
        PMWin.bind('<Return>', lambda event: accsett.newpassBtn.invoke())

    def cngUser(self, unvar, newunVar):
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
            exquery(cngusr, acc)

    def warningmess(self, unvar):
        choice = messagebox.askyesno("Delete Account", "Are you sure?")
        if choice:
            # probably a password verification will be implemented here
            delAccount(unvar)
            welcome_frameFrame()
        else:
            print("will change soon")

    def widgedestroy(*args):
        for widget in args:
            widget.destroy()

    def editUser(self, webVar, table):
        manpass.userEnt = ttk.Entry(manpass, textvariable=aUVar)
        manpass.userEnt.pack()
        manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                      command=lambda: [eUSub(aUVar, webVar, table),
                                                       widgedestroy(manpass.userEnt,
                                                                    manpass.edsubmit)])
        manpass.edsubmit.pack(pady=2)
        manpass.userEnt.delete(0, END)
        PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

        def editEmail(webVar, table):
            manpass.emaillbl = ttk.Label(manpass, text="Enter a new email:")
            manpass.emaillbl.pack()
            manpass.emailEnt = ttk.Entry(manpass, textvariable=aEVar)
            manpass.emailEnt.pack()
            manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                          command=lambda: [eESub(aEVar, webVar, table),
                                                           widgedestroy(manpass.emaillbl, manpass.emailEnt,
                                                                        manpass.edsubmit)])
            manpass.edsubmit.pack(pady=2)
            manpass.emailEnt.delete(0, END)
            PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

    def specificweb(self, webVar, table):
        manpass.edemail = ttk.Button(manpass, text="Change Email", command=lambda: editEmail(webVar, table))
        manpass.edemail.pack(pady=2)
        manpass.edusr = ttk.Button(manpass, text="Change Username", command=lambda: editUser(webVar, table))
        manpass.edusr.pack(pady=2)
        manpass.edpass = ttk.Button(manpass, text="Change Password", command=lambda: editPass(webVar, table))
        manpass.edpass.pack(pady=2)
        manpass.edcancel = ttk.Button(manpass, text="Close",
                                      command=lambda: widgedestroy(manpass.edusr, manpass.edemail,
                                                                   manpass.edpass, manpass.edcancel))
        manpass.edcancel.pack(pady=2)

    def webcredentry(self, table):
        manpass.editlbl = ttk.Label(manpass, text="Enter the website you would like to edit:")
        manpass.editlbl.pack()
        manpass.editentry = ttk.Entry(manpass, textvariable=webVar, width=30)
        manpass.editentry.pack()
        manpass.editbtn = ttk.Button(manpass, text="Submit",
                                     command=lambda: [specificweb(webVar, table),
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

        # clears entry box
        manpass.editentry.delete(0, END)
        # binds enter key to button
        PMWin.bind('<Return>', lambda event: manpass.editbtn.invoke())

    def addWeb(self, table):
        global unvar
        manpass.weblbl = ttk.Label(manpass, text="Enter the website:")
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
                                       command=lambda: webCredentials(unvar, webVar, usrVar, emlVar, pasVar, table))
        manpass.submitBtn.pack(padx=2, pady=2)

        manpass.cancelBtn = ttk.Button(manpass, text="Cancel",
                                       command=lambda: widgedestroy(manpass.weblbl,
                                                                    manpass.webentry, manpass.usrlbl,
                                                                    manpass.usrentry, manpass.emllbl,
                                                                    manpass.emlentry, manpass.paslbl,
                                                                    manpass.pasentry, manpass.submitBtn,
                                                                    manpass.cancelBtn))
        manpass.cancelBtn.pack(padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        manpass.webentry.delete(0, END)
        manpass.usrentry.delete(0, END)
        manpass.emlentry.delete(0, END)
        manpass.pasentry.delete(0, END)
        # binds the Enter key to the button
        PMWin.bind('<Return>', lambda event: manpass.submitBtn.invoke())

    # function for the generate password page
    def newpassword(self):
        # hides the main menu
        mainMenu.pack_forget()

        # password generator frame
        npFrame = ttk.Frame(self.window)
        npFrame.pack()

        npFrame.npLabel = ttk.Label(npFrame, text="Click below to generate your new password!")
        npFrame.npLabel.pack(padx=10, pady=10)

        npFrame.superCoolButton = ttk.Button(npFrame, text="Press me", width=27, command= generateRanPassword)
        npFrame.superCoolButton.pack(padx=2, pady=2)

        npFrame.returnMM2 = ttk.Button(npFrame, text="Return to Main Menu",
                                       command=lambda: [mainmenu(), widgedestroy(npFrame.npLabel,
                                                                                 npFrame.superCoolButton,
                                                                                 npFrame.returnMM2)])
        npFrame.returnMM2.pack(padx=2, pady=2)

    # function for the password generator
    def generateRanPassword(self):
        # set password to empty string
        pw = ""
        # loop that chooses random characters for the password
        while len(pw) < 18:
            digit = random.randint(0, 9)
            Uletter = random.choice(string.ascii_uppercase)
            Lletter = random.choice(string.ascii_lowercase)
            RCharacter = random.choice("!@#$%&*?")
            PUse = [str(digit), Uletter, Lletter, RCharacter]
            pw += random.choice(PUse)

        # replaces label when returned to frame or when a new password is generated
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

        npFrame.npUse = ttk.Button(npFrame, text="Update Main Account",
                                   command=lambda: applyPassMain(credentialsdb, pvar, pw))
        npFrame.npUse.pack(side=TOP, pady=10)

        npFrame.npUse2 = ttk.Button(npFrame, text="Update Secondary Profile")
        npFrame.npUse2.pack(side=TOP, pady=10)

    def editPass(webVar, table):
        manpass.passEnt = ttk.Entry(manpass, textvariable= aPVar)
        manpass.passEnt.pack()
        manpass.edsubmit = ttk.Button(manpass, text="Submit",
                                      command=lambda: [ePSub(aPVar, webVar, table),
                                                       widgedestroy(manpass.passEnt, manpass.edsubmit)])
        manpass.edsubmit.pack(pady=2)
        manpass.passEnt.delete(0, END)
        PMWin.bind('<Return>', lambda event: manpass.edsubmit.invoke())

    def webCredentials(self, unvar, webVar, usrVar, emlVar, pasVar, table):
        userID = unvar.get()
        website = webVar.get()
        username = usrVar.get()
        email = emlVar.get()
        password = pasVar.get()
        if hasattr(manpass, 'emptyEntry'):
            manpass.emptyEntry.destroy()
        if website == "" or username == "" or email == "" or password == "":
            manpass.emptyEntry = ttk.Label(manpass, text="Entry boxes cannot be empty!")
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

            manpass.table.insert("", "end", values=(website, email, username, password))

    def deleteCredbtn(self, table):
        global unvar
        # user prompt
        manpass.webLbl = ttk.Label(manpass, text="Enter the website credentials you would like to delete:")
        manpass.webLbl.pack(padx=2, pady=2)
        manpass.webEntry = ttk.Entry(manpass, textvariable=webVar, width=30)
        manpass.webEntry.pack(padx=2, pady=2)
        manpass.webBtn = ttk.Button(manpass, text="Submit",
                                    command=lambda: delCredentials(credentialsdb, unvar, webVar, table))
        manpass.webBtn.pack(padx=2, pady=2)
        manpass.cancelBtn = ttk.Button(manpass, text="cancel",
                                       command=lambda: widgedestroy(manpass.webLbl,
                                                                    manpass.webEntry,
                                                                    manpass.webBtn,
                                                                    manpass.cancelBtn))
        manpass.cancelBtn.pack()
        manpass.webEntry.delete(0, END)
        PMWin.bind('<Return>', lambda event: manpass.webBtn.invoke())