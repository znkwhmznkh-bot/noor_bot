import telebot
import os

# جلب البيانات
BOT_TOKEN = os.environ.get('BOT_TOKEN')
# جربنا هذا المعرف، تأكد أنه لم يتغير
CHAT_ID = "-1002302305574" 

bot = telebot.TeleBot(BOT_TOKEN)

def test_connection():
    try:
        # محاولة إرسال رسالة بسيطة جداً
        msg = "صدقة جارية عن روح المرحوم كاظم صالح خليفة ✅\nهذا المنشور للتجربة."
        bot.send_message(CHAT_ID, msg)
        print("✅ تم الإرسال بنجاح! اذهب للقناة وتأكد.")
    except Exception as e:
        print(f"❌ فشل الإرسال بسبب: {e}")
        print("تأكد أن البوت مشرف في القناة الصحيحة وأن التوكن سليم.")

if __name__ == "__main__":
    test_connection()
