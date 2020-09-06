import discord
from discord.ext import commands
import aiohttp
import urllib.parse as p


class Samplasion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *, song):
        """Get the lyrics for a song of your choice"""

        song = f'{song}'

        # Start a typing session
        async with ctx.typing():
            # Start a web session
            async with aiohttp.ClientSession() as cs:
                res = await cs.get(f'https://some-random-api.ml/lyrics?title={p.quote(song)}')
                j = await res.json()
                author = j['author']
                title = j['title']
                lyrics = j['lyrics']

            for portion in split(f'Lyrics for **{title}** by {author}\n\n{lyrics}'):
                await ctx.send(portion)


def split(text: str, separator="\n"):
    if len(text) <= 2000:
        return [text]

    list = []

    for portion in text.split(separator):
        if len(list) == 0:
            list[0] = portion
        elif len(list[-1] + separator + portion) < 2000:
            list[-1] += separator + portion
        else:
            list.append(separator + portion)

    return list


def setup(bot):
    bot.add_cog(Samplasion(bot))
