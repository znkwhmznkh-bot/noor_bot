import telebot
import os
import time
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"

bot = telebot.TeleBot(BOT_TOKEN)

intro_list = [
    "🌿 صدقة جارية",
    "🤍 عمل خير لروح فقيدنا",
    "🌸 دعاء ورحمة",
    "📿 ثواب مستمر"
]

dua_list = [
    "اللهم ارحم واغفر لروح المرحوم كاظم صالح خليفة",
    "اللهم اجعل قبره روضة من رياض الجنة",
    "اللهم نور قبره ووسع مدخله",
    "اللهم ابدله داراً خيراً من داره"
]

closing_list = [
    "نسألكم قراءة سورة الفاتحة مع الصلاة على محمد وآل محمد 🌿",
    "الفاتحة مع الصلاة على النبي وآله الكرام 🤍",
    "نرجو الدعاء وقراءة الفاتحة 🌸",
    "اللهم صلِّ على محمد وآل محمد مع الفاتحة"
]

posts = []

for i in range(1, 501):
    post = f"""{random.choice(intro_list)} رقم {i}

بثواب روح والدي المرحوم كاظم صالح خليفة 🤍
{random.choice(dua_list)}

{random.choice(closing_list)}
"""
    posts.append(post)

index = 0

def send_post():
    global index
    try:
        bot.send_message(CHAT_ID, posts[index])
        print(f"تم نشر: {index+1}")

        index += 1

        if index >= len(posts):
            bot.send_message(CHAT_ID, "✅ تم نشر جميع المنشورات (500) بنجاح")
            index = 0

    except Exception as e:
        print(e)

while True:
    send_post()
    time.sleep(3 * 60 * 60)
