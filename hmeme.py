import discord
from discord.ext import commands
import random
import os, os.path # for accessing directory
# print(len([name for name in os.listdir("homelessMeme/")])) - print the number of files in the directory
# source: https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
memeQuantity = len(os.listdir("homelessMeme/")) # get the number of memes
# os.listdir("path") - returns a list of files inside the directory

# source: https://www.youtube.com/watch?v=gX4_ZJl9BKg (for loading extension)
# the function for hmeme
@commands.command()
async def hmeme(context):
    # select a random homeless meme from the file (-1 because randint is inclusive for both argument)
    index = random.randint(0, memeQuantity - 1)
    newMeme = "meme" + str(index) +".jpg"
    # create an embed for the message so it looks pwetty
    # set the colour of embed (the side stripe thingy) to yellow colour (it is discord.Colour.yellow() because yellow() is a class method)
    embed = discord.Embed(colour = discord.Colour.yellow(), title = "__**Homeless meme**__ :fire:")
    # set the image of the embed (this is a weird one, if you want to upload an image from the web you can directly put the url
    # of the image; however if you want to upload local image, you need to add "attachment://" + `fileName`,
    # note: it is the file name, not the path name, so it needs to be combined with file = discord.File() or else it would not work)
    embed.set_image(url = "attachment://" + newMeme)
    await context.message.reply(file = discord.File("homelessMeme/" + newMeme), embed = embed)
    # `file` argument allows the bot to upload file like images, where `discord.File()` takes the path as argument

# setup function is used for discord.ext.commands.bot.load_extension() to recognize it and add the command
async def setup(bot):
    bot.add_command(hmeme)