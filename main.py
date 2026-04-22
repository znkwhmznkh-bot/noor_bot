import telebot
import os

# الحصول على الرموز من الإعدادات
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"

bot = telebot.TeleBot(BOT_TOKEN)

def send_test_message():
    try:
        # محاولة إرسال رسالة بسيطة جداً
        message = "✅ تم تشغيل البوت بنجاح.. صدقة جارية لروح المرحوم كاظم صالح خليفة"
        bot.send_message(CHAT_ID, message)
        print("Done! Check your channel.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_test_message()
