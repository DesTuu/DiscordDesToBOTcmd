from bs4 import BeautifulSoup
import requests
from discord.ext import commands
import main
import discord

@commands.command(
    aliases = ['p'],
    brief=f"{main.prefix}patch - dokładna data ostatniego patcha w LoLu",
  )
async def patch(ctx):
  url= f"https://www.leagueoflegends.com/pl-pl/news/tags/patch-notes/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  
  date = soup.find(class_="style__Time-sc-10dp7mx-0 kJsMQd style__TimeAgo-sc-1h41bzo-12 bAijJH")
  date = str(date)
  
  if "datetime" in date:
      idx = date.index("datetime")
      idx += 10
      idx_end = idx + 10
      r = (date[idx:idx_end])

  x = soup.body.find('h2').text
  x = str(x).replace("Opis patcha", "").replace(" ", "-").replace(".", "-")
  x += "-notes/"
  
  patch_url = f"https://www.leagueoflegends.com/pl-pl/news/game-updates/patch{x}"
  patch_response = requests.get(patch_url)
  patch_soup = BeautifulSoup(patch_response.text, 'lxml')
  y = patch_soup.body.div.div.div.find(class_="skins cboxElement")
  y = y.findAll('img')
  
  chars = ['[', ']', '<', '"', '/>', 'img src=']
  for char in chars:
      y = str(y).replace(char, '')
  
  embed = discord.Embed(
        title = "",
        description = f"Ostatni patch w LoLu był dnia: {r} \n Ostatnie patche: https://www.leagueoflegends.com/pl-pl/news/tags/patch-notes/ \n Ostatni patch: {patch_url} \n Skrót patcha, kliknij w obrazek, aby powiększyć: ",
        color = ctx.author.color
    )

  embed.set_image(url = y)
  await ctx.send(embed = embed)

async def setup(bot):
  bot.add_command(patch)