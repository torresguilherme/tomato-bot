import discord
from discord.ext import commands
import asyncio
import time
import fileinput
from key import key

bot = commands.Bot(command_prefix = ':>')

@bot.event
async def on_ready():
    print("Bot online!")
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------')

print(key)
bot.run(key)
