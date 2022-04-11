import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  banall_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("●** Karabüyü iyi gelir... . !**",
                    buttons=(
                   
		      [Button.url('🎉  𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/MytTagBot?startgroup=a')],
                      [Button.url('📝  𝗗𝗲𝘀𝘁𝗲𝗸 𝗚𝗿𝘂𝗯𝘂  📝',  'https://t.me/HirasetTR')], 
                      [Button.url('😎  𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  😎', 'https://t.me/Meyitzade47')],
                    ),
                    link_preview=False
                   )
