import discord 
from discord.ext import commands     

class Zakuren(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def echo(self, ctx, *, msg):
        await ctx.send(msg)
        
def setup(bot):
    bot.add_cog(Zakuren(bot))