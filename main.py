#importing files
import sqlite3
from tkinter import *
from tkinter import ttk
import random
from sql_database import *
from home import *

users_database() #calls the function which creates the sql database
menu_window() #calls menu() from the home.py file