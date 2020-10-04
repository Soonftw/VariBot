
# -*- coding: utf-8 -*-

# bot.py

import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name} (id: {guild.id})\n"
    )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members: \n - {members}")

@client.event
async def on_member_join(member):
    await member.create_dm
    await member.dem_channel.send(
            f"Hej {member.name}!"
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    quotes = [
            "Life, don't talk to me about life."
            ,
            "Just because you're paranoid doesn't mean that they aren't after you."
            ,
            "I say it's perfectly heartless your eating muffins at all, under the circumstances."
            ]

    if message.content == "test":
        response = random.choice(quotes)
        await message.channel.send(response)
    elif message.content == "raise-exception":
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)
