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


class inspired:
    def __init__(self, bot):
        self.bot = bot
    
    
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        msg = message.content

        if msg.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)



def setup(bot):
    bot.add_cog(inspired(bot))
    print('---> Inspiration LOADED')