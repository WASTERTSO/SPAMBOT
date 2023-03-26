from HeartHacker import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from HeartHacker import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/57ba5962f44d06595b353.jpg"

Riz_Help = "|•| Tsᴏ Sᴘᴀᴍ Bᴏᴛ ⋟\n\n"
 
Riz_Help += f"__Cᴍᴅs Aᴠᴀɪʟᴀʙʟᴇ Iɴ |•| Tsᴏ Sᴘᴀᴍ Bᴏᴛ ⋟__\n\n"

Riz_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
Riz_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n `.pornspam` - this cmd is use for porn spam\n\n"




@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
      await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("Sᴜᴘᴘᴏʀᴛ 🚑", "https://t.me/tso_chats")
        ],
        [
        Button.url("Uᴘᴅᴀᴛᴇs 🚀", "https://t.me/tso_updates")
        ] 
        ]
        )                                                         
