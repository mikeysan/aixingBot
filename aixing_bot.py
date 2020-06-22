# aixing_bot.py
# A discord bot created by Mikey San
# This is mostly a tutorial project for use on my discord server.

import os
import random
import datetime

import discord
from discord.ext import commands
from discord import activity, message

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

import logging

# Setup logging to a file called discord.log.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# We are using the Bot API to interact with discord.
# Assign "bot" to commands.Bot and set the commnd prefix to look for.
# We have also set our commands to be case insensitive. this means $help or
# $Help or even $helP will trigger the bot.
bot = commands.Bot(command_prefix='$', description="A support Bot for NLB Clan", case_insensitive=True)

# Create an event that takes the on_ready function
# This will do a few things once our bot goes live
@bot.event
async def on_ready():
    # Check that we are in the expected server.
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    # Print to terminal (log file) when we make a connection.
    # Also confirm the server name and ID we're connected to.
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # Send a message to the channel "chat" once we are connected.
    # So we can see that we are live there too.
    channel = discord.utils.get(guild.channels, name="chat")
    wave = ":wave:"
    # Let's pretend the bot is playing the game of $help
    # # TODO: Add a help function that displays all the other commands available
    game = discord.Game(name = "$help")
    await bot.change_presence(activity = game)

    # Create a discord embed instance.
    # Set title, colour and timestamp. ps. don't forget to import datetime module
    embed = discord.Embed(
        title = f"{bot.user.name} Online!",
        colour = discord.Colour.from_rgb(255,191,0),
        url = "https://github.com/mikeysan/aixingBot",
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    # Set a footer using the embed instance.
    embed.set_footer(
        text = "I am Open Source. I am Skynet."
    )
    # Send our embeded content to the channel.
    await channel.send(embed = embed)


# Allow a user with admin role the ability to create a channel using our bot
# The bot also needs to have admin role assigned to it.
# TODO: Assign aixing_bot admin role on server or find minimum permisison
# TODO: needed to allow it create channels.
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


# This command reads from an external file.
# It displays random quotes from Star Trek when the $treky command is called
@bot.command(name='treky', help='Responds with random quote from Star Trek')
async def treky(ctx):
    with open("stquotes.txt", "r") as f:
        lines = f.readlines()
        response = random.choice(lines)
    await ctx.send(response)

# Reload cogs
@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.unload_extensions(f"cogs.{cog}")
        bot.load_extensions(f"cogs.{cog}")
        ctx.send(f"{cog} reloaded successfully")
    except Exception as e:
        print(f"{cog} can not be loaded:")
        raise e

# Load cogs
for cog in os.listdir(".\/cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

# Finally, authenticate with discord and let's get cracking.
bot.run(TOKEN)
