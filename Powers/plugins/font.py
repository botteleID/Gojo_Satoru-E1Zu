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
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "卂 乃 匚 刀 乇 下 厶 卄 工 丁 长 乚 从 𠘨 口 尸 㔿 尺 丂 丅 凵 リ 山 乂 丫 乙".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
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
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "𝖆 𝖇 𝖈 𝖉 𝖊 𝖋 𝖌 𝖍 𝖎 𝖏 𝖐 𝖑 𝖒 𝖓 𝖔 𝖕 𝖖 𝖗 𝖘 𝖙 𝖚 𝖛 𝖜 𝖝 𝖞 𝖟".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f2 '{args}' in {m.chat.id}")
    return    

@Gojo.on_message(command("font3"))
async def fontti(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "ѧ ɞ ċ Ԁ є ғ ɢ һ ı j ҡ ʟ ṃ ṅ ȏ ƿ զ я ṡ ṭ ȗ ṿ ẇ × ʏ ẓ".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f3 '{args}' in {m.chat.id}")
    return    
    
    
@Gojo.on_message(command("font4"))
async def fontem(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "𝚊 𝚋 𝚌 𝚍 𝚎 𝚏 𝚐 𝚑 𝚒 𝚓 𝚔 𝚕 𝚖 𝚗 𝚘 𝚙 𝚚 𝚛 𝚜 𝚝 𝚞 𝚟 𝚠 𝚡 𝚢 𝚣".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f4 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font5"))
async def fontli(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "𝕒 𝕓 𝕔 𝕕 𝕖 𝕗 𝕘 𝕙 𝕚 𝕛 𝕜 𝕝 𝕞 𝕟 𝕠 𝕡 𝕢 𝕣 𝕤 𝕥 𝕦 𝕧 𝕨 𝕩 𝕪 𝕫".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f5 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font6"))
async def fonten(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "ค ๒ ς ๔ є Ŧ ﻮ ђ เ ן к ɭ ๓ ภ ๏ ק ợ г ร Շ ย ש ฬ א ץ չ".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f6 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font7"))
async def fonttu(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "🅰 🅱 🅲 🅳 🅴 🅵 🅶 🅷 🅸 🅹 🅺 🅻 🅼 🅽 🅾 🅿 🆀 🆁 🆂 🆃 🆄 🆅 🆆 🆇 🆈 🆉".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f7 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font8"))
async def fontde(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "𝗮 𝗯 𝗰 𝗱 𝗲 𝗳 𝗴 𝗵 𝗶 𝗷 𝗸 𝗹 𝗺 𝗻 𝗼 𝗽 𝗾 𝗿 𝘀 𝘁 𝘂 𝘃 𝘄 𝘅 𝘆 𝘇".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f8 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font9"))
async def fontsem(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "🇦​ 🇧​ 🇨​ 🇩​ 🇪​ 🇫​ 🇬​ 🇭​ 🇮​ 🇯​ 🇰​ 🇱​ 🇲​ 🇳​ 🇴​ 🇵​ 🇶​ 🇷​ 🇸​ 🇹​ 🇺​ 🇻​ 🇼​ 🇽​ 🇾​ 🇿​".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f9 '{args}' in {m.chat.id}")
    return 

@Gojo.on_message(command("font10"))
async def fontsep(_, m: Message):
    if len(m.text.split()) >= 2:
        args = m.text.split(None, 1)[1]
    elif m.reply_to_message and len(m.text.split()) == 1:
        args = m.reply_to_message.text
    else:
        await m.reply_text(
            "Harap balas pesan atau masukkan teks setelah perintah.",
        )
        return
    if not args:
        await m.reply_text(text="Apa yang harus saya lakukan?")
        return

    # Use split to convert to list
    # Not using list itself becuase black changes it to long format...
    normiefont = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    weebyfont = "ᵃ ᵇ ᶜ ᵈ ᵉ ᶠ ᵍ ʰ ᶦ ʲ ᵏ ˡ ᵐ ⁿ ᵒ ᵖ ᵠ ʳ ˢ ᵗ ᵘ ᵛ ʷ ˣ ʸ ᶻ".split()

    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    await m.reply_text(
        text=f"""<code>{string}</code>"""
    )
    LOGGER.info(f"{m.from_user.id} f10 '{args}' in {m.chat.id}")
    return 


                                    
__PLUGIN__ = "font"

_DISABLE_CMDS_ = [
    "font1",
    "font2",
    "font3",
    "font4",
    "font5",
    "font6",
    "font7",
    "font8",
    "font9",
    "font10",
]



__HELP__ = """
**Font Generator**

• /font1 '<reply text>'
• /font2 '<reply text>'
• /font3 '<reply text>'
• /font4 '<reply text>'
• /font5 '<reply text>'
• /font6 '<reply text>'
• /font7 '<reply text>'
• /font8 '<reply text>'
• /font9 '<reply text>'
• /font10 '<reply text>'"""
