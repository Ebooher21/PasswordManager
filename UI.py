from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
import random
import string
import tkinter as tk

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
        self.container.grid(sticky="nsew", row=0, column=0)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        # log in frame
        self.welcome_frame = ttk.Frame(self.container)
        self.welcome_frame.grid(sticky="nsew", row=0, column=0)
        self.welcome_frame.columnconfigure(0, weight=1)
        self.welcome_frame.columnconfigure(1, weight=2)
        self.welcome_frame.columnconfigure(2, weight=1)
        self.welcome_frame.rowconfigure(0,weight=2)
        self.welcome_frame.rowconfigure(1, weight=1)
        self.welcome_frame.rowconfigure(2, weight=1)
        self.welcome_frame.rowconfigure(3,weight=1)
        self.welcome_frame.rowconfigure(4, weight=1)
        self.welcome_frame.rowconfigure(6, weight=1)
        self.welcome_frame.rowconfigure(7, weight=3)

        loginlbl = ttk.Label(self.welcome_frame, text="Welcome to the Super Cool Password Manager")
        loginlbl.grid(column=1, row=0, sticky='ns', padx=2, pady=(20,0))

        usernamelbl = ttk.Label(self.welcome_frame, text="Username")
        usernamelbl.grid(column=1, row=1, sticky='nsew', padx=2, pady=2)

        self.username = ttk.Entry(self.welcome_frame, textvariable=self.unvar, width=30)
        self.username.grid(sticky='nsew', column=1, row=2, padx=2, pady=2)

        passwordlbl = ttk.Label(self.welcome_frame, text="Password")
        passwordlbl.grid(sticky='nsew', column=1, row=3, padx=2, pady=2)

        self.password = ttk.Entry(self.welcome_frame, show="*", textvariable=self.pvar, width=30)
        self.password.grid(column=1, row=4, sticky='nsew', padx=2, pady=2)

        loginbtn = ttk.Button(self.welcome_frame, text="Log in",
                              command=lambda: self.connection.exist_credentials(self.unvar, self.pvar))
        loginbtn.grid(column=1, row=5, sticky='nsew', padx=2, pady=2)
        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: loginbtn.invoke())

        nubtn = ttk.Button(self.welcome_frame, text="Create an Account",
                           command=lambda: self.create_account())
        nubtn.grid(column=1, row=6, sticky='nsew', padx=20, pady=20)

        # create account frame
        self.create_frame = ttk.Frame(self.container)
        self.create_frame.grid(sticky="nsew", row=0, column=0)
        self.create_frame.columnconfigure(0, weight=1)
        self.create_frame.columnconfigure(1, weight=2)
        self.create_frame.columnconfigure(2, weight=1)
        self.create_frame.rowconfigure(0,weight=2)
        self.create_frame.rowconfigure(1,weight=1)
        self.create_frame.rowconfigure(2,weight=1)
        self.create_frame.rowconfigure(3, weight=1)
        self.create_frame.rowconfigure(4, weight=1)
        self.create_frame.rowconfigure(5, weight=1)
        self.create_frame.rowconfigure(6,weight=1)
        self.create_frame.rowconfigure(7, weight=3)

        calbl = ttk.Label(self.create_frame, text="New Account Credentials")
        calbl.grid(column=1, row=0, sticky='ns', padx=0, pady=(20,0))

        setunlbl = ttk.Label(self.create_frame, text="Enter a username")
        setunlbl.grid(sticky='nsew', column=1, row=1, padx=2, pady=2)

        self.setun = ttk.Entry(self.create_frame, textvariable=self.unvar, width=30)
        self.setun.grid(sticky='nsew', column=1, row=2, padx=2, pady=2)

        setpslbl = ttk.Label(self.create_frame, text="Enter a password")
        setpslbl.grid(sticky='nsew', column=1, row=3, padx=2, pady=2)

        self.setps = ttk.Entry(self.create_frame, show="*", textvariable=self.pvar, width=30)
        self.setps.grid(sticky='nsew', column=1, row=4, padx=2, pady=2)

        cabtn = ttk.Button(self.create_frame, text="Create Account",
                           command=lambda: self.connection.cred_check(self.unvar, self.pvar))
        cabtn.grid(sticky='nsew', column=1, row=5, padx=2, pady=2)

        # binds the Enter key to the button
        self.window.bind('<Return>', lambda event: cabtn.invoke())

        returnLogin = ttk.Button(self.create_frame, text="Return to the Login screen",
                                 command=lambda: self.welcome())
        returnLogin.grid(sticky='nsew', column=1, row=6, padx=20, pady=20)

        # manage passwords frame
        self.main_frame = ttk.Frame(self.container)
        self.main_frame.grid(sticky="nsew", row=0, column=0)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.columnconfigure(2, weight=1)

        dir = os.path.dirname(os.path.abspath(__file__))

        signoutBtn = ttk.Button(self.main_frame, text="Sign Out",
                                command=lambda: [self.welcome()])
        signoutBtn.grid(column=0, row=0, sticky=NW, padx=5, pady=5)

        manlabel = ttk.Label(self.main_frame, text="Password List")
        manlabel.grid(column=1, row=0, sticky=N, padx=0, pady=20)

        settings_button = ttk.Button(self.main_frame, text="Settings",
                                     command=lambda: [self.account_settings()])
        settings_button.grid(column=2, row=0, sticky=NE, padx=5, pady=5)

        content = ttk.Frame(self.main_frame)
        content.grid(row=1, column=1, sticky=NSEW)
        content.columnconfigure(0, weight=2)
        content.columnconfigure(1, weight=2)

        buttons_frame = ttk.Frame(content)
        buttons_frame.grid(row=0, column=0, sticky=NSEW)
        buttons_frame.columnconfigure(0, weight=2)

        table_frame = ttk.Frame(content)
        table_frame.grid(row=0, column=1, sticky=NSEW)
        table_frame.columnconfigure(1, weight=2)

        self.table = ttk.Treeview(table_frame, columns=("Website", "Email", "Username", "Password"), show="headings")

        self.table.heading("Website", text="Website")
        self.table.heading("Email", text="Email")
        self.table.heading("Username", text="Username")
        self.table.heading("Password", text="Password")

        self.table.column("Website", width=100)
        self.table.column("Email", width=100)
        self.table.column("Username", width=100)
        self.table.column("Password", width=100)

        self.table.grid(sticky=NSEW, column=1, row=0, padx=(1, 10), pady=0)

        pencil_img = tk.PhotoImage(file=os.path.join(dir, 'images', 'pencil.png'))
        editbtn = ttk.Button(buttons_frame, text='Edit an account', image=pencil_img,
                             command=lambda: self.webcredentry(self.table))
        editbtn.image = pencil_img
        editbtn.grid(sticky=NE, column=0, row=0, padx=(10, 1), pady=0)

        plus_img = tk.PhotoImage(file=os.path.join(dir, 'images', 'plus.png'))
        addAccBtn = ttk.Button(buttons_frame, text="Add an account", image=plus_img,
                               command=lambda: self.addWeb(self.table))
        addAccBtn.image = plus_img
        addAccBtn.grid(sticky='NE', column=0, row=1, padx=(10, 1), pady=0)

        trashbin_img = tk.PhotoImage(file=os.path.join(dir, 'images', 'trash.png'))
        deleteBtn = ttk.Button(buttons_frame, text="Delete an Account", image=trashbin_img,
                               command=lambda: self.deleteCredbtn(self.table))
        deleteBtn.image = trashbin_img
        deleteBtn.grid(sticky='NE', column=0, row=2, padx=(10, 1), pady=0)

        self.settings_frame = ttk.Frame(self.container)
        self.settings_frame.grid(sticky="nsew", row=0, column=0)
        self.settings_frame.columnconfigure(0,weight=1)
        self.settings_frame.columnconfigure(1,weight=10)
        self.settings_frame.columnconfigure(2,weight=1)

        inLbl = ttk.Label(self.settings_frame, text="Account Settings")
        inLbl.grid(column=1, row=0, pady=20)

        usredit = ttk.Button(self.settings_frame, text="Change Username",
                             command=lambda: self.change_username(self.unvar))
        usredit.grid(column=1, row=10, pady=5)

        psedit = ttk.Button(self.settings_frame, text="Change Password",
                            command=lambda: self.change_password(self.pvar))
        psedit.grid(column=1, row=15, pady=5)

        delacc = ttk.Button(self.settings_frame, text="Delete Account",
                            command=lambda: self.warning_message(self.unvar))
        delacc.grid(column=1, row=20, pady=5)

        returnmm = ttk.Button(self.settings_frame, text="Return",
                              command=lambda: self.manage_passwords())
        returnmm.grid(column=0, row=0, padx=2, pady=2)

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

        self.welcome_frame.tkraise()

        # clears the entry textbox after the information is submitted
        self.username.delete(0, END)
        self.password.delete(0, END)

    def successful_login(self):
        self.manage_passwords()

    def find_query_error(self):

        if hasattr(self.welcome_frame, 'emptyEntry'):
            self.welcome_frame.emptyEntry.destroy()
        if hasattr(self.welcome_frame, 'incPass'):
            self.welcome_frame.incPass.destroy()
        if hasattr(self.welcome_frame, 'noacc'):
            self.welcome_frame.noacc.destroy()

        self.welcome_frame.noAccLbl = ttk.Label(self.welcome_frame, text="No accounts for this user...")
        self.welcome_frame.noAccLbl.grid(column=1, row= 60,padx=2, pady=2)

    def read_query_empty(self):

        if hasattr(self.welcome_frame, 'noAccLbl'):
            self.welcome_frame.noAccLbl.destroy()
        if hasattr(self.welcome_frame, 'incPass'):
            self.welcome_frame.incPass.destroy()
        if hasattr(self.welcome_frame, 'noacc'):
            self.welcome_frame.noacc.destroy()

        self.welcome_frame.emptyEntry = ttk.Label(self.welcome_frame, text="Entry boxes cannot be empty!")
        self.welcome_frame.emptyEntry.grid(column=1, row= 60,padx=2, pady=2)

    def incorrect_password(self):

        if hasattr(self.welcome_frame, 'emptyEntry'):
            self.welcome_frame.emptyEntry.destroy()
        if hasattr(self.welcome_frame, 'noAccLbl'):
            self.welcome_frame.noAccLbl.destroy()
        if hasattr(self.welcome_frame, 'noacc'):
            self.welcome_frame.noacc.destroy()

        self.welcome_frame.incPass = ttk.Label(self.welcome_frame, text="Incorrect password!")
        self.welcome_frame.incPass.grid(column=1, row= 60,padx=2, pady=2)

    def account_not_found(self):

        if hasattr(self.welcome_frame, 'emptyEntry'):
            self.welcome_frame.emptyEntry.destroy()
        if hasattr(self.welcome_frame, 'incPass'):
            self.welcome_frame.incPass.destroy()
        if hasattr(self.welcome_frame, 'noAccLbl'):
            self.welcome_frame.noAccLbl.destroy()

        self.welcome_frame.noacc = ttk.Label(self.welcome_frame, text="Account doesn't exist")
        self.welcome_frame.noacc.grid(column=1, row= 60,padx=2, pady=2)

