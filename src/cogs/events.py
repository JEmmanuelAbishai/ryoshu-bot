"""Global event listeners: error handling, member join greetings, ready message."""
import discord
from discord.ext import commands
from loguru import logger

from src.personality.responses import get_response
from src.utils.embeds import error_embed


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        logger.info(get_response("on_ready"))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        channel = member.guild.system_channel
        if channel:
            await channel.send(get_response("on_member_join", member=member.mention))

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=error_embed(get_response("missing_permissions")))
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=error_embed(get_response("bot_missing_permissions")))
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=error_embed(get_response("member_not_found")))
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=error_embed(get_response("bad_argument")))
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=error_embed(get_response("cooldown")))
        elif isinstance(error, commands.CommandNotFound):
            return  # silently ignore unknown commands
        else:
            logger.exception("Unhandled command error", exc_info=error)
            await ctx.send(embed=error_embed(get_response("generic_error")))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Events(bot))
