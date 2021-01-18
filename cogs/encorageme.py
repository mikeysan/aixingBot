from discord import message
from discord.ext import commands
import random
import os
import redis

r = redis.from_url(os.environ.get("REDIS_URL"))

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

def update_encouragements(encouraging_message):
    if "encouragements" in r.keys():
        encouragements = r["encouragements"]
        encouragements.append(encouraging_message)
        r["encouragrments"] = encouragements
    else:
        r["encouragements"] = encouraging_message
        

def delete_encouragements(index):
    encouragements = r["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        r["encouragements"] = encouragements


class encourage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,ctx):
        '''
           Check if any of the words the users typed is part of
           our sad_words list.
        '''

        options = starter_encouragements
        if "encouragements" in r.keys():
            options = options + r["encouragements"]
        
        if any(word in ctx.content for word in sad_words):
            # Send a word of encouragement if needed
            await ctx.channel.send(random.choice(options))
        
        if ctx.content.startswith("$new"):
            encouraging_message = ctx.content.split("$new ", 1)[1]
            update_encouragements(encouraging_message)
            await ctx.channel.send("New encouraging message added")
        
        if ctx.content.startswith("$del"):
            encouragements = []
            if "encouragements" in r.keys():
                index = int(ctx.content.split("$del",1)[1])
                delete_encouragements(index)
                encouragements = r["encouragements"]
                await ctx.channel.send(encouragements)





        

def setup(bot):
    bot.add_cog(encourage(bot))
    print('---> Encouragements LOADED')