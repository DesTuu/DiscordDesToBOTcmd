from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import time
import main

@commands.command(
  aliases=['w'],
  brief=f"{main.prefix}weather - pokazuje aktualną pogodę"
)
async def weather(ctx):

  A = []

  url= f"https://pogoda.wp.pl/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  titles = soup.find_all(class_='el temp')
  
  for i in titles:
    if i.text == 'Baboi Leten':
      break
    value = str(i)[52:56].replace('"', '')
    A.append(f"{i.text}: {value} °C\n")

  string = " ".join(A)
  actual_time = time.strftime("%H:%M")
  await ctx.send(f"Pogoda w Polsce o godzinie {actual_time}(UTC Time) : \n\n{string}")

async def setup(bot):
  bot.add_command(weather)