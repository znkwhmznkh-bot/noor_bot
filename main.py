import telebot
import random
import os

# الإعدادات
API_TOKEN = os.getenv('BOT_TOKEN') 
CHANNEL_ID = '@nour_min_nouruhum' 

bot = telebot.TeleBot(API_TOKEN)

messages = [
    "عن الإمام علي (ع): «أكرم ضيفك وإن كان حقيراً، وقم عن مجلسك لأبيك ومعلمك وإن كنت أميراً»",
    "قالت السيدة فاطمة الزهراء (ع): «فرض الله الصيام تثبيتاً للإخلاص»",
    "عن السيدة زينب (ع): «ما رأيت إلا جميلاً»",
    "اللهم ارحم (كاظم صالح خليفة) واغفر له واسكنه فسيح جناتك.",
    "تذكير: سبحان الله وبحمده، سبحان الله العظيم."
]

def check_and_send():
    try:
        # طباعة المعرف للتأكد
        print(f"📡 محاولة الاتصال بالقناة: {CHANNEL_ID}")
        
        # تجربة جلب معلومات القناة للتأكد من المعرف والصلاحيات
        chat = bot.get_chat(CHANNEL_ID)
        print(f"✅ تم العثور على القناة: {chat.title}")
        print(f"🆔 آيدي القناة: {chat.id}")

        # اختيار نص ونشره
        text = random.choice(messages)
        bot.send_message(CHANNEL_ID, text)
        print(f"🚀 تم النشر بنجاح!")

    except Exception as e:
        print(f"❌ فشل في الوصول للقناة أو النشر.")
        print(f"⚠️ نوع الخطأ: {e}")
        print("💡 نصيحة: تأكد أن القناة 'عامة' وليست 'خاصة'، وأن البوت 'مشرف' (Admin).")

if __name__ == "__main__":
    check_and_send()
