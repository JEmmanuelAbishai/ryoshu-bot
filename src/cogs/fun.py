import aiohttp
from discord.ext import commands

from src.utils.embeds import error_embed, gif_embed

GIPHY_SEARCH_URL = "https://api.giphy.com/v1/gifs/search"

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="art")
    async def art(self, ctx: commands.Context, *, query: str) -> None:
        api_key = self.bot.settings.giphy_api_key
        if not api_key:
            await ctx.send(embed=error_embed("No Key?"))
            return

        params = {"api_key": api_key, "q": query, "limit": 1}
        async with aiohttp.ClientSession() as session:
            async with session.get(GIPHY_SEARCH_URL, params = params) as resp:
                if resp.status != 200:
                    await ctx.send(embed = error_embed("Seems like that didn't work"))
                    return
                data = await resp.json()

        results = data.get("data", [])
        if not results:
            await ctx.send(embed=error_embed(f"No GIFs F.F '{query}'."))
            return

        gif_url = results[0]["images"]["original"]["url"]
        await ctx.send(embed = gif_embed(title = query, gif_url = gif_url))

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Fun(bot))