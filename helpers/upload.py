#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import time

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

from helpers.tools import clean_up
from helpers.progress import progress_func

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def upload_audio(client, message, file_loc):

    msg = await message.edit_text(
        text="**ᴜᴘʟᴏᴀᴅɪɴɢ ᴇxᴛʀᴀᴄᴛᴇᴅ sᴛʀᴇᴀᴍ...**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂", callback_data="progress_msg")]])
    )

    title = None
    artist = None
    thumb = None
    duration = 0

    metadata = extractMetadata(createParser(file_loc))
    if metadata and metadata.has("title"):
        title = metadata.get("title")
    if metadata and metadata.has("artist"):
        artist = metadata.get("artist")
    if metadata and metadata.has("duration"):
        duration = metadata.get("duration").seconds

    c_time = time.time()    

    try:
        await client.send_audio(
            chat_id=message.chat.id,
            audio=file_loc,
            thumb=thumb,
            caption="**𝙹𝙾𝙸𝙽 𝙾𝚄𝚁𝚂 𝙰𝙻𝙻 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂 =» @UNI_MOVIES_BOX**",
            title=title,
            performer=artist,
            duration=duration,
            progress=progress_func,
            progress_args=(
                "**𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙴𝚇𝚃𝚁𝙰𝙲𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼...**",
                msg,
                c_time
            )
        )
    except Exception as e:
        print(e)     
        await msg.edit_text("**Some Error Occurred. See Logs for More Info.**")   
        return

    await msg.delete()
    await clean_up(file_loc)    


async def upload_subtitle(client, message, file_loc):

    msg = await message.edit_text(
        text="**𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙴𝚇𝚃𝚁𝙰𝙲𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼...**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="𝙿𝚁𝙾𝙶𝚁𝙴𝚂𝚂", callback_data="progress_msg")]])
    )

    c_time = time.time() 

    try:
        await client.send_document(
            chat_id=message.chat.id,
            document=file_loc,
            caption="**𝙹𝙾𝙸𝙽 𝙾𝚄𝚁𝚂 𝙰𝙻𝙻 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂 =» @UNI_MOVIES_BOX**",
            progress=progress_func,
            progress_args=(
                "**𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙴𝚇𝚃𝚁𝙰𝙲𝚃𝙴𝙳 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴...**",
                msg,
                c_time
            )
        )
    except Exception as e:
        print(e)     
        await msg.edit_text("**Some Error Occurred. See Logs for More Info.**")   
        return

    await msg.delete()
    await clean_up(file_loc)        
