import jokes
from discord.ext import commands
import random
import main

@commands.command(
    aliases = ['jk'],
    brief=f"{main.prefix}joke - losuje Ci żart",
    help='this is help',
    description='this is desc',
  )
async def joke(ctx):
    r = random.choice(jokes.jokes)
    await ctx.send(r)

async def setup(bot):
  bot.add_command(joke)