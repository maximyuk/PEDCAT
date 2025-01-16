from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.data_base import Database


async def settings_inline_kb(user_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    db = await Database.setup()

    if await db.student_exists(user_id):
        if await db.student_agreed_news_exists(user_id):
            builder.add(
                InlineKeyboardButton(
                    text="Новини 🔔 ✅",
                    callback_data="change_news_not_agreed",
                )
            )

        elif not await db.student_agreed_news_exists(user_id):
            builder.add(InlineKeyboardButton(text="Новини 🔔 🚫", callback_data="change_news_agreed"))
        if await db.student_agreed_alert_exists(user_id):
            builder.add(
                InlineKeyboardButton(
                    text="Тривоги ⚠️ ✅",
                    callback_data="change_alert_not_agreed",
                )
            )

        elif not await db.student_agreed_alert_exists(user_id):
            builder.add(
                InlineKeyboardButton(text="Тривоги ⚠️ 🚫", callback_data="change_alert_agreed")
            )

        builder.add(InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌"))

        builder.add(
            InlineKeyboardButton(text="Змінити групу 🔄", callback_data="change_student_group")
        )

        return builder.adjust(2).as_markup()
