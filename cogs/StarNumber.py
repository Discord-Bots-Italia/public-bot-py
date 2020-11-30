  
import discord 
from discord.ext import commands     

class Starnumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def destroyer(self, ctx, *, user: discord.User):
        await ctx.send(str(user) + ', sei stato ucciso da ' + str(ctx.author))
        
def setup(bot):
    bot.add_cog(Starnumber(bot))
