import discord
from discord import embeds
from discord.ext import commands
from check import checkIfGif
from giphy_client.rest import ApiException
import asyncio


# Snipe Command - If you see this you a gay ass nigga.

snipe_message_author = {}
snipe_message_content = {}


class eventCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        id = 825096759063216128
        reason = ""

        if member.id == id: 
            await member.ban(reason=reason)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} is gone!.')

    # Hello Event

    @commands.Cog.listener()
    async def on_message(self, message):

        if "img_8905.jpg" in message.content.lower():
            await message.channel.purge(limit=1)

        hellos = ['hi', 'hello', 'HELLO', 'hey', 'heyy', 'heyyy', 'hai', 'sup',
                  'whats up', 'Good Morning', 'GOOD MORNING', 'good morning', 'GoodMorning']

        if message.content.lower() in hellos:
            await message.channel.send(f"Howdy there!")

        if message.content.lower() == "the younger the better":
            await message.channel.send(f"Exactly!")

        no = message.author

    # CoolDowns

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            # isinstance is used to compare 2 thing. If they are the same it returns True in this case were comparing if the error is equal to the other error
            em = discord.Embed(color=discord.Colour.blue(),
                               title="Slow down there partner...", description='The command **{}** is still on cooldown for {:.2f}'.format(ctx.command.name, error.retry_after))
            await ctx.send(embed=em)

    # Commands/Events

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        await asyncio.sleep(60)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]

    @commands.command()
    async def snipe(self, ctx):
        channel = ctx.channel
        try:
            snipeEmbed = discord.Embed(
                title=f"Last deleted message in #{channel.name}", description=snipe_message_content[channel.id])
            snipeEmbed.set_footer(
                text=f"Sent By {snipe_message_author[channel.id]}")
            await ctx.send(embed=snipeEmbed)
        except:
            await ctx.send(f"There are no deleted messages in #{channel.name}")


def setup(bot):
    bot.add_cog(eventCommands(bot))
