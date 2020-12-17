import discord
from discord.ext import commands
from discord.ext.commands.core import command

class ChannelAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        '''
        # Allow a user with admin role the ability to create a channel using our bot
        # The bot also needs to have admin role assigned to it.
        # TODO: Assign aixing_bot admin role on server or find minimum permisison
        # TODO: needed to allow it create channels.
        '''
        @bot.command(name='create-channel', help='Create a channel using create-channel followed by channel name')
        @commands.has_role('admin')
        async def create_channel(ctx, channel_name='bot-chat'):
            guild = ctx.guild
            existing_channel = discord.utils.get(guild.channels, name=channel_name)
            if not existing_channel:
                print(f'Creating a new channel: {channel_name}')
                await guild.create_text_channel(channel_name)

        # Add an error check to inform a user if they do not have permisison to run this command.
        # Normally, the error message is not shown to the user so there is no way for them to know why it didn't work
        # This event ensures that they know why.
        @bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.errors.CheckFailure):
                await ctx.send('You do not have the correct role for this command.')


def setup(bot):
    bot.add_cog(ChannelAdmin(bot))
    print('---> Channel Admin LOADED')