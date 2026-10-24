import os
import Connect
from Connect import *
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from UI import *

#uses created environmental variables
db_host = os.environ.get('db_host')
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_database = os.environ.get('db_database')

#connection variable so the functions can access the database
connection = Connect(db_host,db_user,db_password,db_database)
connection.connection_check()

#mainwindow setup
parent = tk.Tk()
parent.minsize(750,550)
parent.columnconfigure(0, weight=1)
parent.rowconfigure(0, weight=1)
style = Style(parent)
style.theme_use('clam')
style.configure('TFrame', background='#aac4e0')
style.configure('TLabel', background='#aac4e0', foreground='#597598', font=('Cascadia Code', 20))
style.configure('Sub.TLabel', background='#aac4e0', foreground='#597598', font=('Cascadia Code', 15))
style.configure('TButton', background='#aac4e0',foreground="#597598",font=("Cascadia Code", 12), bordercolor='#d1ddeb')
style.configure('TEntry', background='#aac4e0', fieldbackground='#d1ddeb', bordercolor='#d1ddeb', foreground='#597598', font=('Cascadia Code', 12))
style.configure('Treeview', background='#d1ddeb', fieldbackground='#d1ddeb', foreground='#597598', font=('Cascadia Code', 12))
style.configure('Treeview.Heading', background='#aac4e0',foreground="#597598", bordercolor='#d1ddeb', font=('Cascadia Code', 12))

ui = UI(parent, connection)
connection.ui = ui
ui.welcome()

#initate main loop
parent.mainloop()
