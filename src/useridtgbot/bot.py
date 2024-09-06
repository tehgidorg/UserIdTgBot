from telegram import Update
from telegram.ext import (ApplicationBuilder, CallbackContext, CommandHandler,
                          MessageHandler, filters)


async def start_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Привет! Я простой Telegram-бот. Чтобы узнать, что я могу, напиши /help."
    )


async def help_handler(update: Update, context: CallbackContext) -> None:
    response = (
        "Доступные команды:\n"
        "/start - запустить бота\n"
        "/help - получить доступные команды\n"
        "/id - получить свой ID\n"
        "/username - получить свой ник"
    )
    await update.message.reply_text(response)


async def id_handler(update: Update, context: CallbackContext) -> None:
    response = f"Ваш ID: {update.effective_user.id}"
    await update.message.reply_text(response)


async def username_handler(update: Update, context: CallbackContext) -> None:
    response = f"Ваш ник: {update.message.chat.username}"
    await update.message.reply_text(response)


async def message_handler(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"Вы написали: {update.message.text}")


def main():
    TOKEN = "TOKEN"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("id", id_handler))
    app.add_handler(CommandHandler("username", username_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
