import discord
from discord.ext import commands
import aiohttp
import urllib.parse as p
from pyquery import PyQuery as pquery


class Samplasion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, song):
        """Get the lyrics of a song of your choice"""

        song = f'{song}'

        # Start a typing session
        async with ctx.typing():
            # Start a web session
            async with aiohttp.ClientSession() as cs:
                res = await cs.get(f'https://some-random-api.ml/lyrics?title={p.quote(song)}')
                j = await res.json()
                try:
                    author = j['author']
                    title = j['title']
                    lyrics = j['lyrics']
                except KeyError:
                    pass

                try:
                    error = j["error"]
                except KeyError:
                    error = None
                    pass

            await cs.close()

            if error:
                emb = discord.Embed(description=f":x: | An unexpected error occurred\n```{error}```", colour=0x2F3136)
                return await ctx.send(embed=emb)

            for portion in split(f'Lyrics for **{title}** by {author}\n\n{lyrics}'):
                await ctx.send(portion)

    @commands.command(aliases=['hor'])
    async def horoscope(self, ctx, *, sign: str):
        """Get today's horoscope!"""
        
        signs = [
            "aries",
            "taurus",
            "gemini",
            "cancer",
            "leo",
            "virgo",
            "libra",
            "scorpio",
            "sagittarius",
            "capricorn",
            "aquarius",
            "pisces"
        ]
        if sign.lower() not in signs:
            signs = "\n".join(signs)
            emb = discord.Embed(description = f":x: | The sign must be one of these:```{signs}```", colour = 0x2F3136)
            return await ctx.send(embed = emb)

        async with ctx.typing(), aiohttp.ClientSession() as cs:
            res = await cs.get(f'https://www.astrology.com/horoscope/daily/today/{sign.lower()}.html')
            pq = pquery(await res.text())

            text = pq("body > section > section > div.horoscope-main.grid.grid-right-sidebar.primis-rr > main > "
                      "p:nth-child(7)").text()

            await cs.close()

            await ctx.send(text)


def split(text: str, separator="\n"):
    if len(text) <= 2000:
        return [text]

    list = []

    for portion in text.split(separator):
        if len(list) < 1:
            list[0] = portion
        elif len(list[-1] + separator + portion) < 2000:
            list[-1] += separator + portion
        else:
            list.append(separator + portion)

    return list

def setup(bot):
    bot.add_cog(Samplasion(bot))