#-----------------------------------------------------------------------------------------------------------------------

    def create_account(self):

        if hasattr(self.container, 'usrexists'):
            self.container.usrexists.destroy()
        if hasattr(self.container, 'pasexists'):
            self.container.pasexists.destroy()
        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.create_frame.tkraise()

        # clears the entry textbox after the information is submitted
        self.setun.delete(0,END)
        self.setps.delete(0,END)

    def user_exists_error(self):
        self.container.usrexists = ttk.Label(self.container, text="User already exists!")
        self.container.usrexists.grid(column=10, row=40)

    def password_unavailable(self):
        self.container.pasexists = ttk.Label(self.container, text="Password Unavailable")
        self.container.pasexists.grid(column=10, row=40)

    def successful_creation(self):
        self.manage_passwords()
        self.widget_destroy(self.container.calbl, self.container.setunlbl,
                     self.container.setun, self.container.setpslbl, self.container.setps,
                     self.container.cabtn, self.container.returnLogin)

#-----------------------------------------------------------------------------------------------------------------------

    def on_click(self, event):
        row = self.table.identify_row(event.y)
        col = self.table.identify_column(event.x)

        index = int(col[1:])-1

    def manage_passwords(self):

        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.main_frame.tkraise()

        if self.table.get_children() != ():
            for row in self.table.get_children():
                self.table.delete(row)

        # retrieves credentials and insert them into the table
        self.connection.findwebcredentials(self.unvar, self.table)

        self.table.bind('<Button-1>', lambda event: self.on_click(event))

    def manager_widget_destroy(self):
        self.widget_destroy(
                      self.container.webLbl,
                            self.container.webEntry,
                            self.container.webBtn,
                            self.container.cancelBtn
                      )

    def account_settings(self):

        if hasattr(self.container, 'emptyEntry'):
            self.container.emptyEntry.destroy()

        self.settings_frame.tkraise()

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