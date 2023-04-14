from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import main
import random
import discord

@commands.command(
  brief=f"{main.prefix}mem - losuje Ci jednego z najnowszych memów"
)
async def mem(ctx):
  A = []
  for site in range(9):
    url = f"https://jbzd.com.pl/str/{site}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    match = soup.findAll('div', attrs={'class':'article-image article-media-image'})
    for i in match:
      try:
        src = i.img['src']
        A.append(src)
      except TypeError:
        pass

  embed = discord.Embed(
    title="",
    description="Oto jeden z najnowszych memów ze strony jbzd.com.pl:",
    color=ctx.author.color
  )

  mem = random.choice(A)
  embed.set_image(url=mem)
  await ctx.send(embed=embed)
  
async def setup(bot):
  bot.add_command(mem)