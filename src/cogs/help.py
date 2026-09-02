"""Custom help command, written in the bot's voice."""
import random

import discord
from discord.ext import commands

from src.personality.responses import get_response
from src.utils.embeds import info_embed


class CustomHelp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.remove_command("help")  # replace discord.py's default help

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context) -> None:
        """Show all available commands. Usage: r!help"""
        prefix = self.bot.settings.command_prefix
        intro = get_response("help_intro")

        embed = info_embed(intro, title="Commands")
        for cog_name, cog in self.bot.cogs.items():
            cmds = cog.get_commands()
            if not cmds:
                continue
            lines = [f"`{prefix}{c.name}` -- {c.help or 'No description'}" for c in cmds]
            embed.add_field(name=cog_name, value="\n".join(lines), inline=False)

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CustomHelp(bot))
