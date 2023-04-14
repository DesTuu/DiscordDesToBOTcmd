from discord.ext import commands
import discord
import main

@commands.command(
    brief=f"{main.prefix}joined nickname - kiedy dany użytkownik dołączył na serwer"
  )
async def joined(ctx, who:discord.Member):
    m = str(who.joined_at)[:19]
    await ctx.send(f"Użytkownik dołączył na serwer: {m}")

async def setup(bot):
  bot.add_command(joined)