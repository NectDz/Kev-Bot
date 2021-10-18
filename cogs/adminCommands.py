import discord
from discord import embeds
from discord.ext import commands
from giphy_client.rest import ApiException

class adminCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
    
        # Mod Commands 

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member,*, reason):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return

        await user.send('You have been kicked from the server!')
        await user.kick(reason =reason)

    # Ban 

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, user: discord.Member,*, reason):
        if str(user) == "@everyone" or str(user) == ctx.author.mention:
            await ctx.message.add_reaction('🤔')
            return


        await ctx.send(f"{user} has been banned by {ctx.author.mention}")
        await user.ban(reason =reason)


    # Clear Command

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clear(self,ctx, amount : int):
        amount += 1

        if amount <= 85: 
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"**{amount-1} message(s) have been deleted!**")
            return 
        else :  
            await ctx.send("That amount is too damn high!")

    # Mute 

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx, member : discord.Member):
        muted_role = ctx.guild.get_role(860677993894903829)

        await member.add_roles(muted_role)

        await ctx.send(member.mention + " has been muted")

    # Unmute

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx, member : discord.Member):
        muted_role = ctx.guild.get_role(860677993894903829)
        await member.remove_role(muted_role)

        await ctx.send(member.mention + " has been unmuted")

def setup(bot):
    bot.add_cog(adminCommands(bot))
