"""Informational utility commands: userinfo, avatar, serverinfo."""
import discord
from discord.ext import commands

from src.utils.embeds import info_embed


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None) -> None:
        """Show info about a member. Usage: r!userinfo [@user]"""
        member = member or ctx.author
        embed = info_embed("", title=f"{member}")
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined server", value=discord.utils.format_dt(member.joined_at, "R"), inline=True)
        embed.add_field(name="Account created", value=discord.utils.format_dt(member.created_at, "R"), inline=True)
        embed.add_field(name="Top role", value=member.top_role.mention, inline=True)
        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    async def avatar(self, ctx: commands.Context, member: discord.Member = None) -> None:
        """Show a member's avatar. Usage: r!avatar [@user]"""
        member = member or ctx.author
        embed = info_embed("", title=f"{member}'s avatar")
        embed.set_image(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx: commands.Context) -> None:
        """Show info about this server. Usage: r!serverinfo"""
        guild = ctx.guild
        embed = info_embed("", title=guild.name)
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Created", value=discord.utils.format_dt(guild.created_at, "R"), inline=True)
        embed.add_field(name="Owner", value=str(guild.owner), inline=True)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Utility(bot))
