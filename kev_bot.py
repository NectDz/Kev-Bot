
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

# Member Join Command

@client.event
async def on_member_join(member):
    guild = client.get_guild(829751693640990780)
    channel = guild.get_channel(829751693640990783)
    await channel.send(f'Welcome to the server {member.mention} ! 🥳 ') 
    await member.send(f'Welcome to the {guild.name} server, {member.name}! 🥳')

client.load_extension('cogs.reddit')
client.load_extension('cogs.HelpCommands')

client.run(os.environ['DISCORD_BOT_TOKEN'])