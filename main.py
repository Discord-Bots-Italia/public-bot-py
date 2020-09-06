import discord 
from discord.ext import commands 
import os 
from dotenv import load_dotenv

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"

load_dotenv(dotenv_path = ".env")

bot = commands.Bot(command_prefix = commands.when_mentioned_or("py "), case_insensitive = True, allowed_mentions = discord.AllowedMentions(everyone=False, roles = False))
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print("ready as", bot.user)

@bot.event 
async def on_command_error(ctx, error):
    emb = discord.Embed(description = f"```\n{error}\n```", colour = 0x2F3136)
    emb.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url_as(static_format = "png")))
    await ctx.send(embed = emb)

for a in os.listdir("./cogs"):
    if a.endswith(".py"):
        bot.load_extension(f"cogs.{a[:-3]}")

token = os.environ.get("token")
bot.run(token)
