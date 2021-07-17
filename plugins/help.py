from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Cukup Kirim Url/Link Youtube Ke Chat Ini\nmade by @xskull7"
    await message.reply_text(helptxt)
