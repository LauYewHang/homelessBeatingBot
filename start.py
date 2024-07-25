import discord
from discord.ext import commands
import mysql.connector

from keys import *

# connect to the database
db = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_user_password,
)