import discord
from discord import embeds
from discord.ext import commands
from gifs import cuddleGifs,hugGifs,slapGifs,sexyGifs,kissGifs,beanerGifs,crackerGifs, gmGifs, gnGifs, killGifs, cryGifs, fuckYouGifs, shutUpGifs, EDPGifs, AsianGifs
from check import checkIfGif
import time, random, os, asyncpraw, giphy_client
from giphy_client.rest import ApiException
import asyncio

# Reddit 

reddit = asyncpraw.Reddit(client_id = os.environ['clientID'],
                     client_secret = os.environ['clientSecret'],
                     username = os.environ['redditUser'],
                     password = os.environ['redditPass'],
                     user_agent= os.environ['userAgent'])

# Meme 
allSubs = []
memeCounter = 0 

# Gaming
gamingList = []
gamingCounter = 0 
class redditCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        global allSubs, memeCounter, reddit
        if len(allSubs) == 0:
            memeCounter = 0
            subreddit = await reddit.subreddit("memes")
            allSubs =[]

            async for submission in subreddit.hot(limit=75):
                if checkIfGif(submission.url):
                    allSubs.append(submission)

        memeCounter += 1

        random_sub = random.choice(allSubs)

        name = random_sub.title
        url = random_sub.url
        em = discord.Embed(color = discord.Colour.blue(),title = ":100: KevBot Meme :100:", description = name)
        em.set_image(url = url)

        await ctx.send(embed = em)
        allSubs.pop(random_sub)

    # Gaming 
    @commands.command()
    async def gaming(self, ctx):
        global gamingList, gamingCounter
        if len(gamingList) == 0 or gamingCounter >= 75:
            gamingCounter = 0 
            subreddit = await reddit.subreddit("gaming")
            gamingList = []
            async for submission in subreddit.hot(limit=75):
                if checkIfGif(submission.url) == True:
                    gamingList.append(submission)    
        
        gamingCounter += 1

        random_sub = random.choice(gamingList)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(color = discord.Colour.blue(),title = ":100: KevBot Gaming :100:", description = name)
        em.set_image(url = url)

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(redditCommands(bot))

