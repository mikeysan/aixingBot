# aixingBot
 A Python based Discord Bot.
 
[![built-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/mikeysan/)
<p>
<a href="https://raw.githubusercontent.com/Py-Contributors/awesomeScripts/master/LICENSE"><img src="https://img.shields.io/github/license/Py-Contributors/awesomeScripts?style=for-the-badge" alt="MIT license"></a>
<a href="https://discord.gg/jTzGuYx"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
</p>
 
 This is very much still a work in progress as it has been developed primarily as a learning tool (there is no harm in coming up with cool features and improvement, though).

## Thinking of contributing?

Please create an issue first detailing what features or improvements you wish to make. We would also ask that you please stick to the [PEP8 style guild](https://pep8.org/) in your coding; e.g.
- DO ``` def something(arg1, arg2) ``` vs 
- DO NOT ``` def something(arg1,arg2) ```
- DO ``` users = something ``` vs 
- DO NOT ``` users=something ```




NOTE- It is recommended that you add your own discord token while running the bot.

- To test the bot you will also need Admin access to a discord server. 

## Hosting the bot on your own machine:
- NOTE: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our the py-awesomescripts server).
- Clone this repo using `git clone`
- cd into the bot folder.
- You'll need to set an environment variable DISCORD_BOT_TOKEN and set it equal to your token.
  (You can make env variables by adding `export GITHUB_BOT_TOKEN = "<TOKEN>"` to your .bashrc/.bash_profile/.zshrc/.sh conf)
  Alternatively comment out the TOKEN import and set it to your own token.
- Install discord.py module:
  ```
    python -m pip install discord.py
  ```
- Install requirements from requirements.txt
  ```
    pip install -r requirements.txt
  ```
- Run the bot using: `python aixingBot.py`
- Enjoy! (don't forget to add your own bot into your discord server by generating an invite link from the discord developers application page in [OAuth2 section](https://discord.com/developers/applications/) and choose application and check Oauth2 section)


## Requirements:
- python 3
- discord(rewrite branch)
- asyncio(inbuilt with python3.4)
- python-dotenv

(note this updated README is inspired by [vyvy-vi](https://github.com/Vyvy-vi/) who also has a Python based Discord Bot.
