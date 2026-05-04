import telebot
import os

API_TOKEN = os.getenv('BOT_TOKEN') 
CHANNEL_ID = '@Norham313' # هذا هو المعرف اللي بالرابط مالتك

bot = telebot.TeleBot(API_TOKEN)

def send_test():
    try:
        bot.send_message(CHANNEL_ID, "تم تفعيل النشر التلقائي بنجاح.. صدقة جارية لروح المرحوم كاظم صالح خليفة.")
        print("✅ تم النشر!")
    except Exception as e:
        print(f"❌ فشل: {e}")

if __name__ == "__main__":
    send_test()
