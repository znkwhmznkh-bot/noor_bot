import telebot
import os
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"
bot = telebot.TeleBot(BOT_TOKEN)

content_list = [
    {"t": "﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾", "s": "القرآن الكريم"},
    {"t": "﴿وَبَشِّرِ الصَّابِرِينَ﴾", "s": "القرآن الكريم"},
    {"t": "﴿اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ﴾", "s": "سورة البقرة"},
    {"t": "يَا مَنْ اسْمُهُ دَوَاءٌ وَذِكْرُهُ شِفَاءٌ.", "s": "مفاتيح الجنان"},
    {"t": "أَشَدُّ الذُّنُوبِ مَا اسْتَهَانَ بِهِ صَاحِبُهُ.", "s": "نهج البلاغة"},
    {"t": "اللهم صل على محمد وآل محمد وعجل فرجهم.", "s": "أذكار"},
    {"t": "أستغفر الله ربي وأتوب إليه.", "s": "تذكير"}
]

def send_random_post():
    try:
        item = random.choice(content_list)
        # هذا السطر هو اللي يغير الرسالة، تأكد ماكو قبله علامة #
        msg = f"✨ {item['t']}\n\n📖 المرجع: {item['s']}\n\n🌿 صدقة جارية لروح المرحوم كاظم صالح خليفة"
        bot.send_message(CHAT_ID, msg)
        print("Done")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_random_post()
