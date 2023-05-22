from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🫧ꜱᴛᴀʀᴛ ꜱᴇꜱꜱɪᴏɴ🫧", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/ab_sumit")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴡᴀɴɴᴀ ꜱᴇᴇ ᴍᴏʀᴇ ʙᴏᴛ", url="https://t.me/thebotstaus")],
    ]

    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ {}
•━━━━━━━•⊰᯽⊱•━━━━━━━•
➻ ɪ'ᴍ ʜᴇʀᴇ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴs \n\n
➻ ᴜꜱᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ
•━━━━━━━•⊰᯽⊱•━━━━━━━• \n\n
❅ᴘᴏᴡᴇʀᴇᴅ ʙʏ - @thebotstatus

    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴍᴇ** 

➻ᴛʜɪꜱ ɪꜱ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀɪɴɢ  ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ

ꜱᴏᴜʀᴄᴇ: [Click Here](https://t.me/thebotstatus)

</>ᴠɪsɪᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ] (https://t.me/twinkleXstars) ғᴏʀ ᴍᴏʀᴇ...

ᴅᴇᴠᴇʟᴏᴘᴇʀ - [ꜱᴜᴍɪᴛ🥀] (https://t.me/ll_sumit_ll)

    """
