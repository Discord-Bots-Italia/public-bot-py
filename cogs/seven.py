import discord 
from discord.ext import commands

class Seven(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.guild:

            if message.channel.id == 846125144376082502:  # datamining
                await message.publish()

def setup(bot):
    bot.add_cog(Seven(bot))
