import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
from cogs.words import MyList
from cogs.words import words
import string
# from time import sleep as delay


# Get words list from MyList class in words.py file
word_list = MyList()
# Put list items from words into class list items
for word in words:
    word_list.addWords(word)

allWords = word_list.wordsList


def get_valid_word(allWords):
        word = random.choice(allWords)  # randomly chooses something from the list
        while '-' in word or ' ' in word:
            word = random.choice(allWords)

        return word.upper()



class hangmanGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #   Hangman Game
    @commands.command(name='Hangman', help='Play Hangman')
    async def hangman(self, ctx):
        word = get_valid_word(allWords)
        word_letters = set(word)  # letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  # what the user has guessed

        lives = 6

        # getting user input
        while len(word_letters) > 0 and lives > 0:
            # letters used
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
            spc = ' '
            await ctx.send(f'You have {lives} lives left and you have used these letters: {spc.join(used_letters)}')

            # what current word is (ie W - R D)
            word_list = [letter if letter in used_letters else '-' for letter in word]
            await ctx.send(f'Current word: {spc.join(word_list)}')

            # user_letter = input('Guess a letter: ').upper()
            await ctx.send('Guess a letter: ')
            user_letter = bot.wait_for('message', check=lambda m: m.user == ctx.user).upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    await ctx.send('')

                else:
                    lives = lives - 1  # takes away a life if wrong
                    await ctx.send('\nYour letter,', user_letter, 'is not in the word.')

            elif user_letter in used_letters:
                await ctx.send('\nYou have already used that letter. Guess another letter.')

            else:
                await ctx.send('\nThat is not a valid letter.')

        # gets here when len(word_letters) == 0 OR when lives == 0
        if lives == 0:
            await ctx.send('You died, sorry. The word was', word)
        else:
            await ctx.send('YAY! You guessed the word', word, '!!')


def setup(bot):
    bot.add_cog(hangmanGame(bot))
    print('---> Hangman LOADED')