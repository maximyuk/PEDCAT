from aiogram import F, Router, types
from src.keyboards import *
from src.data_base import Database

router = Router()


@router.callback_query(F.data == "Статистика 🧮")
async def stats_all_query(query: types.CallbackQuery) -> None:
    db = await Database.setup()
    value_user = await db.count_user()
    value_student = await db.count_student()
    stats = (
        f"📊 <b>Статистика користувачів :</b>\n"
        f" • Загальна к-сть користувачів : {value_user}\n\n"
        f" • Кількість студентів у боті : {value_student}\n"
    )

    error = (
        "На жаль, статистика не змінилася.\n"
        "Чому б не запропонувати\n"
        "бота своїм одногрупникам? 😋"
    )

    try:
        await query.message.edit_text(text=stats, reply_markup=update_kb(), parse_mode="HTML")
    except Exception:
        await query.answer(text=error, show_alert=True)
