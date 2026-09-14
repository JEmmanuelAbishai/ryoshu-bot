import aiohttp
from discord.ext import commands

from src.utils.embeds import error_embed, gif_embed

TENOR_SEARCH_URL = "https://tenor.googleapis.com/v2/search"


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="art")
    async def art(self, ctx: commands.Context, *, query: str) -> None:
        
        api_key = self.bot.settings.tenor_api_key
        if not api_key:
            await ctx.send(embed=error_embed("No key? F.I."))
            return

        params = {"q": query, "key": api_key, "limit": 1, "media_filter": "gif"}
        async with aiohttp.ClientSession() as session:
            async with session.get(TENOR_SEARCH_URL, params=params) as resp:
                if resp.status != 200:
                    await ctx.send(embed=error_embed("Seems like that doesnt work."))
                    return
                data = await resp.json()

        results = data.get("results", [])
        if not results:
            await ctx.send(embed=error_embed(f"No GIFs found for '{query}'."))
            return

        gif_url = results[0]["media_formats"]["gif"]["url"]
        await ctx.send(embed=gif_embed(title=query, gif_url=gif_url))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Fun(bot))
