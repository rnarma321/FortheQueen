import os
import discord
from discord.ext import tasks
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VERSION = "1.0.0"
DESCRIPTION = "For the Queen, game based upon For the King on Steam"
bot = commands.Bot(command_prefix='!', description=DESCRIPTION, pm_help=True, case_insensitive=True)


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # bot.add_cog(Profile(bot))
    # bot.add_cog(Graphing(bot))
    # bot.add_cog(StockExchange(bot))
    # bot.add_cog(Special(bot))
bot.run(TOKEN)
