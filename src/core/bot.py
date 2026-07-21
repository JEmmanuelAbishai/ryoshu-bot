import discord

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

intents = discord.Intents.default()
intents.message_content = True

client = client(intents=intents)
client.run('MTUyOTE3MjczNTM0NTgyMzg3NQ.GQyICl.JrOlwnkmHHLj_2E5qIwVTagDhKukY_Ekt6SUyc')