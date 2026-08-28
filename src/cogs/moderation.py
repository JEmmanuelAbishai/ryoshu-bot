import discord
from discord.ext import commands

from src.core.exceptions import InvalidDurationError
from src.personality.responses import get_response
from src.utils.embeds import error_embed, success_embed
from src.utils.time_parser import parse_duration


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx: commands.Context, count: int) -> None:
        if not 1 <= count <= 100:
            await ctx.send(
                embed=error_embed("Invalid Count. S.A.N. 1-100")
            )
            return

        deleted = await ctx.channel.purge(limit=count + 1)
        actual_count = max(len(deleted) - 1, 0)

        await ctx.send(
            embed=success_embed(
                get_response("purge", count=actual_count)
            )
        )

    @commands.command(name="mute")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def mute(
        self,
        ctx: commands.Context,
        member: discord.Member,
        duration: str
    ) -> None:
        try:
            delta = parse_duration(duration)
        except InvalidDurationError as exc:
            await ctx.send(
                embed=error_embed(str(exc))
            )
            return

        try:
            await member.timeout(
                delta,
                reason=f"Muted by {ctx.author} for {duration}"
            )
        except discord.Forbidden:
            await ctx.send(
                embed=error_embed(
                    get_response("missing_permissions")
                )
            )
            return

        await ctx.send(
            embed=success_embed(
                get_response("mute", member=member.mention)
            )
        )

    @mute.error
    async def mute_error(
        self,
        ctx: commands.Context,
        error: Exception
    ) -> None:
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(
                embed=error_embed(
                    get_response("member_not_found")
                )
            )

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                embed=error_embed(
                    get_response("missing_permissions")
                )
            )

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(
                embed=error_embed(
                    get_response("bot_missing_permissions")
                )
            )

        elif isinstance(error, commands.CommandInvokeError):
            original = error.original

            if isinstance(original, discord.Forbidden):
                await ctx.send(
                    embed=error_embed(
                        get_response("missing_permissions")
                    )
                )
            else:
                raise error

        else:
            raise error

    @commands.command(name="unmute")
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def unmute(
        self,
        ctx: commands.Context,
        member: discord.Member
    ) -> None:
        try:
            await member.timeout(
                None,
                reason=f"Unmuted by {ctx.author}"
            )
        except discord.Forbidden:
            await ctx.send(
                embed=error_embed(
                    get_response("missing_permissions")
                )
            )
            return

        await ctx.send(
            embed=success_embed(
                get_response("unmute", member=member.mention)
            )
        )

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: commands.Context,
        member: discord.Member,
        *,
        reason: str = None
    ) -> None:
        try:
            await member.kick(reason=reason)
        except discord.Forbidden:
            await ctx.send(
                embed=error_embed(
                    get_response("missing_permissions")
                )
            )
            return

        await ctx.send(
            embed=success_embed(
                get_response(
                    "kick",
                    member=member.mention,
                    reason=reason or "No reason provided."
                )
            )
        )

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(
        self,
        ctx: commands.Context,
        member: discord.Member,
        *,
        reason: str = None
    ) -> None:
        try:
            await member.ban(reason=reason)
        except discord.Forbidden:
            await ctx.send(
                embed=error_embed(
                    get_response("missing_permissions")
                )
            )
            return

        await ctx.send(
            embed=success_embed(
                get_response(
                    "ban",
                    member=member.mention,
                    reason=reason or "No reason provided."
                )
            )
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot))
