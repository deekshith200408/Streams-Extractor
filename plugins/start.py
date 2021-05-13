#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script


@trojanz.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text(
        text=Script.START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="help_data"),
                    InlineKeyboardButton("🤴 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "🛡️𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙰𝙽𝙽𝙴𝙻𝚂🛡️", url="https://t.me/UNI_MOVIES_BOX")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data="start_data"),
                    InlineKeyboardButton("🕵️ 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton(
                        "🤹 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 🤹", url="https://t.me/TroJanzSupport")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )


@trojanz.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await message.reply_text(
        text=Script.ABOUT_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data="help_data"),
                    InlineKeyboardButton("🏛️𝚂𝚃𝙰𝚁𝚃 𝙱𝙾𝚃", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton(
                        "🤴 𝙲𝚁𝙴𝙰𝚃𝙴𝚁/𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝚁 🏇", url="https://t.me/Deeks_04_8")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
