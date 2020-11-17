"""Hello 👋, Welcome To 𝗔𝗡𝗧𝗜𝗗𝗘𝗟𝗘𝗧𝗘𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 𝗥𝗢𝗕𝗢𝗧 🚫.\n\nThis Is A Bot For 𝗞𝗜𝗖𝗞𝗜𝗡𝗚 𝗗𝗘𝗟𝗘𝗧𝗘𝗗 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 From Groups.\n\nI Will Check For Deleted Accounts In Active Groups Once An Hour, But Only If The Group Is Active. It Requires The 𝗕𝗔𝗡 𝗨𝗦𝗘𝗥 Permission In Groups & Any Permissions In Channels.

[𝗥𝗘𝗣𝗢𝗥𝗧 𝗕𝗢𝗧 𝗜𝗦𝗦𝗨𝗘𝗦 𝗛𝗘𝗥𝗘 ⚠](https://t.me/Iggie)

[𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗔𝗡𝗗𝗥𝗢𝗜𝗗 𝗔𝗣𝗣𝗟𝗜𝗖𝗔𝗧𝗜𝗢𝗡𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 📱](https://t.me/joinchat/AAAAAE-44AkxSyqIMj1tdQ)

See /help For More Info.
"""

from asyncio import sleep
from .global_functions import log
from telethon import client, events, errors


# /start
@events.register(events.NewMessage(pattern=r"/start$"))
async def on_start(event):
    if event.is_private:    # If command was sent in private
        await log(event)    # Logs the event
        await event.respond(__doc__, link_preview=False)


# Reply when added to group
@events.register(events.ChatAction(func=lambda e:e.user_added and e.is_group))
async def added_to_group(event):
    group = await event.get_chat() # Get group object
    me = (await event.client.get_me()).id

    response = None
    # Check which users were added to the group,
    # if the bot is amongst them, send the message
    for u in event.users:
        if me == u.id:
            response = await event.respond(__doc__, link_preview=False)

    if not response:
        return

    # Delete the message after a minute
    await sleep(60)
    try:
        await response.delete()
    except errors.ChannelPrivateError:
        return
