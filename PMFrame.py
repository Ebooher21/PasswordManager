import os
from Connect import *
from UI import *

#uses created environmental variables
db_host = os.environ.get('db_host')
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_database = os.environ.get('db_database')

#connection variable so the functions can access the database
connection = Connect(db_host, db_user, db_password, db_database)

#mainwindow setup
ui = UI(connection)

#initate main loop
ui.mainloop()
