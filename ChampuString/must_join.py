from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/4e36fe4ef9bd1f00da0d5.jpg", caption=f"» 𝘼𝙘𝙘𝙤𝙧𝙙𝙞𝙣𝙜 𝙩𝙤 𝙢𝙮 𝙙𝙖𝙩𝙖𝙗𝙖𝙨𝙚 𝙮𝙤𝙪'𝙫𝙚 𝙣𝙤𝙩 𝙟𝙤𝙞𝙣𝙚𝙙 [ᴄʜᴧᴍᴘᴜ]({link}) 𝙔𝙚𝙩❟ 𝙞𝙛 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙪𝙨𝙚 𝙢𝙚 𝙩𝙝𝙚𝙣 𝙟𝙤𝙞𝙣 [ᴄʜᴧᴍᴘᴜ]({link}) 𝘼𝙣𝙙 𝙨𝙩𝙖𝙧𝙩 𝙢𝙚 𝙖𝙜𝙖𝙞𝙣 !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> ᴄʜᴧᴍᴘᴜ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
