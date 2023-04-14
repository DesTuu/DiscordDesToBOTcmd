from discord.ext import commands
import discord
import random
import gifs
import main

@commands.command(
    brief=f"{main.prefix}hug nickogólnydiscorda - przytulasz wybranego użytkownika gifem"
  )
async def hug(ctx, user: discord.Member):
  
    embed = discord.Embed(
        title = "",
        description = f"{ctx.author.mention} przytula {user.mention}!",
      #mention to oznaczenie/ping
        color = ctx.author.color
    )

    randomgif = random.choice(gifs.hug)
    embed.set_image(url = randomgif)
    await ctx.send(embed = embed)

async def setup(bot):
  bot.add_command(hug)