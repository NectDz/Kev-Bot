import discord
from discord import embeds
from discord.ext import commands
from gifs import cuddleGifs,hugGifs,slapGifs,sexyGifs,kissGifs,beanerGifs,crackerGifs, gmGifs, gnGifs, killGifs, cryGifs, fuckYouGifs, shutUpGifs, EDPGifs, AsianGifs
import time, random, os, giphy_client
from giphy_client.rest import ApiException
import asyncio

# Dice 

num = [str(i) for i in range(1,10)]

# NSFW 

nsfwCounter = 0 
apiKey = os.environ['giphyKEY']
api_instance = giphy_client.DefaultApi()
api_response = api_instance.gifs_search_get(apiKey, 'nude girls', limit=50, rating = 'r')
lst = list(api_response.data)

# Gay Meter

gayMeter = [i for i in range(1,101)]

class miscCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
    # Gm Command 

    @commands.command()
    async def gm(self,ctx, user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return 

        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"GoodMorning Command",value = f'**{ctx.author.mention} saying GoodMorning to {user}!**')
        em.set_image(url = random.choice(gmGifs))
        await ctx.send(embed = em )


    @commands.command()
    async def gn(self,ctx, user):

        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return 

        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"GoodNight Command",value = f'**{ctx.author.mention} saying GoodNight to {user}!**')
        em.set_image(url = random.choice(gnGifs))

        await ctx.send(embed = em )

    # Ping Command
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f' {round(commands.latency * 1000)}ms')

    # 8 ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx,*,question):
        responses = ["Indeed","Seems unlikely","Very doubtful","Of course","Without a doubt","Can't say...","No"]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # Best Command
    @commands.command()
    async def king(self,ctx,user):
        await ctx.send(f'{user} DO NOT EVER SPEAK TO THE KING (KingKev aka NectDzN) LIKE THAT, HE IS KING!')

    # Dice command

    @commands.command()
    async def dice(self,ctx,*,diceNum):
        numberWord = random.choice(num)
        correct = ""
        if str(diceNum) == numberWord:
            correct = "Correct!"
        else :
            correct = "Incorrect!"
        time.sleep(0.5)
        await ctx.send(f'You are {correct}\n{numberWord} was the answer!')

    # Slap command

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slap(self,ctx,user):
        if str(user) == "@everyone":
            await ctx.message.add_reaction('🤔')
            return

        slap  = random.choice(slapGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Slap Command",value = f'**{ctx.author.mention} slapped {user}!** :rage:')
        em.set_image(url = slap)
        await ctx.send(embed = em)

    # Sexy Command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sexy(self,ctx):
        sexy = sexyGifs
        await ctx.send(f'{random.choice(sexy)}' )

    # Hug Command

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hug(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return 


        hug  = random.choice(hugGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Hug Command",value = f'**{ctx.author.mention} hugged {user}!**')
        em.set_image(url = hug)
        await ctx.send(embed =em)

    # Cuddle Command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cuddle(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.send(f"Can't do not do that weirdo..." ) 
            return 

        cuddle  = random.choice(cuddleGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Cuddle Command",value = f'**{ctx.author.mention} cuddled with {user}!** :kissing_heart:')
        em.set_image(url = cuddle)
        await ctx.send(embed =em)

    # Kiss Command

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kiss(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return


        kiss  = random.choice(kissGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Kiss Command",value = f'**{ctx.author.mention} kissed {user}!** :kissing_heart:')
        em.set_image(url = kiss)
        await ctx.send(embed =em)

    # Beaner Command 


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def beaner(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        beaner  = random.choice(beanerGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Beaner Command",value = f'**{ctx.author.mention} called {user} a beaner! :poop:**')
        em.set_image(url = beaner)
        await ctx.send(embed = em)

    # Cracker Command 

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cracker(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        cracker  = random.choice(crackerGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Cracker Command",value = f'**{ctx.author.mention} called {user} a cracker!**')
        em.set_image(url = cracker)
        await ctx.send(embed =em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def chink(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        asian  = random.choice(AsianGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Asian Command",value = f'**{ctx.author.mention} called {user} a chink!**')
        em.set_image(url = asian)
        await ctx.send(embed =em)

    # Kill Command

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kill(self,ctx,user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        kill  = random.choice(killGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Kill Command",value = f'**{ctx.author.mention} killed {user}! SOMEONE DO SOMETHING!** :eyes:')
        em.set_image(url = kill)
        await ctx.send(embed =em)

    # Cry Command

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cry(self,ctx):
        cry  = random.choice(cryGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Cry Command",value = f'**{ctx.author.mention} is crying!**')
        em.set_image(url = cry)
        await ctx.send(embed =em)

    # Fuck You 
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fu(self,ctx, user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        fuck  = random.choice(fuckYouGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"Fuck You Command",value = f'**{ctx.author.mention} says FUCK YOU to {user}**')
        em.set_image(url = fuck)
        await ctx.send(embed =em)

    # NSFW 
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nsfw(self,ctx):
        global api_response, lst, nsfwCounter

        if ctx.channel.nsfw == True: 
            if nsfwCounter >= 75: 
                api_response = api_instance.gifs_search_get(apiKey, 'hot girls', limit=50, rating = 'r')
                lst = list(api_response.data)
                nsfwCounter = 0 

            nsfwCounter += 1
            
            gif = random.choice(lst)

            em = discord.Embed(color = discord.Colour.blue(),title = "KevBot NSFW")
            em.set_image(url = f'https://media.giphy.com/media/{gif.id}/giphy.gif')

            await ctx.send(embed = em)
        else : 
            await ctx.send("Please use this command on a NSFW Channel!")

    # Shut up
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def shutup(self,ctx, user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        shutup  = random.choice(shutUpGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"ShutUp Command",value = f'**{ctx.author.mention} told {user} to shut up!**')
        em.set_image(url = shutup)
        await ctx.send(embed =em)

    

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def howgay(self,ctx, user):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return
        em = discord.Embed(colour = discord.Colour.purple())
        em.add_field(name = f"Gay Meter",value = f'{user} is {random.choice(gayMeter)}% gay 🏳️‍🌈!')
        await ctx.send(embed =em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def edp(self,ctx, user):
        edp  = random.choice(EDPGifs)
        em = discord.Embed(colour = discord.Colour.red())
        em.add_field(name = f"EDP Command",value = f'**{ctx.author.mention}** says {user} went EDP Mode!')
        em.set_image(url = edp)
        await ctx.send(embed =em)
    
    # Quick Poll - Coded by Jeremy <333
    @commands.command()
    async def poll(self,ctx, *, question=None):
        if question == None:
            await ctx.send("Please write a poll you fucking monkey!")
    
        icon_url = ctx.author.avatar_url 
    
        pollEmbed = discord.Embed(title = "New Poll!", description = f"{question}")
    
        pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
    
        pollEmbed.timestamp = ctx.message.created_at 
    
        await ctx.message.delete()
    
        poll_msg = await ctx.send(embed = pollEmbed)
    
        await poll_msg.add_reaction("⬆️")
        await poll_msg.add_reaction("⬇️")

    # Avatar command

    @commands.command()
    async def av(self,ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)

    # Text To Speech

    @commands.command()
    async def test(self,ctx, *, text):
        await ctx.send(f'{text}', tts=True)

    # Server Info Command

    @commands.command()
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
        
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(miscCommands(bot))
