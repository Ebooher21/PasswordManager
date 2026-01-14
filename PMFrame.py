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
parent.style = Style()
parent.style.theme_use('clam')
ui = UI(parent, connection)
connection.ui = ui
ui.welcome()

#initate main loop
parent.mainloop()
