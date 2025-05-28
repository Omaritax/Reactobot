import discord
import random
import os
from keep_alive import keep_alive

# إعداد الـ Intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# التوكن من secret
TOKEN = os.getenv('TOKEN')

# قائمة ردود الفعل (emojis) اللي ممكن يختارها البوت
reactions = ['😂','🤏🏻','🔥','💀','🐵','💔','🙏','🚬','🗿', '🗣️','👹','💩']

# كلمات بتدل على الضحك
laugh_keywords = ['ضحكت', 'هههه', 'lol', 'ياعم', 'lmao', '😂', '🤣','لول','احا','اجدع','يعم','kys','حرام','اقتل','خخ','بضان']

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(keyword in message.content.lower() for keyword in laugh_keywords):
        reaction = random.choice(reactions)
        try:
            await message.add_reaction(reaction)
        except Exception as e:
            print(f'Error adding reaction: {e}')

keep_alive()  # لتشغيل سيرفر الويب (HTTP) عشان UptimeRobot
client.run(TOKEN)
