import os
import discord
from discord.ext import commands
import requests
import json

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


class inspired(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        
        msg = ctx.content

        if msg.startswith('$inspired'):
            quote = get_quote()
            await ctx.channel.send(quote)



def setup(bot):
    bot.add_cog(inspired(bot))
    print('---> Inspiration LOADED')