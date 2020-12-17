import os
import random
from discord.ext import commands
from discord.ext.commands import bot


class treky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # This command reads from an external file.
        # It displays random quotes from Star Trek when the $treky command is called
        @bot.command(name='treky', help='Responds with random quote from Star Trek')
        async def treky(ctx):
            '''
                Description: Responds with a random quote from star Trek
            '''
            with open("stquotes.txt", "r") as f:
                lines = f.readlines()
                response = random.choice(lines)
            await ctx.send(response)


def setup(bot):
    bot.add_cog(treky(bot))
    print('---> Treky LOADED')