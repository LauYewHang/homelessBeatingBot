import discord
from discord.ext import commands
import mysql.connector # for connecting to mysql database

import botToken # for discord's bot token

class homelessBeatingBot(commands.Bot):
    async def on_ready(self):
        print("It is homeless beating time everyone!!!!")

intents = discord.Intents.all()

bot = homelessBeatingBot(command_prefix = ".hb", intents = intents, activity = discord.Activity(name = "homeless beating", type = discord.ActivityType.competing, state = "In competition... Currently rank #1", timestamps = {"start":1721698794000}))
# discord.Activity() class with attributes:
# `type` - set up the activity type for the bot, in this case, discord.ActivityType.competing
# `state` - kinda like a caption for the activity type, take a string and display it when looking to the bot profile
# `timestamps` - a dictionary with two keys: `start` & `end`, set up the start and end time of the activity in Unix epoch, milliseconds (doesn't display it though, but can be retrieve later in property)
bot.run(botToken.botToken)