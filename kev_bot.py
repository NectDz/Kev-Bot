
import discord
from discord import embeds
from discord.ext import commands
from gifs import cuddleGifs,hugGifs,slapGifs,sexyGifs,kissGifs,beanerGifs,crackerGifs, gmGifs, gnGifs, killGifs, cryGifs, fuckYouGifs, shutUpGifs, EDPGifs, AsianGifs
from check import checkIfGif
import time, random, os, asyncpraw, giphy_client
from giphy_client.rest import ApiException
import asyncio
allSubs = []
memeCounter = 0 
reddit = asyncpraw.Reddit(client_id = os.environ['clientID'],
                     client_secret = os.environ['clientSecret'],
                     username = os.environ['redditUser'],
                     password = os.environ['redditPass'],
                     user_agent= os.environ['userAgent'])

intents= discord.Intents.default()
intents.members = True

botPrefix = "!kg "

client = commands.Bot(command_prefix= botPrefix, case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!kg help'))
    print("Bot is ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has entered!.')

@client.event
async def on_member_remove(member):
    print(f'{member} is gone!.')

# CoolDowns

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):  
        # isinstance is used to compare 2 thing. If they are the same it returns True in this case were comparing if the error is equal to the other error
        em = discord.Embed(color = discord.Colour.blue(),
        title = "Slow down there partner...", description = 'The command **{}** is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))
        await ctx.send(embed = em)

# Mod Commands 

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member,*, reason):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    await user.send('You have been kicked from the server!')
    await user.kick(reason =reason)

# Ban 

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member,*, reason):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return


    await ctx.send(f"{user} has been banned by {ctx.author.mention}")
    await user.ban(reason =reason)


# Clear Command

@client.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount : int):
    amount += 1

    if amount <= 85: 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount-1} message(s) have been deleted!")
        return 
    else :  
        await ctx.send("That amount is too damn high!")

# Mute 

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(860677993894903829)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

# Unmute

@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(860677993894903829)
    await member.remove_role(muted_role)

    await ctx.send(member.mention + " has been unmuted")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Gm Command 

@client.command()
async def gm(ctx, user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return 

    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"GoodMorning Command",value = f'**{ctx.author.mention} saying GoodMorning to {user}!**')
    em.set_image(url = random.choice(gmGifs))
    await ctx.send(embed = em )


@client.command()
async def gn(ctx, user):

    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return 

    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"GoodNight Command",value = f'**{ctx.author.mention} saying GoodNight to {user}!**')
    em.set_image(url = random.choice(gnGifs))

    await ctx.send(embed = em )

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f' {round(client.latency * 1000)}ms')

