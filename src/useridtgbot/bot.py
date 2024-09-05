from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, MessageHandler, filters


async def message_handler(update: Update, context: CallbackContext) -> None:
    first_name = update.effective_user.first_name
    user_name = update.message.chat.username
    user_id = update.effective_user.id
    user_language = update.effective_user.language_code
    current_date = update.message.date.isoformat()

    response_message = (
        f"Имя: {first_name}\n"
        f"Ник: {user_name}\n"
        f"ID: {user_id}\n"
        f"Язык: {user_language}\n"
        f"Время: {current_date}"
    )

    await update.message.reply_text(response_message)

def main():
    TOKEN = 'TOKEN'

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    app.run_polling()

if __name__ == '__main__':
    main()