from discord.ext import commands
import discord
import random
import gifs
import main

@commands.command(
    brief=f"{main.prefix}slap nickogólnydiscorda - uderzasz wybranego użytkownika gifem"
  )
async def slap(ctx, user: discord.Member):
  
    embed = discord.Embed(
        title = "",
        description = f"{ctx.author.mention} uderza {user.mention} prosto w twarz!",
      #mention to oznaczenie/ping
        color = ctx.author.color
    )

    randomgif = random.choice(gifs.slap)
    embed.set_image(url = randomgif)
    await ctx.send(embed = embed)

async def setup(bot):
  bot.add_command(slap)