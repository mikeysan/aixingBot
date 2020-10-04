import asyncio
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import bot


class remindMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
    @commands.bot_has_permissions(attach_files = True, embed_links = True)
    async def reminder(ctx, time, *, reminder):
        print(time)
        print(reminder)
        user = ctx.message.author
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
        embed.set_footer(text="If you have any questions, suggestions or bug reports, please join our support Discord Server: link hidden", icon_url=f"{bot.user.avatar_url}")
        seconds = 0
        counter = 0
        if reminder is None:
            embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds == 0:
            embed.add_field(name='Warning',
                            value='Please specify a proper duration, send `reminder_help` for more information.')
        elif seconds < 300:
            embed.add_field(name='Warning',
                            value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
        elif seconds > 7776000:
            embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
        else:
            await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
            await asyncio.sleep(seconds)



def setup(bot):
    bot.add_cog(remindMe(bot))
    print('---> REMINDME LOADED')