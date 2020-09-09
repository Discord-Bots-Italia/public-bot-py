import discord, io, functools
from discord.ext import commands  
from PIL import Image   

class chickenmatty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def has_transparency(self, img):
        if img.mode == "P":
            transparent = img.info.get("transparency", -1)
            for _, index in img.getcolors():
                if index == transparent:
                    return True

        elif img.mode == "RGBA":
            extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

        return False


    def coviddi_sync(self, image):
        
        base = Image.open("assets/coviddi.png").resize((500, 500)).convert("RGBA")
        img = Image.open(io.BytesIO(image)).resize((250, 250)).convert("RGBA")
        mask = Image.open("assets/circle-mask.jpg").resize((250, 250)).convert("L")

        transparency = self.has_transparency(img)

        if transparency:
            base.paste(img, (120, 30), img)

        else:
            base.paste(img, (120, 30), mask)

        b = io.BytesIO()
        base.save(b, "png")
        b.seek(0)
        return b

    async def coviddi(self, image):
    
        function = functools.partial(self.coviddi_sync, image)
        img = await self.bot.loop.run_in_executor(None, function)
        return img

    @commands.command()
    async def we(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        bytes = await member.avatar_url_as(format = "png").read()
        bytes = await self.coviddi(bytes)
        file = discord.File(fp = bytes, filename = "coviddi.png")
        await ctx.send("BUONGIORNO DA MONDELLO!!! OGGI AMMARE", file = file)
        
def setup(bot):
    bot.add_cog(chickenmatty(bot))
