from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import main

@commands.command(
    aliases = ['$'],
    brief=f"{main.prefix}rate - aktualny kurs waluty euro i dolara",
  )
async def rate(ctx):
  A = []

  url= f"https://www.money.pl/pieniadze/nbp/srednie/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  info = soup.find(class_="sc-1fexh53-1 YpZHd").text
  titles = soup.find_all(class_='rt-tr-group')
  
  for i in titles:
      if 'dolar amerykański' in str(i.text) or 'euroEUR4' in str(i.text):
          A.append(i.text)
  
  usd = A[0][22:26]
  usd = f"4,{usd}"
  
  euro = A[1][9:13]
  euro = f"4,{euro}"

  await ctx.send(f"{info} \n 1 dolar amerykański (USD) = {usd} zł \n 1 euro (€) = {euro} zł")

async def setup(bot):
  bot.add_command(rate)