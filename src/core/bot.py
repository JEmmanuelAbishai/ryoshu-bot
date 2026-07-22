import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("hello"):
            await message.channel.send("Nice to meet ya I.F.")

    async def on_message_edit(self, before, after):
        if after.author == self.user:
            return
        if before.content == after.content:
            return
        await after.channel.send(
            f" N.F.W {after.author.display_name}"
        )

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('MTUyOTE3MjczNTM0NTgyMzg3NQ.GtwC2J.PQowDS-sdXTlSaH5hsWAwq4zH1PyVXdnKbsW1k')