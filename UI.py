from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import random
import string

class UI:

    def __init__(self, window, connect):
        self.window = window
        self.connection = connect

        # set string variables for frame command use
        self.unvar = StringVar(master=self.window)
        self.pvar = StringVar(master=self.window)
        self.webVar = StringVar(master=self.window)
        self.usrVar = StringVar(master=self.window)
        self.emlVar = StringVar(master=self.window)
        self.pasVar = StringVar(master=self.window)
        self.newunVar = StringVar(master=self.window)
        self.newpVar = StringVar(master=self.window)
        self.aUVar = StringVar(master=self.window)
        self.aEVar = StringVar(master=self.window)
        self.aPVar = StringVar(master=self.window)

        self.window.geometry("500x400")
        self.window.title('Super Cool Password Manager')

        self.container = ttk.Frame(self.window)
        self.container.pack()

    # methods for the log in frame
    def welcome(self):

        if hasattr(self.container, 'inLbl'):
            self.container.inLbl.destroy()
        if hasattr(self.container, 'usredit'):
            self.container.usredit.destroy()
        if hasattr(self.container, 'psedit'):
            self.container.psedit.destroy()
        if hasattr(self.container, 'delacc'):
            self.container.delacc.destroy()
        if hasattr(self.container, 'returnmm'):
            self.container.returnmm.destroy()
        if hasattr(self.container, 'incPass'):
            self.container.incPass.destroy()
        if hasattr(self.container, 'noacc'):
            self.container.noacc.destroy()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()


        self.container.loginlbl = ttk.Label(self.container, text="Welcome to the Super Cool Password Manager")
        self.container.loginlbl.pack(side='top', padx=20, pady=20)

        self.container.usernamelbl = ttk.Label(self.container, text="Username")
        self.container.usernamelbl.pack(side='top', padx=2, pady=2)

        self.container.username = ttk.Entry(self.container, textvariable= self.unvar, width=30)
        self.container.username.pack(side='top', padx=2, pady=2)

        self.container.passwordlbl = ttk.Label(self.container, text="Password")
        self.container.passwordlbl.pack(side='top', padx=2, pady=2)

        self.container.password = ttk.Entry(self.container, show="*", textvariable= self.pvar, width=30)
        self.container.password.pack(side='top', padx=2, pady=2)

        self.container.loginbtn = ttk.Button(self.container, text="Log in",
                                      command=lambda: self.connection.exist_credentials(self.unvar, self.pvar))
        self.container.loginbtn.pack(side='top', padx=5, pady=5)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.loginbtn.invoke())

        self.container.nulbl = ttk.Label(self.container, text="New User?")
        self.container.nulbl.pack(side='top', padx=2, pady=2)

        self.container.nubtn = ttk.Button(self.container, text="Create an Account",
                                   command=lambda: [self.create_account(),
                                                    self.widget_destroy(self.container.loginlbl, self.container.usernamelbl,
                                                                 self.container.username, self.container.passwordlbl,
                                                                 self.container.password, self.container.loginbtn,
                                                                 self.container.nulbl, self.container.nubtn)])
        self.container.nubtn.pack(side='top', padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        self.container.username.delete(0, END)
        self.container.password.delete(0, END)

    def find_query_error(self):
        self.container.noAccLbl = ttk.Label(self.container, text="No accounts for this user...")
        self.container.noAccLbl.pack(padx=2, pady=2)

    def read_query_empty(self):
        self.container.emptyEntry = ttk.Label(self.container, text="Entry boxes cannot be empty!")
        self.container.emptyEntry.pack()

    def successful_login(self):
        self.main_menu()
        self.widget_destroy(self.container.loginlbl, self.container.usernamelbl,
                          self.container.username, self.container.passwordlbl,
                          self.container.password, self.container.loginbtn,
                          self.container.nulbl, self.container.nubtn)

    def incorrect_password(self):
        self.container.incPass = ttk.Label(self.container, text="Incorrect password!")
        self.container.incPass.pack()

    def account_not_found(self):
        self.container.noacc = ttk.Label(self.container, text="Account doesn't exist")
        self.container.noacc.pack()

#-----------------------------------------------------------------------------------------------------------------------

    def create_account(self):
        #removes empty space of welcome_frame frame widgets
        #welcome_frame.pack_forget()

        if hasattr(self.container, 'usrexists'):
            self.container.usrexists.destroy()
        if hasattr(self.container, 'pasexists'):
            self.container.pasexists.destroy()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.container.calbl = ttk.Label(self.container, text="New Account Credentials")
        self.container.calbl.pack(side='top', padx=20, pady=20)

        self.container.setunlbl = ttk.Label(self.container, text="Enter a username")
        self.container.setunlbl.pack(side=TOP, padx=2, pady=2)

        self.container.setun = ttk.Entry(self.container, textvariable= self.unvar, width=30)
        self.container.setun.pack(side=TOP, padx=2, pady=2)

        self.container.setpslbl = ttk.Label(self.container, text="Enter a password")
        self.container.setpslbl.pack(side=TOP, padx=2, pady=2)

        self.container.setps = ttk.Entry(self.container, show ="*", textvariable= self.pvar, width=30)
        self.container.setps.pack(side=TOP, padx=2, pady=2)

        self.container.cabtn = ttk.Button(self.container, text="Create Account",
                               command = lambda: self.connection.cred_check(self.unvar, self.pvar))
        self.container.cabtn.pack(side=TOP, padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        self.container.setun.delete(0,END)
        self.container.setps.delete(0,END)

        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.cabtn.invoke())

        self.container.returnLogin = ttk.Button(self.container, text="Return to the Login screen",
                                         command= lambda: [self.welcome(),
                                                           self.widget_destroy(
                                                               self.container.calbl,
                                                               self.container.setunlbl,
                                                               self.container.setun,
                                                               self.container.setpslbl,
                                                               self.container.setps,
                                                               self.container.cabtn,
                                                               self.container.returnLogin
                                                           )])
        self.container.returnLogin.pack(padx=20, pady=20)

    def user_exists_error(self):
        self.container.usrexists = ttk.Label(self.container, text="User already exists!")
        self.container.usrexists.pack()

    def password_unavailable(self):
        self.container.pasexists = ttk.Label(self.container, text="Password Unavailable")
        self.container.pasexists.pack()

    def successful_creation(self):
        self.main_menu()
        self.widget_destroy(self.container.calbl, self.container.setunlbl,
                     self.container.setun, self.container.setpslbl, self.container.setps,
                     self.container.cabtn, self.container.returnLogin)

#-----------------------------------------------------------------------------------------------------------------------

    def main_menu(self):
        if hasattr(self.container, 'calbl'):
            self.container.calbl.destroy()
        if hasattr(self.container, 'setunlbl'):
            self.container.setunlbl.destroy()
        if hasattr(self.container, 'setun'):
            self.container.setun.destroy()
        if hasattr(self.container, 'setpslbl'):
            self.container.setpslbl.destroy()
        if hasattr(self.container, 'setps'):
            self.container.setps.destroy()
        if hasattr(self.container, 'cabtn'):
            self.container.cabtn.destroy()
        if hasattr(self.container, 'returnLogin'):
            self.container.returnLogin.destroy()
        if hasattr(self.container, 'npLbl'):
            self.container.npLbl.destroy()
        if hasattr(self.container, 'npUse'):
            self.container.npUse.destroy()
        if hasattr(self.container, 'npUse2'):
            self.container.npUse2.destroy()

        self.container.welcome_frameMes = ttk.Label(self.container, text="Super Cool Main Menu")
        self.container.welcome_frameMes.pack(padx=20, pady=20)

        self.container.managePassButton = ttk.Button(self.container, text="Current Passwords",
                                               command=lambda: [self.manage_passwords(),
                                                                self.widget_destroy(
                                                                        self.container.welcome_frameMes,
                                                                              self.container.managePassButton,
                                                                              self.container.newPass,
                                                                              self.container.accsettings,
                                                                              self.container.signoutBtn
                                                                        )])
        self.container.managePassButton.pack(padx=5, pady=5)

        self.container.newPass = ttk.Button(self.container, text="Password Generator",
                                      command=lambda: [self.newpassword(), self.widget_destroy(
                                                                              self.container.welcome_frameMes,
                                                                                    self.container.managePassButton,
                                                                                    self.container.newPass,
                                                                                    self.container.accsettings,
                                                                                    self.container.signoutBtn
                                                                              )])
        self.container.newPass.pack(padx=5, pady=5)

        self.container.accsettings = ttk.Button(self.container, text="Account Settings",
                                          command=lambda: [self.account_settings(), self.widget_destroy(
                                                                                 self.container.welcome_frameMes,
                                                                                       self.container.managePassButton,
                                                                                       self.container.newPass,
                                                                                       self.container.accsettings,
                                                                                       self.container.signoutBtn
                                                                                 )])
        self.container.accsettings.pack(padx=5, pady=5)

        self.container.signoutBtn = ttk.Button(self.container, text="Sign Out",
                                         command=lambda: [self.welcome(), self.widget_destroy(
                                                                                 self.container.welcome_frameMes,
                                                                                       self.container.managePassButton,
                                                                                       self.container.newPass,
                                                                                       self.container.accsettings,
                                                                                       self.container.signoutBtn
                                                                                 )])
        self.container.signoutBtn.pack(padx=5, pady=5)


    # function for the manage password page
    def manage_passwords(self):
        #mainMenu.pack_forget()

        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.container.manlabel = ttk.Label(self.container, text="Here are your current passwords")
        self.container.manlabel.pack(padx=10, pady=10)

        self.container.table = ttk.Treeview(self.container, columns=("Website", "Email", "Username", "Password"), show="headings")

        self.container.table.heading("Website", text="Website")
        self.container.table.heading("Email", text="Email")
        self.container.table.heading("Username", text="Username")
        self.container.table.heading("Password", text="Password")

        self.container.table.column("Website", width=100)
        self.container.table.column("Email", width=100)
        self.container.table.column("Username", width=100)
        self.container.table.column("Password", width=100)

        # retrieves credentials and insert them into the table
        self.connection.findwebcredentials(self.unvar, self.container.table)
        self.container.table.pack(padx=2, pady=2)

        self.container.editbtn = ttk.Button(self.container, text="Edit an Account", command=lambda: self.webcredentry(self.container.table))
        self.container.editbtn.pack(padx=2, pady=2)

        self.container.addAccBtn = ttk.Button(self.container, text="Add a new Website Account", command=lambda: self.addWeb(self.container.table))
        self.container.addAccBtn.pack(padx=2, pady=2)

        self.container.deleteBtn = ttk.Button(self.container, text="Delete an Account", command=lambda: self.deleteCredbtn(self.container.table))
        self.container.deleteBtn.pack(padx=2, pady=2)

        self.container.returnMM1 = ttk.Button(self.container, text="Return to Main Menu",
                                       command=lambda: [self.main_menu(),
                                                        self.widget_destroy(self.container.manlabel,
                                                                                 self.container.table,
                                                                                 self.container.editbtn,
                                                                                 self.container.addAccBtn,
                                                                                 self.container.deleteBtn,
                                                                                 self.container.returnMM1
                                                                        )])
        self.container.returnMM1.pack(pady=2)

    def manager_widget_destroy(self):
        self.widget_destroy(
                      self.container.webLbl,
                            self.container.webEntry,
                            self.container.webBtn,
                            self.container.cancelBtn
                      )

    def account_settings(self):
        #mainMenu.pack_forget()

        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.container.inLbl = ttk.Label(self.container, text="Account Settings")
        self.container.inLbl.pack(pady=20)

        self.container.usredit = ttk.Button(self.container, text="Change Username", command=lambda: self.change_username(self.unvar))
        self.container.usredit.pack(pady=5)

        self.container.psedit = ttk.Button(self.container, text="Change Password", command=lambda: self.change_password(self.pvar))
        self.container.psedit.pack(pady=5)

        self.container.delacc = ttk.Button(self.container, text="Delete Account", command=lambda: self.warning_message(self.unvar))
        self.container.delacc.pack(pady=5)

        self.container.returnmm = ttk.Button(self.container, text="Return to the Main Menu",
                                      command=lambda: [self.main_menu(),
                                                       self.widget_destroy(
                                                              self.container.inLbl,
                                                                    self.container.usredit,
                                                                    self.container.psedit,
                                                                    self.container.delacc,
                                                                    self.container.returnmm
                                                              )])
        self.container.returnmm.pack(pady=10)

    def account_settings_widget_destroy(self):
        self.widget_destroy(
                         self.container.newpassLbl,
                         self.container.newpassEntry,
                         self.container.newpassBtn
                    )

    def change_username(self, unvar):
        self.container.newusrnameLbl = ttk.Label(self.container, text="Enter your new username:")
        self.container.newusrnameLbl.pack(padx=2, pady=2)
        self.container.newusrnameEntry = ttk.Entry(self.container, textvariable= self.newunVar, width=30)
        self.container.newusrnameEntry.pack(padx=2, pady=2)
        self.container.newusrnameBtn = ttk.Button(self.container, text="Submit",
                                           command=lambda: [self.cngUser(self.unvar, self.newunVar),
                                                            self.widget_destroy(self.container.newusrnameLbl, self.container.newusrnameEntry,
                                                                         self.container.newusrnameBtn, self.container.cancelBtn)])
        self.container.newusrnameBtn.pack(padx=2, pady=2)
        self.container.cancelBtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda:
                                       self.widget_destroy(self.container.newusrnameLbl,
                                                    self.container.newusrnameEntry,
                                                    self.container.newusrnameBtn,
                                                    self.container.cancelBtn))
        self.container.cancelBtn.pack(padx=2, pady=2)
        # clears the entry textbox after the information is submitted
        self.container.newusrnameEntry.delete(0, END)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.newusrnameBtn.invoke())

    def change_password(self, pvar):
        self.container.newpassLbl = ttk.Label(self.container, text="Enter your new password:")
        self.container.newpassLbl.pack(padx=2, pady=2)
        self.container.newpassEntry = ttk.Entry(self.container, textvariable= self.newpVar, width=30)
        self.container.newpassEntry.pack(padx=2, pady=2)
        self.container.newpassBtn = ttk.Button(self.container, text="Submit",
                                        command=lambda: [self.connection.cngPass(self.pvar, self.newpVar),
                                                         self.widget_destroy(self.container.newpassLbl, self.container.newpassEntry,
                                                                      self.container.cancelBtn)])
        self.container.newpassBtn.pack(padx=2, pady=2)
        self.container.cancelBtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda:
                                       self.widget_destroy(self.container.newpassLbl,
                                                    self.container.newpassEntry,
                                                    self.container.newpassBtn,
                                                    self.container.cancelBtn))
        self.container.cancelBtn.pack(padx=2, pady=2)
        # clears the entry textbox after the information is submitted
        self.container.newpassEntry.delete(0, END)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.newpassBtn.invoke())

    def cngUser(self, unvar, newunVar):
        user = unvar.get()
        newuser = newunVar.get()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()
        if newuser == "":
            self.container.emptyEntry = ttk.Label(self.container, text="Entry boxes cannot be empty!")
            self.container.emptyEntry.pack()
        else:
            self.widget_destroy(self.container.newusrnameLbl,
                         self.container.newusrnameEntry,
                         self.container.newusrnameBtn)
            cngusr = "UPDATE account SET userID = %s WHERE userID = %s;"
            acc = (newuser, user)
            self.connection.execute_query(cngusr, acc)

    def warning_message(self, unvar):
        choice = messagebox.askyesno("Delete Account", "Are you sure?")
        if choice:
            # probably a password verification will be implemented here
            self.connection.delete_account(unvar)
            self.welcome()
        else:
            print("will change soon")

    def widget_destroy(self, *args):
        for widget in args:
            widget.destroy()

    def editUser(self, webVar, table):
        self.container.userEnt = ttk.Entry(self.container, textvariable=self.aUVar)
        self.container.userEnt.pack()
        self.container.edsubmit = ttk.Button(self.container, text="Submit",
                                      command=lambda: [self.connection.eUSub(self.aUVar, self.webVar, table),
                                                       self.widget_destroy(self.container.userEnt,
                                                                    self.container.edsubmit)])
        self.container.edsubmit.pack(pady=2)
        self.container.userEnt.delete(0, END)
        self.window.bind('<Return>', lambda event: self.container.edsubmit.invoke())

    def edit_email(self, table):
        self.container.emaillbl = ttk.Label(self.container, text="Enter a new email:")
        self.container.emaillbl.pack()
        self.container.emailEnt = ttk.Entry(self.container, textvariable= self.aEVar)
        self.container.emailEnt.pack()
        self.container.edsubmit = ttk.Button(self.container, text="Submit",
                                      command=lambda: [self.connection.eESub(self.aEVar, self.webVar, self.unvar, table),
                                                       self.widget_destroy(self.container.emaillbl,
                                                       self.container.emailEnt, self.container.edsubmit)])
        self.container.edsubmit.pack(pady=2)
        self.container.emailEnt.delete(0, END)
        self.window.bind('<Return>', lambda event: self.container.edsubmit.invoke())

    def specificweb(self, table):
        self.container.edemail = ttk.Button(self.container, text="Change Email", command=lambda: self.edit_email(self.webVar, table))
        self.container.edemail.pack(pady=2)
        self.container.edusr = ttk.Button(self.container, text="Change Username", command=lambda: self.editUser(self.webVar, table))
        self.container.edusr.pack(pady=2)
        self.container.edpass = ttk.Button(self.container, text="Change Password", command=lambda: self.editPass(self.webVar, table))
        self.container.edpass.pack(pady=2)
        self.container.edcancel = ttk.Button(self.container, text="Close",
                                      command=lambda: self.widget_destroy(self.container.edusr, self.container.edemail,
                                                                   self.container.edpass, self.container.edcancel))
        self.container.edcancel.pack(pady=2)

    def webcredentry(self, table):
        self.container.editlbl = ttk.Label(self.container, text="Enter the website you would like to edit:")
        self.container.editlbl.pack()
        self.container.editentry = ttk.Entry(self.container, textvariable= self.webVar, width=30)
        self.container.editentry.pack()
        self.container.editbtn = ttk.Button(self.container, text="Submit",
                                     command=lambda: [self.specificweb(self.webVar, table),
                                                      self.widget_destroy(self.container.editlbl,
                                                                   self.container.editentry,
                                                                   self.container.editbtn,
                                                                   self.container.cancelbtn)])
        self.container.editbtn.pack()
        self.container.cancelbtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda: self.widget_destroy(self.container.editlbl,
                                                                    self.container.editentry,
                                                                    self.container.editbtn,
                                                                    self.container.cancelbtn))
        self.container.cancelbtn.pack()

        # clears entry box
        self.container.editentry.delete(0, END)
        # binds enter key to button
        self.window.bind('<Return>', lambda event: self.container.editbtn.invoke())

    def addWeb(self, table):
        global unvar
        self.container.weblbl = ttk.Label(self.container, text="Enter the website:")
        self.container.weblbl.pack(padx=2, pady=2)
        self.container.webentry = ttk.Entry(self.container, textvariable= self.webVar, width=30)
        self.container.webentry.pack(padx=2, pady=2)

        self.container.usrlbl = ttk.Label(self.container, text="Enter the username:")
        self.container.usrlbl.pack(padx=2, pady=2)
        self.container.usrentry = ttk.Entry(self.container, textvariable= self.usrVar, width=30)
        self.container.usrentry.pack(padx=2, pady=2)

        self.container.emllbl = ttk.Label(self.container, text="Enter the email:")
        self.container.emllbl.pack(padx=2, pady=2)
        self.container.emlentry = ttk.Entry(self.container, textvariable= self.emlVar, width=30)
        self.container.emlentry.pack(padx=2, pady=2)

        self.container.paslbl = ttk.Label(self.container, text="Enter the password:")
        self.container.paslbl.pack(padx=2, pady=2)
        self.container.pasentry = ttk.Entry(self.container, textvariable= self.pasVar, width=30)
        self.container.pasentry.pack(padx=2, pady=2)

        self.container.submitBtn = ttk.Button(self.container, text="Submit",
                                       command=lambda: self.webCredentials(self.unvar, self.webVar, self.usrVar, self.emlVar, self.pasVar, table))
        self.container.submitBtn.pack(padx=2, pady=2)

        self.container.cancelBtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda: self.widget_destroy(self.container.weblbl,
                                                                    self.container.webentry, self.container.usrlbl,
                                                                    self.container.usrentry, self.container.emllbl,
                                                                    self.container.emlentry, self.container.paslbl,
                                                                    self.container.pasentry, self.container.submitBtn,
                                                                    self.container.cancelBtn))
        self.container.cancelBtn.pack(padx=2, pady=2)

        # clears the entry textbox after the information is submitted
        self.container.webentry.delete(0, END)
        self.container.usrentry.delete(0, END)
        self.container.emlentry.delete(0, END)
        self.container.pasentry.delete(0, END)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.submitBtn.invoke())

    # function for the generate password page
    def newpassword(self):
        # hides the main menu
        #mainMenu.pack_forget()

        self.container.npLabel = ttk.Label(self.container, text="Click below to generate your new password!")
        self.container.npLabel.pack(padx=10, pady=10)

        self.container.superCoolButton = ttk.Button(self.container, text="Press me", width=27, command= self.generateRanPassword)
        self.container.superCoolButton.pack(padx=2, pady=2)

        self.container.returnMM2 = ttk.Button(self.container, text="Return to Main Menu",
                                       command=lambda: [self.main_menu(), self.widget_destroy(self.container.npLabel,
                                                                                 self.container.superCoolButton,
                                                                                 self.container.returnMM2)])
        self.container.returnMM2.pack(padx=2, pady=2)

    def new_password_widget_destroy(self):
        self.container.widget_destroy(
                     self.container.npLbl,
                     self.container.npUse
            )

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

        if hasattr(self.container, 'npLbl'):
            self.container.npLbl.destroy()
        if hasattr(self.container, 'npUse'):
            self.container.npUse.destroy()
        if hasattr(self.container, 'npUse2'):
            self.container.npUse2.destroy()

        self.container.npLbl = ttk.Label(self.container, text="Your new password is " + pw)
        self.container.npLbl.pack(side=TOP, pady=20)

        self.container.npUse = ttk.Button(self.container, text="Update Main Account",
                                   command=lambda: self.connection.applyPassMain(pvar, pw))
        self.container.npUse.pack(side=TOP, pady=10)

        self.container.npUse2 = ttk.Button(self.container, text="Update Secondary Profile")
        self.container.npUse2.pack(side=TOP, pady=10)

    def editPass(self, webVar, table):
        self.container.passEnt = ttk.Entry(self.container, textvariable= self.aPVar)
        self.container.passEnt.pack()
        self.container.edsubmit = ttk.Button(self.container, text="Submit",
                                      command=lambda: [self.connection.ePSub(self.aPVar, self.webVar, table),
                                                       self.widget_destroy(self.container.passEnt, self.container.edsubmit)])
        self.container.edsubmit.pack(pady=2)
        self.container.passEnt.delete(0, END)
        self.window.bind('<Return>', lambda event: self.container.edsubmit.invoke())

    def webCredentials(self, unvar, webVar, usrVar, emlVar, pasVar, table):
        userID = unvar.get()
        website = webVar.get()
        username = usrVar.get()
        email = emlVar.get()
        password = pasVar.get()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()
        if website == "" or username == "" or email == "" or password == "":
            self.container.emptyEntry = ttk.Label(self.container, text="Entry boxes cannot be empty!")
            self.container.emptyEntry.pack(padx=2, pady=2)
        else:
            self.widget_destroy(self.container.weblbl, self.container.webentry,
                         self.container.usrlbl, self.container.usrentry,
                         self.container.emllbl, self.container.emlentry,
                         self.container.paslbl, self.container.pasentry,
                         self.container.submitBtn, self.container.cancelBtn)
            pasAcc = "INSERT INTO passwords (userID, website, email, username, password2) VALUES (%s, %s, %s, %s, %s);"
            credentials = (userID, website, email, username, password)
            self.connection.execute_query(pasAcc, credentials)

            self.container.table.insert("", "end", values=(website, email, username, password))

    def deleteCredbtn(self, table):
        # user prompt
        self.container.webLbl = ttk.Label(self.container, text="Enter the website credentials you would like to delete:")
        self.container.webLbl.pack(padx=2, pady=2)
        self.container.webEntry = ttk.Entry(self.container, textvariable= self.webVar, width=30)
        self.container.webEntry.pack(padx=2, pady=2)
        self.container.webBtn = ttk.Button(self.container, text="Submit",
                                    command=lambda: self.connection.delCredentials(self.unvar, self.webVar, table))
        self.container.webBtn.pack(padx=2, pady=2)
        self.container.cancelBtn = ttk.Button(self.container, text="cancel",
                                       command=lambda: self.widget_destroy(self.container.webLbl,
                                                                    self.container.webEntry,
                                                                    self.container.webBtn,
                                                                    self.container.cancelBtn))
        self.container.cancelBtn.pack()
        self.container.webEntry.delete(0, END)
        self.window.bind('<Return>', lambda event: self.container.webBtn.invoke())