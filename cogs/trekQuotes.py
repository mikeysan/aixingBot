import pathlib
import random
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command


class treky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # This command reads from an external file.
    # It displays random quotes from Star Trek when the $treky command is called
    @commands.command(name='treky', help='Responds with random quote from Star Trek')
    async def treky(self, ctx):
        '''
            Description: Responds with a random quote from star Trek
        '''
        filepath = pathlib.Path(__file__).parent / 'stquotes.txt'
        with open(filepath, "r") as f:
            lines = f.readlines()
            response = random.choice(lines)
        await ctx.send(response)


def setup(bot):
    bot.add_cog(treky(bot))
    print('---> Treky LOADED')