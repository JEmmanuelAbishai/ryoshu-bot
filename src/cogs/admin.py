from discord.ext import commands
from src.utils.decorators import guild_only__admin

class Admin(commands.Cog):
    def _init_(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="reload")
    @guild_only__admin()
    async def reload(self, ctx: commands.Context, cog: str) -> None:
        extension = f"src.cogs.{cog}"
        try:
            await self.bot.reload_extension(extension)
        except Exception as exc:
            await ctx.send(f"Failed to reload `{cog}` : {exc}")
            return
        await ctx.send(f"Reloaded `{cog}` successfully.")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))