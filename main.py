import discord
import os
from google.cloud import translate_v2 as translate
import six

client = discord.Client()
translator = translate.Client()

translation_groups = {}
translation_groups['general'] = [837977828808458253, 841313609761816626, 841307528121155594, 842043260109324378, 849642737719967754] #to be removed
translation_groups['guild_war'] = [839855093905883176, 841313665843462164, 841313365975498763, 842043319978295316, 849642822076596244] #to be removed
translation_groups['cross_war'] = [840218404198940713, 841313714815893567, 841313415958888468, 842043378257625140, 849642967769808896] #to be removed
translation_groups['new_general'] = [866912447381372949, 866913492888190996, 866913578799464449, 866913657749635103, 866913738593796096]
translation_groups['new_off_topic'] = [866912466171592744, 866916411071135764, 866916540170764328, 866916483744923688, 866916614288310283]
translation_groups['new_guild_war'] = [866912263569670144, 866913872865656862, 866913937710776350, 866914012171993108, 866914091212734464]
translation_groups['new_cross_war'] = [866912286577000468, 866915237802278932, 866916132466982932, 866916179951878196, 866916236617449492]

channel_language = {}
channel_language[837977828808458253] = 'en' #to be removed
channel_language[841313609761816626] = 'ko' #to be removed
channel_language[841307528121155594] = 'zh-tw' #to be removed
channel_language[842043260109324378] = 'ja' #to be removed
channel_language[849642737719967754] = 'pt' #to be removed
channel_language[839855093905883176] = 'en' #to be removed
channel_language[841313665843462164] = 'ko' #to be removed
channel_language[841313365975498763] = 'zh-tw' #to be removed
channel_language[842043319978295316] = 'ja' #to be removed
channel_language[849642822076596244] = 'pt' #to be removed
channel_language[840218404198940713] = 'en' #to be removed
channel_language[841313714815893567] = 'ko' #to be removed
channel_language[841313415958888468] = 'zh-tw' #to be removed
channel_language[842043378257625140] = 'ja' #to be removed
channel_language[849642967769808896] = 'pt' #to be removed
channel_language[866912447381372949] = 'en'
channel_language[866912466171592744] = 'en'
channel_language[866912263569670144] = 'en'
channel_language[866912286577000468] = 'en'
channel_language[866913492888190996] = 'zh-tw'
channel_language[866916411071135764] = 'zh-tw'
channel_language[866913872865656862] = 'zh-tw'
channel_language[866915237802278932] = 'zh-tw'
channel_language[866913578799464449] = 'ko'
channel_language[866916540170764328] = 'ko'
channel_language[866913937710776350] = 'ko'
channel_language[866916132466982932] = 'ko'
channel_language[866913657749635103] = 'ja'
channel_language[866916483744923688] = 'ja'
channel_language[866914012171993108] = 'ja'
channel_language[866916179951878196] = 'ja'
channel_language[866913738593796096] = 'pt'
channel_language[866916614288310283] = 'pt'
channel_language[866914091212734464] = 'pt'
channel_language[866916236617449492] = 'pt'


def translate_text(target, text):
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    result = translator.translate(text, target_language=target)
    return result["translatedText"]

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
                translation = translate_text(channel_language[channel_id], message.content)
                embed = discord.Embed(title = '', description = translation + '\n\n' + 'via #' + str(message.channel), color = discord.Color.red())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                await client.get_channel(channel_id).send(embed = embed)

bot_token = os.environ['TOKEN']
client.run(bot_token)

