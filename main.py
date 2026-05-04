import telebot
import random
import os

# الإعدادات
API_TOKEN = os.getenv('BOT_TOKEN') 
CHANNEL_ID = '@nour_min_nouruhum' # تأكد إن هذا المعرف صحيح 100%

bot = telebot.TeleBot(API_TOKEN)

messages = [
    "عن الإمام علي (ع): «أكرم ضيفك وإن كان حقيراً، وقم عن مجلسك لأبيك ومعلمك وإن كنت أميراً» - (نهج البلاغة)",
    "قالت السيدة فاطمة الزهراء (ع): «فرض الله الصيام تثبيتاً للإخلاص» - (الخطبة الفدكية)",
    "عن السيدة زينب (ع): «ما رأيت إلا جميلاً» - (في مجلس ابن زياد)",
    "اللهم ارحم (كاظم صالح خليفة) واغفر له واسكنه فسيح جناتك.",
    "تذكير: سبحان الله وبحمده، سبحان الله العظيم."
]

def send_post():
    try:
        text = random.choice(messages)
        # محاولة الإرسال
        bot.send_message(CHANNEL_ID, text)
        print(f"✅ تم النشر بنجاح!")
    except Exception as e:
        print(f"❌ فشل النشر. السبب: {e}")
        print("تأكد أن البوت مشرف (Admin) في القناة وأن المعرف صحيح.")

if __name__ == "__main__":
    send_post()
