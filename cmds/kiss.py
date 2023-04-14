from discord.ext import commands
import discord
import random
import gifs
import main

@commands.command(
    brief=f"{main.prefix}kiss nickogólnydiscorda - całujesz wybranego użytkownika gifem"
  )
async def kiss(ctx, user: discord.Member):
  
    embed = discord.Embed(
        title = "",
        description = f"{ctx.author.mention} całuje {user.mention} prosto w usta!",
      #mention to oznaczenie/ping
        color = ctx.author.color
    )

    randomgif = random.choice(gifs.kiss)
    embed.set_image(url = randomgif)
    await ctx.send(embed = embed)

async def setup(bot):
  bot.add_command(kiss)