import discord
import os
from googletrans import Translator

client = discord.Client()
translator = Translator()

general_eng = 837977828808458253
guild_war_eng = 839855093905883176
cross_war_eng = 840218404198940713

general_ch = 841307528121155594
guild_war_ch = 841313365975498763
cross_war_ch = 841313415958888468

general_kr = 841313609761816626
guild_war_kr = 841313665843462164
cross_war_kr = 841313714815893567

async def translate_from_eng(message, ch_channel, ko_channel):
    chinese = translator.translate(message.content, dest = "zh-tw")
    embed_ch = discord.Embed(title = "", description = chinese.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_ch.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(ch_channel).send(embed = embed_ch)
    korean = translator.translate(message.content, dest = "ko")
    embed_ko = discord.Embed(title = "", description = korean.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_ko.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(ko_channel).send(embed = embed_ko)

async def translate_from_ch(message, eng_channel, ko_channel):
    english = translator.translate(message.content, dest = "en")
    embed_en = discord.Embed(title = "", description = english.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_en.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(eng_channel).send(embed = embed_en)
    korean = translator.translate(message.content, dest = "ko")
    embed_ko = discord.Embed(title = "", description = korean.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_ko.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(ko_channel).send(embed = embed_ko)

async def translate_from_ko(message, eng_channel, ch_channel):
    english = translator.translate(message.content, dest = "en")
    embed_en = discord.Embed(title = "", description = english.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_en.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(eng_channel).send(embed = embed_en)
    chinese = translator.translate(message.content, dest = "zh-tw")
    embed_ch = discord.Embed(title = "", description = chinese.text + "\n\n" + "via #" + str(message.channel), color = discord.Color.red())
    embed_ch.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
    await client.get_channel(ch_channel).send(embed = embed_ch)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == general_eng:
        await translate_from_eng(message, general_ch, general_kr)
    if message.channel.id == guild_war_eng:
        await translate_from_eng(message, guild_war_ch, guild_war_kr)
    if message.channel.id == cross_war_eng:
        await translate_from_eng(message, cross_war_ch, cross_war_kr)
    if message.channel.id == general_ch:
        await translate_from_ch(message, general_eng, general_kr)
    if message.channel.id == guild_war_ch:
        await translate_from_ch(message, guild_war_eng, guild_war_kr)
    if message.channel.id == cross_war_ch:
        await translate_from_ch(message, cross_war_eng, cross_war_kr)
    if message.channel.id == general_kr:
        await translate_from_ko(message, general_eng, general_ch)
    if message.channel.id == guild_war_kr:
        await translate_from_ko(message, guild_war_eng, guild_war_ch)
    if message.channel.id == cross_war_kr:
        await translate_from_ko(message, cross_war_eng, cross_war_ch)



bot_token = os.environ['TOKEN']
client.run(bot_token)

