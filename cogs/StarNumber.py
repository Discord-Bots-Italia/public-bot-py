  
import discord 
from discord.ext import commands     

class Starnumber(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def destroyer(self, ctx, *, user: discord.User):
        await ctx.send(str(user) + ', sei stato ucciso da ' + str(ctx.author))
    @commands.command()
    async def send(self, ctx, user: discord.User):
        await ctx.send("https://tenor.com/view/kick-cartoon-silly-wacky-gif-9316304")
        await ctx,send(f"{user.mention} è stato **lanciato fuori dalla finestra** da {ctx.author.mention}")
def setup(bot):
    bot.add_cog(Starnumber(bot))
