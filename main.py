import telebot
import os
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"
bot = telebot.TeleBot(BOT_TOKEN)

# هذه هي القائمة التي سيختار منها البوت عشوائياً
content_list = [
    {"t": "﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾", "s": "القرآن الكريم"},
    {"t": "﴿وَبَشِّرِ الصَّابِرِينَ﴾", "s": "القرآن الكريم"},
    {"t": "يَا مَنْ اسْمُهُ دَوَاءٌ وَذِكْرُهُ شِفَاءٌ.", "s": "مفاتيح الجنان"},
    {"t": "أَشَدُّ الذُّنُوبِ مَا اسْتَهَانَ بِهِ صَاحِبُهُ.", "s": "نهج البلاغة"},
    {"t": "اللهم صل على محمد وآل محمد وعجل فرجهم.", "s": "أذكار"},
    {"t": "أستغفر الله ربي وأتوب إليه.", "s": "تذكير"}
]

def send_random_post():
    try:
        # اختيار عشوائي من القائمة أعلاه
        item = random.choice(content_list)
        
        # تنسيق الرسالة النهائي
        final_message = (
            f"✨ {item['t']}\n\n"
            f"📖 المصدر: {item['s']}\n\n"
            f"🌿 صدقة جارية لروح المرحوم كاظم صالح خليفة"
        )
        
        bot.send_message(CHAT_ID, final_message)
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_random_post()
