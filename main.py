import discord
import os
from googletrans import Translator

client = discord.Client()
translator = Translator()

translation_groups = {}
translation_groups['general'] = [837977828808458253, 841313609761816626, 841307528121155594, 842043260109324378, 849642737719967754]
translation_groups['guild_war'] = [839855093905883176, 841313665843462164, 841313365975498763, 842043319978295316, 849642822076596244]
translation_groups['cross_war'] = [840218404198940713, 841313714815893567, 841313415958888468, 842043378257625140, 849642967769808896]

channel_language = {}
channel_language[837977828808458253] = 'en'
channel_language[841313609761816626] = 'ko'
channel_language[841307528121155594] = 'zh-tw'
channel_language[842043260109324378] = 'ja'
channel_language[849642737719967754] = 'pt'
channel_language[839855093905883176] = 'en'
channel_language[841313665843462164] = 'ko'
channel_language[841313365975498763] = 'zh-tw'
channel_language[842043319978295316] = 'ja'
channel_language[849642822076596244] = 'pt'
channel_language[840218404198940713] = 'en'
channel_language[841313714815893567] = 'ko'
channel_language[841313415958888468] = 'zh-tw'
channel_language[842043378257625140] = 'ja'
channel_language[849642967769808896] = 'pt'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for k, v in translation_groups.items():
        if message.channel.id in v:
            for channel_id in v:
                if message.channel.id == channel_id:
                    continue
                translation = translator.translate(message.content, dest = channel_language[channel_id])
                embed = discord.Embed(title = '', description = translation.text + '\n\n' + 'via #' + str(message.channel), color = discord.Color.red())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                await client.get_channel(channel_id).send(embed = embed)

bot_token = os.environ['TOKEN']
client.run(bot_token)

