import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(ctx, user:discord.User, * ,reason):
        if ctx.author.id == 666578281142812673:
            await ctx.message.delete()
            warning = discord.Embed(title="", description=f"{user.mention} has been warned | {reason}", color=0xFF0000)
            await ctx.send(embed=warning)
            await user.send(f"You were warned in {ctx.guild.name}\n reason : {reason}")
            


    @commands.command()
    async def announce(ctx, *, msg):
        members = ctx.guild.members
        if ctx.message.author.guild_permissions.administrator:
            for user in members:
                print(user)
                try:
                    if not user.bot:
                        await user.send(msg)
                except:
                    await ctx.send(f"could not send to {user.mention}")
        else :
            await ctx.send(f"{members.mention} you are not permited to use that command")
        
        
    @commands.command()
    async def dm(ctx, user:discord.User, *, msg):
        if ctx.message.author.guild_permissions.administrator:
            try:
                await user.send(msg)
            except Exception as e:
                await ctx.send(f"could not to send to {user.mention}")
                await ctx.send(f"||{e}||")
        else:
            await ctx.send(f"{ctx.message.author.mention} you are not permited to use that command")
            
    @commands.command()
    async def ban(ctx, user:discord.User=None, reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            if reason == None:
                reason = "An admin found your conduct goes against the benefit of our community!"
            if user == None:
                await ctx.send(f"Who do you want to ban?")
                return
            try:
                await user.send(f'you have been banned from **{ctx.guild}**\nReason : **{reason}**')
                await ctx.guild.ban(user, delete_message_days = 0, reason=reason)
                await ctx.send(f"{user.mention} has been banned")
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you are not permited to use that command")
        
    @commands.command()
    async def kickout(ctx, user:discord.User=None ,reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            if reason == None:
                reason = "For conduct unbecoming of a member of our community!"
            if user == None:
                await ctx.send(f"Who do you want to kick?")
                return
            try:
                await user.send(f'you have been kicked from **{ctx.guild}**\nReason : **{reason}**')
                await ctx.guild.kick(user,reason=reason)
                await ctx.send(f"{user.mention} has been kicked")
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you are not permited to use that command")
        
        
    @commands.command()
    async def unban(ctx, member=None, reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            if reason == None:
                reason = "Someone likes you!"
            if member == None:
                await ctx.send(f"Who would you like to unban?\nType in their ``username#id``")
                return
            try:
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user,reason=reason)
                        await ctx.send(f"{user.mention} has been unbanned")
                        await user.send(f'you have been unbanned from **{ctx.guild}**\nReason : **{reason}**')
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you are not permited to use that command")
            
def setup(bot):
    bot.add_cog(Moderation(bot))
    print('---> MODERATION LOADED')
