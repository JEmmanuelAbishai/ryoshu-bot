from discord.ext import commands
#Reusable commands
def guild_only_admin():
    async def predicate(ctx: commands.Context) -> bool:
        return ctx.guild is not None and ctx.author.guild_permissions.administrator
    return commands.check(predicate)
#Prevents LLM spam
def user_cooldown(rate: int = 1, per_seconds: float = 5.0):
    return commands.cooldown(rate, per_seconds, commands.BucketType.user)