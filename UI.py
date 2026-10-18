from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
import random
import string
import tkinter

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
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.grid(sticky=NSEW)

        self.container.margin = ttk.Frame(self.container)
        self.container.margin.grid(row=0, column=0, sticky="nsew")

        self.container.margin.columnconfigure(0, weight=1)
        self.container.margin.columnconfigure(1, weight=2)
        self.container.margin.columnconfigure(2, weight=1)

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

        self.container.margin = ttk.Frame(self.container)
        self.container.margin.grid(row=0,column=0, sticky="nsew")

        self.container.margin.columnconfigure(0,weight=1)
        self.container.margin.columnconfigure(1,weight=2)
        self.container.margin.columnconfigure(2,weight=1)

        self.container.margin.loginlbl = ttk.Label(self.container.margin, text="Welcome to the Super Cool Password Manager")
        self.container.margin.loginlbl.grid(column=1, row=0, sticky=N, padx=0, pady=20)

        self.container.margin.usernamelbl = ttk.Label(self.container.margin, text="Username")
        self.container.margin.usernamelbl.grid(column=1, row=1, sticky=NS, padx=2, pady=(10,2))

        self.container.margin.username = ttk.Entry(self.container.margin, textvariable=self.unvar)
        self.container.margin.username.grid(column=1, row=2, sticky=NSEW, padx=200, pady=(6,15))

        self.container.margin.passwordlbl = ttk.Label(self.container.margin, text="Password")
        self.container.margin.passwordlbl.grid(column=1, row=35, sticky=NS, padx=2, pady=(10,2))

        self.container.margin.password = ttk.Entry(self.container.margin, show="*", textvariable=self.pvar)
        self.container.margin.password.grid(column=1, row=45, sticky=NSEW, padx=200, pady=(6,15))

        self.container.margin.loginbtn = ttk.Button(self.container.margin, text="Log in",
                                             command=lambda: self.connection.exist_credentials(self.unvar, self.pvar))
        self.container.margin.loginbtn.grid(column=1, row=65, sticky=NSEW, padx=200, pady=20)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: self.container.margin.loginbtn.invoke())

        self.container.margin.nulbl = ttk.Label(self.container.margin, text="New User?")
        self.container.margin.nulbl.grid(column=1, row=100, sticky=NS, padx=2, pady=(20,2))

        self.container.margin.nubtn = ttk.Button(self.container.margin, text="Create an Account",
                                          command=lambda: [self.create_account(),
                                                           self.widget_destroy(self.container.margin.loginlbl,
                                                                               self.container.margin.usernamelbl,
                                                                               self.container.margin.username,
                                                                               self.container.margin.passwordlbl,
                                                                               self.container.margin.password,
                                                                               self.container.margin.loginbtn,
                                                                               self.container.margin.nulbl,
                                                                               self.container.margin.nubtn)])
        self.container.margin.nubtn.grid(column=1, row=125, sticky=NSEW, padx=200, pady=6)

        # clears the entry textbox after the information is submitted
        self.container.margin.username.delete(0, END)
        self.container.margin.password.delete(0, END)

    def successful_login(self):
        self.manage_passwords()
        self.widget_destroy(self.container.margin.loginlbl, self.container.margin.usernamelbl,
                          self.container.margin.username, self.container.margin.passwordlbl,
                          self.container.margin.password, self.container.margin.loginbtn,
                          self.container.margin.nulbl, self.container.margin.nubtn)

    def find_query_error(self):
        self.container.noAccLbl = ttk.Label(self.container, text="No accounts for this user...")
        self.container.noAccLbl.grid(column=10, row= 60,padx=2, pady=2)

    def read_query_empty(self):
        self.container.emptyEntry = ttk.Label(self.container, text="Entry boxes cannot be empty!")
        self.container.emptyEntry.grid(column=10, row= 60,padx=2, pady=2)

    def incorrect_password(self):
        self.container.incPass = ttk.Label(self.container, text="Incorrect password!")
        self.container.incPass.grid(column=10, row= 60,padx=2, pady=2)

    def account_not_found(self):
        self.container.noacc = ttk.Label(self.container, text="Account doesn't exist")
        self.container.noacc.grid(column=10, row= 60,padx=2, pady=2)

