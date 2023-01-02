from traceback import format_exc

from Powers.utils.custom_filters import command 
from Powers import LOGGER
from Powers.bot_class import Gojo 
# All the import provided above is mandotry in case you don't want to use logger remove the first and third import 
# Import more funcs and module as per your need

@Gojo.on_message(command("^\.samata(?: |$)(.*)")) # Pass additional filters if you need

@register(outgoing=True, pattern=r"^\.samata(?: |$)(.*)")

async def lastname(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:

await event.edit("```Reply to any user message.```")
        return
    message = await event.get_reply_message()
    chat = "@SangMataInfo_bot"

    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Sit tight while we crunching data from NSA```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await event.reply("```Please unblock @sangmatainfo_bot and try again```")
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await event.edit(f"{r.message}")
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith(
                    "No records") or r.text.startswith("No records"):
                await event.edit("```No records found for this user```")
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await event.edit(f"{response.message}")
            await event.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@SangMataInfo_bot` is not responding!.`")



  '''use logger to add log info using LOGGER.info(<string>) in the platfrom on which bot is running 
    and error as LOGGER.error(<string>) and after LOGGER.error() use        
    LOGGER.error(format_exc())'''
    
__PLUGIN__ = "sangmata"
_DISABLE_CMDS_ = [Sang] # Enter the commands if you want that they can be disabled if needed.

__alt_name__ = [<command as string>] # Alternative name of the plugin
    

__HELP__ = """
**Rules**
sang mata
 group."""
