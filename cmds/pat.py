from discord.ext import commands
import discord
import random
import gifs
import main

@commands.command(
    brief=f"{main.prefix}pat nickogólnydiscorda - głaszczesz wybranego użytkownika gifem"
  )
async def pat(ctx, user: discord.Member):
  
    embed = discord.Embed(
        title = "",
        description = f"{ctx.author.mention} głaszcze {user.mention} po głowie ^^!",
      #mention to oznaczenie/ping
        color = ctx.author.color
    )

    randomgif = random.choice(gifs.pat)
    embed.set_image(url = randomgif)
    await ctx.send(embed = embed)

async def setup(bot):
  bot.add_command(pat)