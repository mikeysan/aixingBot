from discord import message
from discord.ext import commands
import random


sad_words = [
    "sad",
    "depressed",
    "unhappy",
    "pissed",
    "mad",
    "upset",
    "angry",
    "miserable"
    ]

starter_encouragements = [
    "Cheer up!",
    "You are a great person!",
    "Hang in there!",
    "Act as if what you do makes a difference. It does.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Never bend your head. Always hold it high. Look the world straight in the eye.",
    "Believe you can and you're halfway there."
]

class encourage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,ctx):
        if any(word in ctx.content for word in sad_words):
            await self.bot.send("You said something sad!")
            await ctx.channel.send(random.choice(starter_encouragements))
        
        


def setup(bot):
    bot.add_cog(encourage(bot))
    print('---> Encouragements LOADED')