from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝙃𝙚𝙮 {msg.from_user.mention},

𝙏𝙝𝙞𝙨 𝙞𝙨 {me2},
𝘼𝙣 𝙤𝙥𝙚𝙣 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙩𝙧𝙞𝙣𝙜 𝙨𝙚𝙨𝙨𝙞𝙤𝙣 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧 𝙗𝙤𝙩❟ 𝙬𝙧𝙞𝙩𝙩𝙚𝙣 𝙞𝙣 𝙥𝙮𝙩𝙝𝙤𝙣 𝙬𝙞𝙩𝙝 𝙩𝙝𝙚 𝙝𝙚𝙡𝙥 𝙤𝙛 𝙥𝙮𝙧𝙤𝙜𝙧𝙖𝙢 

𝙈𝙖𝙙𝙚 𝙬𝙞𝙩𝙝 𝙗𝙮  :[ᴄʜᴧᴍᴘᴜ](t.me/TheShivanshu) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝘾𝙝𝙖𝙢𝙥𝙪", url="https:/t.me/TheShivanshu"),
                    InlineKeyboardButton("𝙊𝙬𝙣𝙚𝙧", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
