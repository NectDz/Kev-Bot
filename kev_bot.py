
import discord
from discord import embeds
from discord.ext import commands
from gifs import cuddleGifs,hugGifs,slapGifs,sexyGifs,kissGifs,beanerGifs,crackerGifs, gmGifs, gnGifs, killGifs, cryGifs, fuckYouGifs, shutUpGifs
from check import checkIfGif
import time, random, os, asyncpraw, giphy_client
from giphy_client.rest import ApiException
memeCounter = 0 

allSubs = []

reddit = asyncpraw.Reddit(client_id = os.environ['clientID'],
                     client_secret = os.environ['clientSecret'],
                     username = os.environ['redditUser'],
                     password = os.environ['redditPass'],
                     user_agent= os.environ['userAgent'])

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


# Meme 

@client.command()
async def meme(ctx):
    global allSubs, memeCounter
    if len(allSubs) == 0 or memeCounter >= 75:
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


# Gaming
gamingList = []
gamingCounter = 0  
@client.command()
async def gaming(ctx):
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

# Help Command

@client.group(invoke_without_command = True)
async def help(ctx):
    
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
async def help2(ctx):    
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
async def help3(ctx):    
    em = discord.Embed(colour = discord.Colour.gold(),title = "Help 3", description = "Use **!kg <command>** to use a command\nDo **!kg help <command>** to see how to use the command")
    em.add_field(name = "**jail**", value = "Puts the user you mentioned in Jail!")
    em.add_field(name = "**howgay**", value = "Tells you how gay the user you mentioned is 🏳️‍🌈")


    em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
    em.set_footer(text=f'Page 3 out of 3')
    await ctx.send(embed = em)

# Mod Commands 

@help.command()
async def mod(ctx):
    em = discord.Embed(colour = discord.Colour.purple(),title = "Mod Commands", description = "Commands **ONLY** Mods can use")

    em.add_field(name = "**clear**", value =f"Deletes the amount of message(s) specified")
    em.add_field(name = "**kick**", value =f"Kicks the user you mentioned and gives a reason")
    em.add_field(name = "**ban**", value =f"Bans the user you mentioned and gives a reason")
    em.add_field(name = "**mute**", value =f"Mutes the user you mentioned and gives a reason")
    em.add_field(name = "**unmute**", value =f"Unmutes the user you mentioned")

    em.set_thumbnail(url = 'https://i.ibb.co/L0czQLQ/Bot-Avatar-2.png')
    em.set_footer(text=f"KevBot Created by NectDzN aka 'KingKev'")
    await ctx.send(embed =em)


# Kick | Needs Client Command

@help.command()
async def kick(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Kick Command", description = "Kicks a member from the server")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} kick <member> [reason]")
    await ctx.send(embed =em)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member,*, reason):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return

    await user.send('You have been kicked from the server!')
    await user.kick(reason =reason)

# Ban 

@help.command()
async def ban(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Ban Command", description = "Ban a member from the server")

    em.add_field(name = "**Syntax**", value =f"{botPrefix} ban <member> [reason]")

    await ctx.send(embed =em)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member,*, reason):
    if str(user) == "@everyone" or str(user) == ctx.author.mention:
        await ctx.message.add_reaction('🤔')
        return


    await ctx.send(f"{user} has been banned by {ctx.author.mention}")
    await user.ban(reason =reason)


# Clear Command

@help.command()
async def clear(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Clear Command", description = "Clears messages from the server")

    em.add_field(name = "**Syntax**", value =f"{botPrefix} clear <amount>")

    await ctx.send(embed =em)

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

@help.command()
async def mute(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Mute Command", description = "Mutes user")

    em.add_field(name = "**Syntax**", value =f"{botPrefix} mute @<user>")

    await ctx.send(embed =em)

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(860677993894903829)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

# Unmute

@help.command()
async def unmute(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "UnMute Command", description = "UnMutes user")

    em.add_field(name = "**Syntax**", value =f"{botPrefix} unmute @<user>")

    await ctx.send(embed =em)

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
async def best(ctx,member):
    await ctx.send(f'{member} is the best!')

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

@help.command()
async def hug(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Hug Command", description = "Hugs a user you mention ")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} hug @<member>")
    await ctx.send(embed =em)

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

@help.command()
async def kiss(ctx):
    em = discord.Embed(colour = discord.Colour.gold(),title = "Kiss Command", description = f"{botPrefix} kiss @<member>")
    await ctx.send(embed =em)

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

@help.command()
async def beaner(ctx):
    em = discord.Embed(colour = discord.Colour.gold(),title = "Beaner Command", description = f"{botPrefix} beaner @<member>")
    await ctx.send(embed =em)

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

@help.command()
async def cracker(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Cracker Command", description = "Calls the person you mentioned a Cracker")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} beaner @<member>")
    await ctx.send(embed =em)

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

# Kill Command

@help.command()
async def kill(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Kill Command", description = "Kills the person you mentioned :eyes:")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} kill @<member>")
    await ctx.send(embed =em)

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

@help.command()
async def cry(ctx):
    em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} cry")
    await ctx.send(embed =em)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cry(ctx):
    cry  = random.choice(cryGifs)
    em = discord.Embed(colour = discord.Colour.red())
    em.add_field(name = f"Cry Command",value = f'**{ctx.author.mention} is crying!**')
    em.set_image(url = cry)
    await ctx.send(embed =em)

# Fuck You 

@help.command()
async def fu(ctx): 
    em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} fu @<member>")
    await ctx.send(embed =em)

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

# NSFW | No Help Command

nsfwCounter = 0 
apiKey = os.environ['giphyKEY']
api_instance = giphy_client.DefaultApi()
api_response = api_instance.gifs_search_get(apiKey, 'hot girls', limit=50, rating = 'r')
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

@help.command()
async def shutup(ctx): 
    em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
    em.add_field(name = "**Syntax**", value =f"{botPrefix} shutup @<member>")
    await ctx.send(embed =em)

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

client.run(os.environ['DISCORD_BOT_TOKEN'])
