import discord 
from discord.ext import commands     
import aiohttp
import io

class Sebastiano(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        "give an hug to someone"
        if member == ctx.author:
            return await ctx.send("lmao imagine hugging yourself")

        f = discord.File(fp = "assets/hug.gif")

        await ctx.send(f"**{ctx.author.display_name}** hugged **{member.display_name}**", allowed_mentions = discord.AllowedMentions(users = False, roles = False, everyone = False), file = f)

    @commands.command()
    async def redpanda(self, ctx):
        "RedPanda owo"

        async with ctx.typing():
            async with aiohttp.ClientSession() as cs:
                res = await cs.get("https://some-random-api.ml/img/red_panda")
                j = await res.json()
                url = j["link"]
                async with cs.get(url) as img:
                    bytes = await img.read()

            await ctx.send(file = discord.File(fp = io.BytesIO(bytes), filename = "redpanda.png"))


def setup(bot):
    bot.add_cog(Sebastiano(bot))
