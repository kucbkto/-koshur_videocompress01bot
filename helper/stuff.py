#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Assalamu'alaikum `{ok.user.first_name}`\nBe chus video compress bot.\nBe kre videok size kam quality kharab krne warai\nBaye deme be screnshot te video te.",
        buttons=[
            [Button.inline("MADAD", data="ihelp")],
            [
                Button.url("BAKI BOTS", url="https://t.me/kashir_bots"),
                Button.url("DEVELOPER", url="t.me/kashmir_1"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠  Quality CompressorBot**\n\n+KRE TUHIND VIDEO COMPRESS QUALITY KHRAB GAXENEY WARAIY.\n+BE HAKE DETH Compressed SAMPLE Video\n+be chus shhal istamaal krun\n-Quality Settings MUJUB mai chu lgn time Compress karnas.\nAARAM SAAN Soz video ake ake mtlb yele1 mkle pure compress gaxeth aday soze byakh video.\nspam ne baya kyanh.\n\nvideo soaz yakr forward  te yenay options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠  Quality CompressorBot**\n\n+KRE TUHIND VIDEO COMPRESS QUALITY KHRAB GAXENEY WARAIY.\n+BE HAKE DETH Compressed SAMPLE Video\n+Screenshots Te deme\n+be chus shhal istamaal krun\n--Quality Settings MUJUB mai chu lgn time Compress karnas.\nAARAM SAAN Soz video ake ake mtlb yele1 mkle pure compress gaxeth aday soze byakh video.\nspam ne baya kyanh.\n\nvideo soaz yakr forward  te yenay options",
        buttons=[Button.inline("WAPAS", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"Assalamu'alaikum `{ok.user.first_name}`\nBE CHUS VIDEO COMPRESS BOT.\nTE KRE TUHIND VIDEO COMPRESS QUALITY KHRAB GAXENEY WARAIY\nbaye deme screenshot te sample video te.",
        buttons=[
            [Button.inline("MADAD", data="ihelp")],
            [
                Button.url("BAKI BOTS", url="https://t.me/kashir_bots"),
                Button.url("DEVELOPER", url="t.me/kashmir_1"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("MYANNE HISAB", data=f"encc{key}"),
                Button.inline("TUNDE HISAB", data=f"ccom{key}"),
            ],
            [Button.inline("Back", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **BE KYA KRE** 🐠",
        buttons=[
            [
                Button.inline("GENERATE SAMPLE", data=f"gsmpl{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("COMPRESS", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send Ur Custom Name For That File")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Wanevhaz naav kya thavo : {g}\n\nSOAZ Thumbnail Picture AME KHATRE."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
