# SplitBuddy — Telegram бот для дележки расходов

## Запуск (локально)
1. Установите Python 3.11+
2. Создайте виртуальное окружение и установите зависимости:
   
   ```bash
   pip install -r requirements.txt
   ```
3. Создайте файл `.env` по примеру `.env.example` и вставьте ваш Telegram Bot Token.
4. Запустите бота:
   
   ```bash
   python -m src.main
   ```

## Функционал MVP
- /start, /help
- /newbill (заглушка)
- /status (заглушка)

## Стек
- aiogram 3
- SQLAlchemy + SQLite

## Структура
- `src/main.py` — входная точка
- `src/config.py` — конфиг (переменные окружения)
- `src/db.py` — модели и подключение к БД
- `src/handlers.py` — команды и роуты
