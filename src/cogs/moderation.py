import discord
from discord.ext import commands

from src.core.exceptions import InvalidDurationError

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx: commands.Context, count: int) -> None:
        if not 1 <= count <= 100:
            await ctx.send(embed=error_embed("Invalid Count. S.A.N. 1-100"))
            return

        deleted = await ctx.channel.purge(limit= count+1)
        actual_count = max(len(deleted) - 1, 0)

        confirmation = await ctx.send(get_response("purge", count=actual_count))
        await confirmation.delete(delay=5)
