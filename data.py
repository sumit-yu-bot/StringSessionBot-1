from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
    ]

    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ {}
•━━━━━━━•⊰᯽⊱•━━━━━━━•
➻ ɪ'ᴍ ʜᴇʀᴇ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴs 
➻ ᴜꜱᴇ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ
•━━━━━━━•⊰᯽⊱•━━━━━━━•
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

ꜱᴏᴜʀᴄᴇ: [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)

</>ᴠɪsɪᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ] (https://t.me/twinkleXstars) ғᴏʀ ᴍᴏʀᴇ...

ᴅᴇᴠᴇʟᴏᴘᴇʀ - [ꜱᴜᴍɪᴛ🥀] (https://t.me/ll_sumit_ll)

    """