#-----------------------------------------------------------------------------------------------------------------------

    def create_account(self):

        if hasattr(self.container, 'usrexists'):
            self.container.usrexists.destroy()
        if hasattr(self.container, 'pasexists'):
            self.container.pasexists.destroy()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.container.calbl = ttk.Label(self.container, text="New Account Credentials")
        self.container.calbl.grid(column=10, row=0, sticky=N, padx=20, pady=20)

        self.container.setunlbl = ttk.Label(self.container, text="Enter a username")
        self.container.setunlbl.grid(column=10, row=10, padx=2, pady=2)

        self.container.setun = ttk.Entry(self.container, textvariable= self.unvar, width=30)
        self.container.setun.grid(column=10, row=15, padx=2, pady=2)

        self.container.setpslbl = ttk.Label(self.container, text="Enter a password")
        self.container.setpslbl.grid(column=10, row=25, padx=2, pady=2)

        self.container.setps = ttk.Entry(self.container, show ="*", textvariable= self.pvar, width=30)
        self.container.setps.grid(column=10, row=30, padx=2, pady=2)

        self.container.cabtn = ttk.Button(self.container, text="Create Account",
                               command = lambda: self.connection.cred_check(self.unvar, self.pvar))
        self.container.cabtn.grid(column=10, row=35, padx=2, pady=2)

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
        self.container.returnLogin.grid(column=10, row=50, padx=20, pady=20)

    def user_exists_error(self):
        self.container.usrexists = ttk.Label(self.container, text="User already exists!")
        self.container.usrexists.grid(column=10, row=40)

    def password_unavailable(self):
        self.container.pasexists = ttk.Label(self.container, text="Password Unavailable")
        self.container.pasexists.grid(column=10, row=40)

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
        self.container.welcome_frameMes.grid(column=10, row=0, sticky=N, padx=20, pady=20)

        self.container.managePassButton = ttk.Button(self.container, text="Current Passwords",
                                               command=lambda: [self.manage_passwords(),
                                                                    self.widget_destroy(
                                                                        self.container.welcome_frameMes,
                                                                              self.container.managePassButton,
                                                                              self.container.newPass,
                                                                              self.container.accsettings,
                                                                              self.container.signoutBtn
                                                                        )])
        self.container.managePassButton.grid(column=10, row=10, padx=5, pady=5)

        self.container.newPass = ttk.Button(self.container, text="Password Generator",
                                      command=lambda: [self.newpassword(), self.widget_destroy(
                                                                              self.container.welcome_frameMes,
                                                                                    self.container.managePassButton,
                                                                                    self.container.newPass,
                                                                                    self.container.accsettings,
                                                                                    self.container.signoutBtn
                                                                              )])
        self.container.newPass.grid(column=10, row=20, padx=5, pady=5)

        self.container.accsettings = ttk.Button(self.container, text="Account Settings",
                                          command=lambda: [self.account_settings(), self.widget_destroy(
                                                                                 self.container.welcome_frameMes,
                                                                                       self.container.managePassButton,
                                                                                       self.container.newPass,
                                                                                       self.container.accsettings,
                                                                                       self.container.signoutBtn
                                                                                 )])
        self.container.accsettings.grid(column=10, row=30, padx=5, pady=5)

        self.container.signoutBtn = ttk.Button(self.container, text="Sign Out",
                                         command=lambda: [self.welcome(), self.widget_destroy(
                                                                                 self.container.welcome_frameMes,
                                                                                       self.container.managePassButton,
                                                                                       self.container.newPass,
                                                                                       self.container.accsettings,
                                                                                       self.container.signoutBtn
                                                                                 )])
        self.container.signoutBtn.grid(column=10, row=40, padx=5, pady=5)

    def on_click(self, event, table):
        row = table.identify_row(event.y)
        col = table.identify_column(event.x)

        index = int(col[1:])-1

    # function for the manage password page
    def manage_passwords(self):

        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        dir = os.path.dirname(os.path.abspath(__file__))

        self.container.margin.content = ttk.Frame(self.container.margin)
        self.container.margin.content.grid(row=1,column=1, sticky="NSEW")
        self.container.margin.content.columnconfigure((0,1), weight=2)

        self.container.margin.manlabel = ttk.Label(self.container.margin, text="Password List")
        self.container.margin.manlabel.grid(sticky=N, column=1, row=0, padx=0, pady=20)

        self.container.margin.content.table = ttk.Treeview(self.container.margin.content, columns=("Website", "Email", "Username", "Password"), show="headings")

        self.container.margin.content.table.heading("Website", text="Website")
        self.container.margin.content.table.heading("Email", text="Email")
        self.container.margin.content.table.heading("Username", text="Username")
        self.container.margin.content.table.heading("Password", text="Password")

        self.container.margin.content.table.column("Website", width=100)
        self.container.margin.content.table.column("Email", width=100)
        self.container.margin.content.table.column("Username", width=100)
        self.container.margin.content.table.column("Password", width=100)

        self.container.margin.content.table.bind('<Button-1>', lambda event: self.on_click(event, self.container.margin.table))

        # retrieves credentials and insert them into the table
        self.connection.findwebcredentials(self.unvar, self.container.margin.content.table)
        self.container.margin.content.table.grid(sticky=NSEW, column=1, row=20, padx=20, pady=0)

        pencil_img = tkinter.PhotoImage(file=os.path.join(dir, 'images', 'pencil.png'))
        self.container.margin.content.editbtn = ttk.Button(self.container.margin.content, text='Edit an account', image=pencil_img, command=lambda: self.webcredentry(self.container.table))
        self.container.margin.content.editbtn.image = pencil_img
        self.container.margin.content.editbtn.grid(sticky=NSEW, column=0, row=20, padx=20, pady=0)

        plus_img = tkinter.PhotoImage(file=os.path.join(dir, 'images', 'plus.png'))
        self.container.margin.content.addAccBtn = ttk.Button(self.container.margin.content, text="Add an account", image=plus_img, command=lambda: self.addWeb(self.container.table))
        self.container.margin.content.addAccBtn.image = plus_img
        self.container.margin.content.addAccBtn.grid(sticky=NSEW, column=0, row=30, padx=20, pady=0)

        trashbin_img = tkinter.PhotoImage(file=os.path.join(dir, 'images', 'trash.png'))
        self.container.margin.content.deleteBtn = ttk.Button(self.container.margin.content, text="Delete an Account", image=trashbin_img, command=lambda: self.deleteCredbtn(self.container.table))
        self.container.margin.content.deleteBtn.image = trashbin_img
        self.container.margin.content.deleteBtn.grid(sticky=NSEW, column=0, row=40, padx=20, pady=0)

        self.container.margin.returnMM1 = ttk.Button(self.container.margin, text="Settings",
                                       command=lambda: [self.account_settings(),
                                                        self.widget_destroy(self.container.margin.manlabel,
                                                                                self.container.margin.table,
                                                                                self.container.margin.editbtn,
                                                                                self.container.margin.addAccBtn,
                                                                                self.container.margin.deleteBtn,
                                                                                self.container.margin.returnMM1,
                                                                                self.container.margin.signoutBtn
                                                                        )])
        self.container.margin.returnMM1.grid(column=2, row=0, sticky=NE, padx=2, pady=2)

        self.container.margin.signoutBtn = ttk.Button(self.container, text="Sign Out",
                                               command=lambda: [self.welcome(),
                                                                self.widget_destroy(
                                                            self.container.margin.manlabel,
                                                                self.container.margin.table,
                                                                self.container.margin.editbtn,
                                                                self.container.margin.addAccBtn,
                                                                self.container.margin.deleteBtn,
                                                                self.container.margin.returnMM1,
                                                                self.container.margin.signoutBtn
                                               )])
        self.container.margin.signoutBtn.grid(column=0, row=0, sticky=NW, padx=2, pady=2)

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
        self.container.inLbl.grid(column=10, row=0, pady=20)

        self.container.usredit = ttk.Button(self.container, text="Change Username", command=lambda: self.change_username(self.unvar))
        self.container.usredit.grid(column=10, row=10, pady=5)

        self.container.psedit = ttk.Button(self.container, text="Change Password", command=lambda: self.change_password(self.pvar))
        self.container.psedit.grid(column=1, row=15, pady=5)

        self.container.delacc = ttk.Button(self.container, text="Delete Account", command=lambda: self.warning_message(self.unvar))
        self.container.delacc.grid(column=1, row=20, pady=5)

        self.container.returnmm = ttk.Button(self.container, text="Return",
                                      command=lambda: [self.manage_passwords(),
                                                       self.widget_destroy(
                                                              self.container.inLbl,
                                                                    self.container.usredit,
                                                                    self.container.psedit,
                                                                    self.container.delacc,
                                                                    self.container.returnmm
                                                              )])
        self.container.returnmm.grid(column=1, row=0, pady=10)

    def account_settings_widget_destroy(self):
        self.widget_destroy(
                         self.container.newpassLbl,
                         self.container.newpassEntry,
                         self.container.newpassBtn
                    )

    def change_username(self, unvar):
        self.container.newusrnameLbl = ttk.Label(self.container, text="Enter your new username:")
        self.container.newusrnameLbl.grid(column=10, row=50, padx=2, pady=2)
        self.container.newusrnameEntry = ttk.Entry(self.container, textvariable= self.newunVar, width=30)
        self.container.newusrnameEntry.grid(column=10, row=55, padx=2, pady=2)
        self.container.newusrnameBtn = ttk.Button(self.container, text="Submit",
                                           command=lambda: [self.cngUser(self.unvar, self.newunVar),
                                                            self.widget_destroy(self.container.newusrnameLbl, self.container.newusrnameEntry,
                                                                         self.container.newusrnameBtn, self.container.cancelBtn)])
        self.container.newusrnameBtn.grid(column=10, row=60, padx=2, pady=2)
        self.container.cancelBtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda:
                                       self.widget_destroy(self.container.newusrnameLbl,
                                                    self.container.newusrnameEntry,
                                                    self.container.newusrnameBtn,
                                                    self.container.cancelBtn))
        self.container.cancelBtn.grid(column=1, row=65, padx=2, pady=2)
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

    def editUser(self, table):
        self.container.userEnt = ttk.Entry(self.container, textvariable=self.aUVar)
        self.container.userEnt.pack()
        self.container.edsubmit = ttk.Button(self.container, text="Submit",
                                      command=lambda: [self.connection.eUSub(self.aUVar, self.webVar, self.unvar, table),
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
                                      command=lambda: [self.connection.eESub(self.emlVar, self.aEVar, self.webVar, self.unvar, table),
                                                       self.widget_destroy(self.container.emaillbl,
                                                       self.container.emailEnt, self.container.edsubmit)])
        self.container.edsubmit.pack(pady=2)
        self.container.emailEnt.delete(0, END)
        self.window.bind('<Return>', lambda event: self.container.edsubmit.invoke())

    def specificweb(self, table):
        self.container.edemail = ttk.Button(self.container, text="Change Email", command=lambda: self.edit_email(table))
        self.container.edemail.pack(pady=2)
        self.container.edusr = ttk.Button(self.container, text="Change Username", command=lambda: self.editUser(table))
        self.container.edusr.pack(pady=2)
        self.container.edpass = ttk.Button(self.container, text="Change Password", command=lambda: self.editPass(table))
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
        self.container.edit_btn = ttk.Button(self.container, text="Submit",
                                     command=lambda: [self.specificweb(table),
                                                      self.widget_destroy(self.container.editlbl,
                                                                   self.container.editentry,
                                                                   self.container.edit_btn,
                                                                   self.container.cancelbtn)])
        self.container.edit_btn.pack()
        self.container.cancelbtn = ttk.Button(self.container, text="Cancel",
                                       command=lambda: self.widget_destroy(self.container.editlbl,
                                                                    self.container.editentry,
                                                                    self.container.edit_btn,
                                                                    self.container.cancelbtn))
        self.container.cancelbtn.pack()

        # clears entry box
        self.container.editentry.delete(0, END)
        # binds enter key to button
        self.window.bind('<Return>', lambda event: self.container.edit_btn.invoke())

    def addWeb(self, table):
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

    def editPass(self, table):
        self.container.passEnt = ttk.Entry(self.container, textvariable= self.aPVar)
        self.container.passEnt.pack()
        self.container.edsubmit = ttk.Button(self.container, text="Submit",
                                      command=lambda: [self.connection.ePSub(self.aPVar, self.webVar, self.unvar, table),
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