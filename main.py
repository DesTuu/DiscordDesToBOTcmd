import discord
from discord.ext import commands, tasks
import settings
import keep_alive
import requests
from bs4 import BeautifulSoup

logger = settings.logging.getLogger('bot')

prefix = "!"

def run():
  intents = discord.Intents().all()
  intents.message_content = True
  bot = commands.Bot(command_prefix=prefix, intents=intents, activity=discord.Game(name='!help'))

  @bot.event
  async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    for cmd_file in settings.CMD_DIR.glob('*.py'):
      if cmd_file.name != '__init__.py':
        await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    task_loop.start()

  @tasks.loop(seconds=1800)
  async def task_loop():
    auto_url = "https://www.leagueoflegends.com/pl-pl/news/tags/patch-notes/"
    auto_response = requests.get(auto_url)
    auto_soup = BeautifulSoup(auto_response.text, 'lxml')
    auto_match = auto_soup.find('div', attrs={'class':'style__ImageWrapper-sc-1h41bzo-5 bxstMo'})
    auto_src = auto_match.img['src']
    
    with open("old_patch.txt") as auto_r:
        auto_patch_url = auto_r.readlines()

    auto_channel = bot.get_channel(1084864375816458300)
    if "".join(auto_patch_url) == auto_src:
        pass
    else:
        await auto_channel.send("**Właśnie wyszedł nowy patch w LoLu!:**\nhttps://www.leagueoflegends.com/pl-pl/news/tags/patch-notes/\n**Możesz też wpisać komendę !patch by dowiedzieć się więcej!**")
        with open("old_patch.txt", "w") as auto_f:
            auto_f.write(auto_src)
  
  keep_alive.keep_alive()
  
  bot.run(settings.MY_SECRET, root_logger=True)

if __name__ == "__main__":
  run()