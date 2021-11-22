import discord
from discord import embeds
from discord.ext import commands

botPrefix = "!kg "

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
        em.add_field(name = "**snipe**", value = "Snipes messages that have been deleted by someone.")
        em.add_field(name = "**poll**", value = "Makes a poll to let you know what others think!")
        em.add_field(name = "**av**", value = "Shows someones avatar.")


        em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
        em.set_footer(text=f'Page 3 out of 3')
        await ctx.send(embed = em)

    @help.command()
    async def mod(self, ctx):
        em = discord.Embed(colour = discord.Colour.purple(),title = "Mod Commands", description = "Commands **ONLY** Mods can use")

        em.add_field(name = "**clear**", value =f"Deletes the amount of message(s) specified")
        em.add_field(name = "**kick**", value =f"Kicks the user you mentioned and gives a reason")
        em.add_field(name = "**ban**", value =f"Bans the user you mentioned and gives a reason")
        em.add_field(name = "**mute**", value =f"Mutes the user you mentioned and gives a reason")
        em.add_field(name = "**unmute**", value =f"Unmutes the user you mentioned")

        em.set_thumbnail(url = 'https://i.imgur.com/mrwjkRC.png')
        em.set_footer(text=f"KGBot Created by NectDzN aka 'KingKev'")
        await ctx.send(embed =em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Kick Command", description = "Kicks a member from the server")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} kick <member> [reason]")
        await ctx.send(embed =em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Ban Command", description = "Ban a member from the server")

        em.add_field(name = "**Syntax**", value =f"{botPrefix} ban <member> [reason]")

        await ctx.send(embed =em)

    @help.command()
    async def clear(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Clear Command", description = "Clears messages from the server")

        em.add_field(name = "**Syntax**", value =f"{botPrefix} clear <amount>")

        await ctx.send(embed =em)

    @help.command()
    async def mute(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Mute Command", description = "Mutes user")

        em.add_field(name = "**Syntax**", value =f"{botPrefix} mute @<user>")

        await ctx.send(embed =em)

    @help.command()
    async def unmute(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "UnMute Command", description = "UnMutes user")

        em.add_field(name = "**Syntax**", value =f"{botPrefix} unmute @<user>")

        await ctx.send(embed =em)

    @help.command()
    async def hug(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Hug Command", description = "Hugs a user you mention ")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} hug @<member>")
        await ctx.send(embed =em)

    @help.command()
    async def kiss(self,ctx):
        em = discord.Embed(colour = discord.Colour.gold(),title = "Kiss Command", description = f"{botPrefix} kiss @<member>")
        await ctx.send(embed =em)

    @help.command()
    async def kill(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Kill Command", description = "Kills the person you mentioned :eyes:")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} kill @<member>")
        await ctx.send(embed =em)

    @help.command()
    async def cry(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} cry")
        await ctx.send(embed =em)

    @help.command()
    async def fu(self,ctx): 
        em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} fu @<member>")
        await ctx.send(embed =em)

    @help.command()
    async def nsfw(self,ctx): 
        em = discord.Embed(colour = discord.Colour.blue(),title = "NSFW Command", description = "Shows a NSFW photo")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} NSFW")
        await ctx.send(embed =em)

    @help.command()
    async def shutup(self,ctx): 
        em = discord.Embed(colour = discord.Colour.blue(),title = "Cry Command", description = "Shows a crying gif ")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} shutup @<member>")
        await ctx.send(embed =em)

    @help.command()
    async def snipe(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Snipe Command", description = "Snipes messages that have been deleted by someone.")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} snipe")
        await ctx.send(embed =em)
    
    @help.command()
    async def poll(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Poll Command", description = "Makes a poll")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} poll")
        await ctx.send(embed =em)

    @help.command()
    async def av(self,ctx):
        em = discord.Embed(colour = discord.Colour.blue(),title = "Avatar Command", description = "Shows someones avatar.")
        em.add_field(name = "**Syntax**", value =f"{botPrefix} av")
        await ctx.send(embed =em)

def setup(bot):
    bot.add_cog(helpCommands(bot))
