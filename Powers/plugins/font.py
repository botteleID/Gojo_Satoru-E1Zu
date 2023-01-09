from html import escape
from random import choice

from pyrogram import enums
from pyrogram.errors import MessageTooLong
from pyrogram.types import Message
import telebot
from telebot import types

from Powers import DEV_USERS, LOGGER
from Powers.bot_class import Gojo
from Powers.utils import extras
from Powers.utils.custom_filters import command



   
@Gojo.on_message(command("font1"))
async def fontsat(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Please reply to a message or enter text after command to weebify it.",
        )
        return
    if not args:
        await m.reply_text(text="What am I supposed to Weebify?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "卂 乃 匚 刀 乇 下 厶 卄 工 丁 长 乚 从 𠘨 口 尸 㔿 尺 丂 丅 凵 リ 山 乂 丫 乙".split()

    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<b>Weebified String:</b>
        <code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f2 '{args}' in {m.chat.id}")
    return
    
@Gojo.on_message(command("font2"))
async def fontdu(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Please reply to a message or enter text after command to weebify it.",
        )
        return
    if not args:
        await m.reply_text(text="What am I supposed to Weebify?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "𝖆 𝖇 𝖈 𝖉 𝖊 𝖋 𝖌 𝖍 𝖎 𝖏 𝖐 𝖑 𝖒 𝖓 𝖔 𝖕 𝖖 𝖗 𝖘 𝖙 𝖚 𝖛 𝖜 𝖝 𝖞 𝖟".split()

    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<b>Weebified String:</b>
        <code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f2 '{args}' in {m.chat.id}")
    return    


__PLUGIN__ = "font"

_DISABLE_CMDS_ = [
    "font1",
    "font2",
]

__HELP__ = """
**Font Generator**

• /shout '<keyword>': tulis apa saja yang ingin kamu berikan teriakan nyaring."""
