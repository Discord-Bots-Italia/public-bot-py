import discord
from discord.ext import commands 
import random

class HelpCommand:
    def __init__(self, bot):
        self.bot = bot

    async def command_list(self, ctx):
        "return the commands list"
        emb = discord.Embed(title = "Help", description = "", colour = discord.Colour.from_hsv(random.random(), 1, 1), timestamp = ctx.message.created_at)
        emb.set_author(name = ctx.author, icon_url = str(ctx.author.avatar_url_as(static_format = "png")))
        #emb.set_thumbnail(url = str(self.bot.user.avatar_url_as(static_format = "png")))

        for cog in self.bot.cogs:
            cog_str = ""
            cog = self.bot.get_cog(cog)
            commands = cog.get_commands()
            commands = [cmd for cmd in commands if not cmd.hidden]

            if len(commands) >= 1:
                for command in commands:
                    cog_str += f"{self.bot.clean_prefix}{command.name} {command.signature}\n" if command.signature else f"{self.bot.clean_prefix}{command.name}\n" 

                emb.add_field(name = cog.qualified_name, value = f"```prolog\n{cog_str}\n```")
        
        return await ctx.send(embed = emb)

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        self.help = HelpCommand(bot)
        bot.help_command = None

    @commands.command(hidden = True)
    async def help(self, ctx):
        await self.help.command_list(ctx)

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

def setup(bot):
    bot.add_cog(Help(bot))