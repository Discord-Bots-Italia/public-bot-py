import discord 
from discord.ext import commands 
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path = ".env")

bot = commands.Bot(command_prefix = commands.when_mentioned_or("py "), case_insensitive = True)
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print("ready as", bot.user)

for a in os.listdir("./cogs"):
    if a.endswith(".py"):
        bot.load_extension(f"cogs.{a[:-3]}")

token = os.environ.get("token")
bot.run(token)
