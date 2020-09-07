import discord 
from discord.ext import commands     

class miky(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def mik(self,ctx):
        await ctx.send("<:DBImikcattivo:712982337536655390>")
        
def setup(bot):
    bot.add_cog(miky(bot))
