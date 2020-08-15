import discord 
from discord.ext import commands     

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def ping(self, ctx):
        pong = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! {pong}ms:ping_pong:")

    @commands.command(aliases = ["src"])
    async def source(self, ctx):
        await ctx.send("https://github.com/Discord-Bots-Italia/public-bot-py")
        
def setup(bot):
    bot.add_cog(Misc(bot))
