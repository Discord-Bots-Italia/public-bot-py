import discord 
from discord.ext import commands     

class chickenmatty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def we(self,ctx):
        await ctx.send("BUONGIORNO DA MONDELLO!!! OGGI AMMARE")
        
def setup(bot):
    bot.add_cog(chickenmatty(bot))