# 8 ball
@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
    responses = ["Indeed","Seems unlikely","Very doubtful","Of course","Without a doubt","Can't say...","No"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Best Command
@client.command()
async def king(ctx,user):
    await ctx.send(f'{user} DO NOT EVER SPEAK TO THE KING (KingKev aka NectDzN) LIKE THAT, HE IS KING!')

num = [str(i) for i in range(1,10)]

# Dice command

@client.command()
async def dice(ctx,*,diceNum):
    numberWord = random.choice(num)
    correct = ""
    if str(diceNum) == numberWord:
        correct = "Correct!"
    else :
        correct = "Incorrect!"
    time.sleep(0.5)
    await ctx.send(f'You are {correct}\n{numberWord} was the answer!')

# Slap command

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slap(ctx,user):
    if str(user) == "@everyone":
        await ctx.message.add_reaction('🤔')
        return

    slap  = random.choice(slapGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Slap Command",value = f'**{ctx.author.mention} slapped {user}!** :rage:')
    em.set_image(url = slap)
    await ctx.send(embed = em)

# Sexy Command
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def sexy(ctx):
    sexy = sexyGifs
    await ctx.send(f'{random.choice(sexy)}' )

# Hug Command

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hug(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return 


    hug  = random.choice(hugGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Hug Command",value = f'**{ctx.author.mention} hugged {user}!**')
    em.set_image(url = hug)
    await ctx.send(embed =em)

# Cuddle Command
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cuddle(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.send(f"Can't do not do that weirdo..." ) 
        return 

    cuddle  = random.choice(cuddleGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Cuddle Command",value = f'**{ctx.author.mention} cuddled with {user}!** :kissing_heart:')
    em.set_image(url = cuddle)
    await ctx.send(embed =em)

# Kiss Command

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kiss(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return


    kiss  = random.choice(kissGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Kiss Command",value = f'**{ctx.author.mention} kissed {user}!** :kissing_heart:')
    em.set_image(url = kiss)
    await ctx.send(embed =em)

# Beaner Command 


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def beaner(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    beaner  = random.choice(beanerGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Beaner Command",value = f'**{ctx.author.mention} called {user} a beaner! :poop:**')
    em.set_image(url = beaner)
    await ctx.send(embed = em)

# Cracker Command 

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cracker(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    cracker  = random.choice(crackerGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Cracker Command",value = f'**{ctx.author.mention} called {user} a cracker!**')
    em.set_image(url = cracker)
    await ctx.send(embed =em)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def chink(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    asian  = random.choice(AsianGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Asian Command",value = f'**{ctx.author.mention} called {user} a chink!**')
    em.set_image(url = asian)
    await ctx.send(embed =em)

# Kill Command

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx,user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    kill  = random.choice(killGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Kill Command",value = f'**{ctx.author.mention} killed {user}! SOMEONE DO SOMETHING!** :eyes:')
    em.set_image(url = kill)
    await ctx.send(embed =em)

# Cry Command

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cry(ctx):
    cry  = random.choice(cryGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Cry Command",value = f'**{ctx.author.mention} is crying!**')
    em.set_image(url = cry)
    await ctx.send(embed =em)

# Fuck You 

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def fu(ctx, user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    fuck  = random.choice(fuckYouGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Fuck You Command",value = f'**{ctx.author.mention} says FUCK YOU to {user}**')
    em.set_image(url = fuck)
    await ctx.send(embed =em)

# NSFW 

nsfwCounter = 0 
apiKey = os.environ['giphyKEY']
api_instance = giphy_client.DefaultApi()
api_response = api_instance.gifs_search_get(apiKey, 'nude girls', limit=50, rating = 'r')
lst = list(api_response.data)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def nsfw(ctx):
    global api_response, lst, nsfwCounter

    if nsfwCounter >= 75: 
        api_response = api_instance.gifs_search_get(apiKey, 'hot girls', limit=50, rating = 'r')
        lst = list(api_response.data)
        nsfwCounter = 0 

    nsfwCounter += 1
    
    gif = random.choice(lst)

    em = discord.Embed(color = discord.Colour.blue(),title = "KevBot NSFW")
    em.set_image(url = f'https://media.giphy.com/media/{gif.id}/giphy.gif')

    await ctx.send(embed = em)

# Shut up

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def shutup(ctx, user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    shutup  = random.choice(shutUpGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"ShutUp Command",value = f'**{ctx.author.mention} told {user} to shut up!**')
    em.set_image(url = shutup)
    await ctx.send(embed =em)

gayMeter = [i for i in range(1,101)]

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def howgay(ctx, user):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return
    em = discord.Embed(colour = discord.Colour.purple())
    em.add_field(name = f"Gay Meter",value = f'{user} is {random.choice(gayMeter)}% gay 🏳️‍🌈!')
    await ctx.send(embed =em)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def edp(ctx, user):
    edp  = random.choice(EDPGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"EDP Command",value = f'**{ctx.author.mention}** says {user} went EDP Mode!')
    em.set_image(url = edp)
    await ctx.send(embed =em)

# Snipe Command - If you see this you a gay ass nigga.

snipe_message_author = {}
snipe_message_content = {}
 
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Sent By {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"There are no deleted messages in #{channel.name}")

# Quick Poll - Coded by Jeremy <333

@client.command()
async def poll(ctx, *, question=None):
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

# Member Join Command

@client.event
async def on_member_join(member):
    guild = client.get_guild(889546253225046049)
    channel = guild.get_channel(889546253975822338)
    await channel.send(f'Welcome to the server {member.mention} ! 🥳 ') 
    await member.send(f'Welcome to the {guild.name} server, {member.name}! 🥳')
    

# Avatar command

@client.command()
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

# Text To Speech

@client.command()
async def test(ctx, *, text):
    await ctx.send(f'{text}', tts=True)

# Server Info Command

@client.command()
async def serverinfo(ctx):
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

client.load_extension('cogs.reddit')
client.load_extension('cogs.HelpCommands')

client.run(os.environ['DISCORD_BOT_TOKEN'])