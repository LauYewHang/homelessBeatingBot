import discord
from discord.ext import commands
import mysql.connector # for connecting to mysql database

import hmeme
import start

import keys # for discord's bot token

# create class homelessBeatingBot from discord.ext.commands.Bot
class homelessBeatingBot(commands.Bot):
    async def on_ready(self):
        print("It is homeless beating time everyone!!!!")
        # load the extension (hmeme function) from hmeme.py
        # source: https://www.youtube.com/watch?v=gX4_ZJl9BKg
        await bot.load_extension("hmeme")

intents = discord.Intents.all()

# create object homelessBeatingBot
bot = homelessBeatingBot(command_prefix = ".hb ", intents = intents, activity = discord.Activity(name = "homeless beating", type = discord.ActivityType.competing, state = "In competition... Currently rank #1", timestamps = {"start":1721698794000}))
# discord.Activity() class with attributes:
# `type` - set up the activity type for the bot, in this case, discord.ActivityType.competing
# `state` - kinda like a caption for the activity type, take a string and display it when looking to the bot profile
# `timestamps` - a dictionary with two keys: `start` & `end`, set up the start and end time of the activity in Unix epoch, milliseconds (doesn't display it though, but can be retrieve later in property)

# activate the bot
bot.run(keys.botToken)