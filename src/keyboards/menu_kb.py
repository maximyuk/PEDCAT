from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
)

from src.data_base import Database


# Головна клавіатура для не зареєстрованих
def start_all_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = ["Реєстрація 📝", "Розклад 📚", "Інше 📌", "Для абітурієнта 🧑‍💻"]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# Головна клавіатура для студентів
def start_student_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = ["Студент 👨‍🎓", "Налаштування ⚙️", "Інше 📌", "Розклад 📚"]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# Головна клавіатура для адмінів
def start_admin_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    keyboard = ["Панель 📁", "Адмін 🔑", "Інше 📌", "Розклад 📚", "Налаштування ⚙️"]

    for button in keyboard:
        builder.add(KeyboardButton(text=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# 📌 other
def other_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Про бота 🖇",
        "Про мене 👀",
        "Статистика 🧮",
        "Допомога 🛠",
        "Час роботи 📅",
        # "Фото кота 🖼",
        "Сховати ❌",
        "Донат 🫡",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# 🧑‍💻 applicant
def applicant_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = ["Вступ 📗", "Про коледж 🛡", "Адреса 📫", "Контакти 📘", "Реквізити 💳"]
    keyboard_url = [
        ("Офіційний сайт 🌎", "https://vvpc.com.ua/"),
        ("Спеціальності 📜", "https://padlet.com/VasylT/padlet-2ppk483bi2mgsg3h"),
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    builder.add(InlineKeyboardButton(text=keyboard_url[0][0], url=keyboard_url[0][1]))
    builder.add(InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌"))
    builder.add(InlineKeyboardButton(text=keyboard_url[1][0], url=keyboard_url[1][1]))

    return builder.adjust(2).as_markup(resize_keyboard=True)


# Клавіатура розкладу (для зареєстрованих)
async def schedule_kb(user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    db = await Database.setup()

    keyboard = ["Розклад студ. 🧑‍🎓", "Сховати ❌"]

    if await db.student_exists(user_id):
        keyboard.insert(0, "Розклад дзвінків ⌚️")
        keyboard.insert(0, "Розклад пар 👀")
        keyboard.insert(3, "Ч/З тиждень ✏️")

        for button in keyboard:
            builder.add(InlineKeyboardButton(text=button, callback_data=button))

        return builder.adjust(2).as_markup(resize_keyboard=True)

    else:
        keyboard.insert(0, "Ч/З тиждень ✒️")
        keyboard.insert(0, "Розклад дзвінків ⌛️")

        for button in keyboard:
            builder.add(InlineKeyboardButton(text=button, callback_data=button))

        return builder.adjust(2).as_markup(resize_keyboard=True)

def animals_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Сховати ❌",
        "⬅️ Назад",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)




