import discord
from discord import embeds
from discord.ext import commands
from check import checkIfGif
import random, os, asyncpraw

class helpCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        
        em = discord.Embed(colour = discord.Colour.gold(),title = "Help", description = "Use **!kg <command>** to use a command\nDo **!kg help <command>** to see how to use the command")
        em.add_field(name = "**kiss**", value = "Kisses the user you mentioned :kissing_heart:")
        em.add_field(name = "**meme**", value = "Sends a random meme :laughing:")
        em.add_field(name = "**nsfw**", value = "Sends a NSFW **(Use in NSFW)** :eyes:")
        em.add_field(name = "**gaming**", value = "Sends gaming related pics/memes")
        em.add_field(name = "**slap**", value = "Slaps the user you mentioned!")
        em.add_field(name = "**cuddle**", value = "Cuddle with the user you mentioned! :heart:")

        em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
        em.set_footer(text=f'Page 1 out of 3')
        await ctx.send(embed = em)

    @help.command(aliases=['2'])
    async def help2(self, ctx):    
        em = discord.Embed(colour = discord.Colour.gold(),title = "Help 2", description = "Use **!kg <command>** to use a command\nDo **!kg help <command>** to see how to use the command")
        em.add_field(name = "**hug**", value = "Hugs the user you mentioned!")
        em.add_field(name = "**kill**", value = "Kills the user you mentioned! :smiling_imp:")
        em.add_field(name = "**fu**", value = "Tells the user you mentioned **FUCK YOU** :joy:")
        em.add_field(name = "**shutup**", value = "Tells the user you mentioned to shut their mouth")
        em.add_field(name = "**gm**", value = "Says GoodMorning to your favorite person!")
        em.add_field(name = "**gn**", value = "Says GoodNight to your favorite person!")

        em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
        em.set_footer(text=f'Page 2 out of 3')
        await ctx.send(embed = em)

    @help.command(aliases=['3'])
    async def help3(self,ctx):    
        em = discord.Embed(colour = discord.Colour.gold(),title = "Help 3", description = "Use **!kg <command>** to use a command\nDo **!kg help <command>** to see how to use the command")
        em.add_field(name = "**jail**", value = "Puts the user you mentioned in Jail!")
        em.add_field(name = "**howgay**", value = "Tells you how gay the user you mentioned is 🏳️‍🌈")
        em.add_field(name = "**edp**", value = "Use this when someone goes edp mode!")
        em.add_field(name = "**snipe**", value = "Snipes messages that have been deleted by someone.")
        em.add_field(name = "**poll**", value = "Makes a poll to let you know what others think!")
        em.add_field(name = "**av**", value = "Shows someones avatar.")


        em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
        em.set_footer(text=f'Page 3 out of 3')
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(helpCommands(bot))
