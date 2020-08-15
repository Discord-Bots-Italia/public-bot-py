import discord, random
from discord.ext import commands     

class Rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.command()
    async def rps(self, ctx):           
        moves = ["rock", "paper", "scissors"]
        e = discord.Embed(
            title="Let's play some R-P-S!",
            colour=0x5FB49C
        ).add_field(name="Start", value="React to start playing.", inline=False)
        
        msg = await ctx.send(embed=e)
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'  

        await msg.add_reaction(emoji='✅')
        reaction, _ = await self.bot.wait_for("reaction_add", check=check)
        if reaction.emoji == '✅':
            bot_move = random.choice(moves)
            while True:
                await ctx.send("Choose one of the following moves:\n Rock\n Paper\n Scissors\n and write it.")
                def checkmsg(m):
                    return m.content.lower() in moves
                user_move = await self.bot.wait_for("message", check=checkmsg)
                user_move = user_move.content.lower()
                if user_move in moves:
                    await ctx.send(f"Ok! I choose... {bot_move}!")
                    if user_move == "rock" and bot_move == "paper" or user_move == "scissors" and bot_move == "rock" or user_move == "paper" and bot_move == "scissors":
                        await ctx.send("I win.")
                    elif user_move == "paper" and bot_move == "rock" or user_move == "rock" and bot_move == "scissors" or user_move == "scissors" and bot_move == "paper":
                        await ctx.send("You win.")
                    else:
                        await ctx.send("It's a draw.")
                    break
                    
                else:
                    await ctx.send(f"That move doesn't exist!")
                    continue
            
        
def setup(bot):
    bot.add_cog(Rps(bot))
