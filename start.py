import discord
from discord.ext import commands
import mysql.connector
import random
import os

from keys import *

memeQuantity = len(os.listdir("homelessMeme/"))

# connect to the database
db = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_user_password,
    database = db_name,
    # `autocommit = True` makes all the subsequent insertion into tables auto commit and doesn't need to call cursor.commit()
    autocommit = True
)

# cursor object for executing statements to communicate with MySQL database
cursor = db.cursor()

@commands.command()
async def start(context):
    userID = str(context.author.id)
    cursor.execute("SELECT EXISTS(SELECT * FROM tb_user WHERE discordID =" + userID + ")")
    # `SELECT * FROM tb_user WHERE discordID = userID` checks if the user has registered for homelessBeatingBot
    # `SELECT EXISTS` checks if the search result return anything. if yes, then it returns the number of values return by the searching; otherwise it is 0
    result = cursor.fetchall()[0][0]
    # cursor.fetchall() get the results from the last query
    # in this case the result is: [(1,)] (if the value exist in database)
    # [(0,)] if the value doesn't exist in database
    # result is returned in a list, which inside is tuple(s) of values of the results of query 
    # (thus we use [0][0], the first indexing specify the first tuple, the second indexing specify the first value inside the tuple)

    # create embed to make message pwetty
    embed = discord.Embed()
    if (result == 0): # check if the user discord id doesn't exist in database
        embed.color = discord.Colour.from_rgb(50, 205, 50) # lime green for embed colour cause apparently it represents welcoming
        # title and description of the embed
        embed.title = "**__Welcome to the board!!__**"
        embed.description = "We are happy to have you in the team (づ๑•ᴗ•๑)づ♡\nLet's give our best in beating the homeless,\nfor everyone's brighter tomorrow!\n\nYour legacy begin here..."
        # set the thumbail for the embed
        thumbnail = discord.File("emoji/hbb_excited.gif")
        embed.set_thumbnail(url = "attachment://hbb_excited.gif")
        # add the user's discord id into the database
        cursor.execute("INSERT INTO tb_user (discordID) VALUES(" + userID +")")

        await context.message.reply(files = [thumbnail], embed = embed)
    else:
        embed.colour = discord.Colour.from_rgb(220, 20, 60) # crimson color cause it is hot
        # title and description to tell the player they have already registered
        embed.title = "**__Did you forgor?__**"
        embed.description = "Darling you have already started your adventure!\nHappy beating homeless! ଘ(੭˃ᴗ˂)੭♡\nHere's a cookie :cookie: and a homeless meme, mwah <3"
        # set up thumbnail (a smol image at the top right corner)
        thumbnail = discord.File("emoji/hbb_confused.gif")
        embed.set_thumbnail(url = "attachment://hbb_confused.gif")
        # set up homeless meme image attachment
        memeID = "meme" + str(random.randint(0, memeQuantity - 1)) + ".jpg"
        memeFile = discord.File("homelessMeme/" + memeID)
        embed.set_image(url = "attachment://" + memeID)

        await context.message.reply(files = [thumbnail, memeFile], embed = embed)
        # use `file` for single attachment; `files` for a sequence of attachments
        # the thumnnail file is for the smol picture at the top right, memeFile is the larger image at the bottom
        # source: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-upload-an-image

async def setup(bot):
    bot.add_command(start)