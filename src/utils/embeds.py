import discord

COLOR_SUCCESS = discord.Color.green()   
COLOR_ERROR = discord.Color.red()
COLOR_INFO = discord.Color.blue()
COLOR_RYOSHU = 0xCF0000

def success_embed(description: str, title: str = None) -> discord.Embed:
    embed = discord.Embed(description=description, color=COLOR_RYOSHU)
    if title:
        embed.title = title
    return embed

def error_embed(description: str, title: str = None) -> discord.Embed:
    embed = discord.Embed(description=description, color=COLOR_RYOSHU)
    if title:
        embed.title = title
    return embed

def info_embed(description: str, title: str = None) -> discord.Embed:
    embed = discord.Embed(description=description, color=COLOR_RYOSHU)
    if title:
        embed.title = title
    return embed

def gif_embed(title: str, gif_url: str, source_url: str = None) -> discord.Embed:
    embed = discord.Embed(title=title, color=COLOR_RYOSHU)
    embed.set_image(url=gif_url)
    if source_url:
        embed.url = source_url
    return embed