import discord
from discord.ext import commands
#from discord import app_commands
import time
import platform
import random
import asyncio
import datetime
import os

#=================================================
intents = discord.Intents.all()

client = commands.Bot(command_prefix = commands.when_mentioned_or(">>"),
                      help_command = None,
                      case_insensitive = True,
                      intents = intents,
                      self_bot = True)

#=================================================
TOKEN = os.environ.get('token')
arruser = [597843136093487106, 911410904946593823, 227553086909054976]

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

    id_kenh = 1166666665518452868
    id_server = 1164530814281842698

    for guild in client.guilds:
        if guild.voice_client:  # Kiểm tra xem bot có voice client trong guild hay không
            id_kenh = guild.voice_client.channel.id
            break
    if (id_kenh == 1166666665518452868):
        await asyncio.sleep(5.5)
    vc = discord.utils.get(client.get_guild(id_server).channels, id = id_kenh)
    await vc.guild.change_voice_state(channel = vc, self_mute = True, self_deaf = False)

#--------------
@client.event
async def on_message(message):
    if (message.author.id in arruser):
        #s = message.content
        #print(s)
        #------------------------------
        if message.content.startswith('ocurse'):
            await message.channel.send(f"opray <@597843136093487106>")
        #-----------------------------
    await client.process_commands(message)
#==================================================
@client.command(aliases = ["startmessspam"]) #chỉ có acc selfbot mới dùng được lệnh
async def messspamtest(ctx):
    if ctx.channel.id in [1130342854598860801, 1019776265508638750]:
        for i in range (0,1000):
            comment = await ctx.send(f"{i}")
            await asyncio.sleep(1)
            #await (ctx.send(f"{i}")) ---> khong can them cai nay, tu dong co lenh in roi
            emo = ["👍","👎","😀","😊","😙","😎","😔","😕","👆","👇"]
            so = random.randint(1,10)
            for j in range (0,so):
                await (comment.add_reaction(emo[j]))
                await asyncio.sleep(1)

            #if (j < 2):
            #    await asyncio.sleep(0.5)
    else:
        await ctx.send("nothing")
#=================================================
client.run(TOKEN, bot = False)
