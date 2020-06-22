import discord
from discord.ext import commands

# Define class Mod(commands.Cog):
class Mod(commands.Mod):
    """kick users command for Mod."""

    def __init__(self, bot):
        self.bot = bot

    @commands.commnd()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked by {ctx.author.mention}.[{reason}]")

def setup(bot):
    bot.add_cog(Mod(bot))
