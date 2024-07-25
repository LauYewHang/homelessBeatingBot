import discord
from discord.ext import commands
import random
import os, os.path # for accessing directory
# print(len([name for name in os.listdir("homelessMeme/")])) - print the number of files in the directory
# source: https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
memeQuantity = len(os.listdir("homelessMeme/")) # get the number of memes
# os.listdir("path") - returns a list of files inside the directory

# the function for hmeme
@commands.command()
async def hmeme(context):
    index = random.randint(0, memeQuantity)
    newMeme = "meme" + str(index) +".jpg"
    await context.message.reply(file = discord.File("homelessMeme/" + newMeme))

# setup function is used for discord.ext.commands.bot.load_extension() to recognize it and add the command
async def setup(bot):
    bot.add_command(hmeme)