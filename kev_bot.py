
import discord
from discord import embeds
from discord.ext import commands
import os

botPrefix = "!kg "

client = commands.Bot(command_prefix= botPrefix, case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!kg help'))
    print("Bot is ready!")

client.remove_command('help')

client.load_extension('cogs.eventCommands')
client.load_extension('cogs.adminCommands')
client.load_extension('cogs.misc')
client.load_extension('cogs.reddit')
client.load_extension('cogs.HelpCommands')

client.run(os.environ['DISCORD_BOT_TOKEN'])