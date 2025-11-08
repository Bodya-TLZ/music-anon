from telegram.ext import Updater, MessageHandler, Filters

# ======== Вставляем токен и ID группы ========
TOKEN = '8001234383:AAEGE2kWQK2qk0FkUzzK9k7Ca5Gk1__7elA'
ADMIN_GROUP_ID = -1003266451531
# ============================================

# Обработчик входящих сообщений
def handle_message(update, context):
    user_text = update.message.text
    if user_text:
        # Отправляем анонимно в группу администрации
        context.bot.send_message(
            chat_id=ADMIN_GROUP_ID,
            text=f"📩 Новое сообщение:\n\n{user_text}"
        )
        # Подтверждение пользователю
        update.message.reply_text("✅ Сообщение отправлено администрации анонимно.")

# Основная функция запуска бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
