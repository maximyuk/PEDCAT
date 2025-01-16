from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# 🖤 card
def url_card_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_card = "https://send.monobank.ua/jar/5uzN1NcwYA"

    builder.add(InlineKeyboardButton(text="Поповнити монобанку 🖤", url=url_card))
    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="other_inline"))

    return builder.adjust(1, 2).as_markup()


# 📘 contact
def url_contact_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_contact = "https://vvpc.com.ua/contacts"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Перевірити 🌐", url=url_contact))

    return builder.as_markup()


# 💳 score
def url_score_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_score = "https://vvpc.com.ua/node/980"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Перевірити 🌐", url=url_score))

    return builder.as_markup()


# 🌎 official site
def url_official_site_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_official_site = "https://vvpc.com.ua/"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Сайт 🌐", url=url_official_site))

    return builder.as_markup()


# 📗 introduction
def url_introduction_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_introduction = "https://vvpc.com.ua/vstup"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Вступ ➡️", url=url_introduction))

    return builder.as_markup()


# 🛡 about college
def url_about_college_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_about_college = "https://vvpc.com.ua/node/948"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Про коледж 🛡", url=url_about_college))

    return builder.as_markup()


# 📜 speciality
def url_speciality_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    url_speciality = "https://padlet.com/VasylT/padlet-2ppk483bi2mgsg3h"

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="applicant_inline"))
    builder.add(InlineKeyboardButton(text="Спеціальності 🤯", url=url_speciality))

    return builder.as_markup()
