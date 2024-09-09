from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)


async def start_handler(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Получить свой ID", callback_data="id")],
        [InlineKeyboardButton("Получить свой ник", callback_data="username")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Я простой Telegram-бот. Выберите действие:", reply_markup=reply_markup
    )


async def help_handler(update: Update, context: CallbackContext) -> None:
    response = (
        "Доступные команды:\n"
        "/start - запустить бота\n"
        "/help - получить доступные команды\n"
    )
    await update.message.reply_text(response)


async def id_handler(update: Update, context: CallbackContext) -> None:
    response = f"Ваш ID: {update.effective_user.id}"
    await update.callback_query.message.reply_text(response)


async def username_handler(update: Update, context: CallbackContext) -> None:
    response = f"Ваш ник: {update.effective_user.username}"
    await update.callback_query.message.reply_text(response)


async def message_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Вы написали: {update.message.text}")


async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    if query.data == "id":
        await id_handler(update, context)
    elif query.data == "username":
        await username_handler(update, context)

    await query.answer()


def main():
    TOKEN = "TOKEN"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
