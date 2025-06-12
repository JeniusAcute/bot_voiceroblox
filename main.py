import discord
from discord.ext import commands
import os

#=================================================
intents = discord.Intents.all()

client = commands.Bot(command_prefix = commands.when_mentioned_or(">>"),
                      help_command = None,
                      case_insensitive = True,
                      intents = intents,
                      self_bot = True)

#=================================================
TOKEN = os.environ.get("token")

#=================================================
@client.event                                                       #KHOI DONG BOT
async def on_ready():

    print("Done")

    id_kenh = 1247080044816498711
    id_server = 1040974953274671205
    
    vc = discord.utils.get(client.get_guild(id_server).channels, id = id_kenh)
    await vc.guild.change_voice_state(channel = vc, self_mute = True, self_deaf = False)

#--------------

#=================================================
client.run(TOKEN, bot = False)
