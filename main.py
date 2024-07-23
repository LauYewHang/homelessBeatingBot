import discord
from discord.ext import commands

import botToken # for discord's bot token

class homelessBeatingBot(commands.bot):
    async def on_ready(self):
        print("It is homeless beating time everyone!!!!")

intents = discord.Intents.all()

bot = hoemlessBeatingBot(command_prefix = ".hb", intents = intents)
bot.run(botToken.botToken)