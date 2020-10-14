#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import os
import datetime
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()

#Environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
#GUILD = os.getenv("DISCORD_GUILD")
GUILD = os.getenv("TEST_GUILD")
#CHANNEL = os.getenv("STD_CHANNEL_ID")
CHANNEL = os.getenv("TEST_CHANNEL")
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

#Bot commands
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    members = '\n - '.join([member.display_name for member in guild.members])
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("World of Warcraft"))
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'Guild Members:\n - {members}'
    )

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice :int, number_of_sides :int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name="attendance", help="Records attending students.")
async def att(ctx):
    #Kolla hur ctx fungerar
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    members = '\n'.join([member.display_name for member in guild.members])
    channel = ctx.channel
    date = str(datetime.datetime.today()).split(" ")[0]
    fileName = "attendance_"+date+".txt"

    await channel.send("Närvarande är: \n"+members)
    f = open(fileName, 'w')
    f.write(members)
    f.close

bot.run(TOKEN)
