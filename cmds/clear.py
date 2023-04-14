from discord.ext import commands
import main

@commands.command(
  aliases = ['cls'],
  brief=f"{main.prefix}clear liczba - usuwa wszystkie wiadomości z kanału"
)
async def clear(ctx):
  if ctx.author.id == 354712325053218819:
    await ctx.channel.purge()
  else:
    await ctx.author.send("Przykro mi, nie masz uprawnień, żeby użyć tej komendy!")

async def setup(bot):
  bot.add_command(clear)