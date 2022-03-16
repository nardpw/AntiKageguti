import discord
import json

with open('config.json', encoding='utf-8') as f:
        config = json.load(f)

class AntiKageguti(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        for w in config['words']:
            if w in message.content:
                f = open('log.txt', 'a')
                f.write(f"From {message.author} {message.content}\n")
                f.close()
                print("Success")
                break

client = AntiKageguti()
client.run(config["token"])