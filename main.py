import discord
from discord.ext import commands
#from discord import app_commands
import time
import platform
import random
import asyncio
import datetime
import os

from keep_alive import keep_alive
keep_alive()

#=================================================
intents = discord.Intents.all()

client = commands.Bot(command_prefix = commands.when_mentioned_or(">>"),
                      help_command = None,
                      case_insensitive = True,
                      intents = intents,
                      self_bot = True)

#=================================================
TOKEN = os.environ.get('token')

#=================================================
@client.event                                                       #KHOI DONG BOT
async def on_ready():
    print(" ")
    prfx = (time.strftime("%H:%M:%S  ", time.gmtime()))
    print(prfx + "Dang nhap Bot:        " +  client.user.name)
    print(prfx + "Bot ID:               " +  str(client.user.id))
    print(prfx + "Phien  ban discord.py:    " + discord.__version__)
    print(prfx + "Phien ban Python:     " + str(platform.python_version()))
    print(" ")

    id_kenh = 1247080060708585545
    id_server = 1040974953274671205
  
    vc = discord.utils.get(client.get_guild(id_server).channels, id = id_kenh)
    await vc.guild.change_voice_state(channel = vc, self_mute = True, self_deaf = False)

#--------------

#==================================================

#=================================================
client.run(TOKEN, bot = False)
