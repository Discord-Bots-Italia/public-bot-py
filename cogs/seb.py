import discord 
from discord.ext import commands     

class Sebastiano(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        "hug someone"
        if member == ctx.author:
            return await ctx.send("lmao imagine hugging yourself")

        f = discord.File(fp = "assets/hug.gif")

        await ctx.send(f"**{ctx.author.display_name}** hugged **{member.display_name}**", allowed_mentions = discord.AllowedMentions(users = False, roles = False, everyone = False), file = f)
        
def setup(bot):
    bot.add_cog(Misc(bot))
