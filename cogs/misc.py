import discord 
from discord.ext import commands 
import inspect    

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def ping(self, ctx):
        pong = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! {pong}ms:ping_pong:")

    @commands.command(aliases = ["src"])
    async def source(self, ctx, *, command: str = None):
        """Get bot source or source of a command"""

        source_url = 'https://github.com/Discord-Bots-Italia/public-bot-py'
        branch = 'master'

        if command is None:
            return await ctx.send(source_url)

        else:
            obj = self.bot.get_command(command.replace('.', ' '))
            if obj is None:
                return await ctx.send('Could not find command.')

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)
        location = os.path.relpath(filename).replace('\\', '/')

        final_url = f'<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>'
        await ctx.send(final_url)
        
def setup(bot):
    bot.add_cog(Misc(bot))
