from aiogram import F, Router, types
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from src.keyboards import *
from src.data_base import Database
from src.utils import is_super_admin, password_for_admin, get_current_date, clear_all

import aiohttp
import asyncio

router = Router()


class FSMSuperAdminPanel(StatesGroup):
    add_or_change_calls = State()
    add_or_change_schedule_name = State()
    add_or_change_schedule_photo = State()
    add_group_name = State()
    add_or_change_any_photo = State()
    delete_group_name = State()


@router.callback_query(F.data == "Оновити 📅")
async def add_or_change_schedule1(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "Виберіть групу зі списку ⬇️", reply_markup=await group_selection_student_kb()
    )
    await state.set_state(FSMSuperAdminPanel.add_or_change_schedule_name)
    

@router.callback_query(FSMSuperAdminPanel.add_or_change_schedule_name)
async def add_or_change_schedule_get_name_group(
    query: types.CallbackQuery, state: FSMContext
):
    await query.message.edit_text(
        "Надішліть фото 🖼\nЗ увімкнутим стисненням та назвою групи у описі",
        reply_markup=None,
    )
    await state.set_state(FSMSuperAdminPanel.add_or_change_schedule_photo)
    await state.update_data(name_group=query.data, message=query.message)


@router.message(F.photo, FSMSuperAdminPanel.add_or_change_schedule_photo)
async def add_or_change_schedule2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    date = f"Змінено: {get_current_date()}"
    data = (await state.get_data())["name_group"]
    

    await message.answer("Фото групи змінено ✅", reply_markup=super_admin_kb())
    await clear_all(message, state)

    await db.student_group_photo_update(data, message.photo[0].file_id, date)



@router.message(F.text.startswith("sql "))
async def sql(message: types.Message) -> None:
    if not await is_super_admin(message):
        return

    db = await Database.setup()
    await db.sql_request(message.text[4:])
    await message.answer("GOOD JOB")


@router.callback_query(F.data == "Пароль 🔐")
async def password(query: types.CallbackQuery) -> None:
    if not await is_super_admin(query):
        return

    await query.answer(f"PASSWORD : {password_for_admin()}", show_alert=True)


@router.callback_query(F.data == "База даних 🖥")
async def send_file_db(query: types.CallbackQuery) -> None:
    if not await is_super_admin(query):
        return

    file_path = types.FSInputFile("data/database.db")
    await query.bot.send_document(query.from_user.id, file_path)
    await query.answer()


@router.callback_query(F.data == "⬅️ Назад")
async def super_admin_back(query: types.CallbackQuery, state: FSMContext):
    text = f"Панель керування ботом 🎛\n"

    await state.clear()
    await query.message.edit_text(text=text, reply_markup=super_admin_kb())


@router.callback_query(F.data == "Групи 👥")
async def choice_in_panel1(query: types.CallbackQuery):
    text = (
        f"Панель керування Групами 🎛\n" f"• Додати групу 👥\n" f"• Видалити групу 👥\n"
    )

    await query.message.edit_text(text=text, reply_markup=super_admin_group())


@router.callback_query(F.data == "Змінити 🔔")
async def add_or_change_calls1(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "Надішліть фото 🖼\nЗ увімкнутим стисненням", reply_markup=super_admin_back_kb()
    )
    await state.set_state(FSMSuperAdminPanel.add_or_change_calls)
    await state.update_data(message=query.message)


@router.message(F.photo, FSMSuperAdminPanel.add_or_change_calls)
async def add_or_change_calls2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    date = f"Змінено: {get_current_date()}"

    await message.answer("Фото дзвінків змінено ✅", reply_markup=super_admin_kb())
    await clear_all(message, state)

    if await db.photo_exists("calls"):
        await db.update_photo(
            name_photo="calls", photo=message.photo[0].file_id, date_photo=date
        )
        return

    await db.add_photo(
        name_photo="calls", photo=message.photo[0].file_id, date_photo=date
    )


@router.callback_query(F.data == "Додати 👥")
async def add_student(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "Введіть назву групи ⬇️", reply_markup=super_admin_back_kb()
    )
    await state.set_state(FSMSuperAdminPanel.add_group_name)


@router.message(F.text, FSMSuperAdminPanel.add_group_name)
async def add_student2(message: types.Message, state: FSMContext):
    db = await Database.setup()
    user_message = message.text

    await db.add_student_group(user_message)

    await message.answer("Група додана ✅", reply_markup=super_admin_back_kb())
    await state.clear()


@router.callback_query(F.data == "Видалити 👥")
async def delete_student(query: types.CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "Виберіть групу зі списку нижче ⬇️",
        reply_markup=await group_selection_student_kb(),
    )

    await state.set_state(FSMSuperAdminPanel.delete_group_name)


@router.callback_query(F.data, FSMSuperAdminPanel.delete_group_name)
async def delete_student2(query: types.CallbackQuery, state: FSMContext):
    db = await Database.setup()
    group_name = query.data

    await db.delete_student_group(group_name)

    await query.message.edit_text(
        f"Група {group_name} видалена ✅", reply_markup=super_admin_back_kb()
    )
    await state.clear()



# @router.callback_query(F.data == "Додати фото тваринки")
# async def add_animal_photo(message: types.Message):
#     db = await Database.setup()

#     # Отримуємо фото і підпис від користувача
#     photo = message.photo[-1].file_id  # Отримуємо файл фото (найкращу якість)
#     caption = message.caption if message.caption else "Фото тваринки"
#     name_photo = caption  # Можна взяти з підпису чи інше поле для назви
#     date_photo = get_current_date()  # Задайте поточну дату, якщо потрібно
    
#     # Додаємо фото тваринки в базу даних
#     await db.add_animal_photo(name_photo, photo, date_photo)

#     # Відповідаємо користувачу
#     await message.answer("Фото тваринки додано в базу ✅", reply_markup=admin_kb())