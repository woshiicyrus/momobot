import discord
from discord.ext import commands

import os
import random

client = commands.Bot(command_prefix = 'momo.')
token = "ODQ3MzU0Nzk5NTM1MDMwMzAy.YK82pw.MqKeeiRCjJPVNwzPVaZPxfYtuUk"

channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
gachapons = ['New Leaf City', 'Mushroom Shrine', 'Kerning City', 'Henesys', 'Ellinia', 'Nautilus Harbor', 'Showa Town', 'Perion', 'CBD']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel == "chatting":
            await channel.send(f"Welcome to the server {member.mention}!")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    # Hug
    if message.content.startswith('momo.hug'):
        for user in message.mentions:
            msg = 'Hugs {}'.format(user.mention)
            await message.channel.send(msg)

    # Slap
    elif message.content.startswith('momo.slap'):
        for user in message.mentions:
            msg = 'Slaps {}'.format(user.mention)
            await message.channel.send(msg, file=discord.File('slap.gif'))

    # Taste
    elif message.content.startswith('momo.taste'):
        for user in message.mentions:
            msg = 'Tastes {} {}'.format(user.mention, "dick")
            await message.channel.send(msg)

    await client.process_commands(message)

@client.command()
async def ping(message):
    if str(message.channel) == 'testing-momobot':
        await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def members(message):
    guild_id = client.get_guild(830455873772060722)

    if str(message.channel) == 'testing-momobot':
        await message.channel.send(f'No. of Members: {guild_id.member_count}')

@client.command()
async def fku(message):
    if str(message.channel) == 'testing-momobot':
        await message.channel.send('FK U MOMO NO CHIN CHIN')

@client.command()
async def virgin(message):
    if str(message.channel) == 'testing-momobot':
        await message.channel.send('Jing is virgin')

@client.command()
async def channel(message):
    if str(message.channel) == 'testing-momobot':
        await message.channel.send(f'{message.author.mention}, Channel: {random.choice(channels)} \nDisclaimer: MOMODES will not be held accountable for any bad runs uwu')

@client.command()
async def gacha(message):
    if str(message.channel) == 'testing-momobot':
        await message.channel.send(f'{message.author.mention}, Go play gacha at {random.choice(gachapons)} \nDisclaimer: MOMODES will not be held accountable for any bad runs uwu')

client.run(token)