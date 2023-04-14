from discord.ext import commands
import main

@commands.command(
    name = 'survey',
    aliases = ['s'],
    brief=f"{main.prefix}survey treśćankiety - niech zagłosują za lub przeciw w ankiecie",
    help='this is help',
    description='this is desc',
    enabled=True,
    hidden=False,
  )
async def survey(ctx, *message):
    message = await ctx.send(" ".join(message))
    await ctx.message.delete()
    await message.add_reaction("\U00002705")
    await message.add_reaction("\U0000274c")

async def setup(bot):
  bot.add_command(survey)