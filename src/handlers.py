from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я SplitBuddy — помогу делить расходы в группе.\n"
        "/newbill — создать счет (скоро)\n"
        "/status — сводка по долгам (скоро)\n"
        "/help — справка"
    )

@router.message(F.text == "/help")
async def cmd_help(message: Message):
    await message.answer(
        "Команды:\n"
        "/start — приветствие\n"
        "/newbill — создать счет (MVP-заглушка)\n"
        "/status — сводка (MVP-заглушка)\n"
        "/help — помощь"
    )

@router.message(F.text == "/newbill")
async def cmd_newbill(message: Message):
    await message.answer("Создание счета пока в разработке. Скоро добавим формы и кнопки ✍️")

@router.message(F.text == "/status")
async def cmd_status(message: Message):
    await message.answer("Сводка долгов пока недоступна. В ближайшем релизе появится баланс по участникам.")
