import telebot
import os
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"
bot = telebot.TeleBot(BOT_TOKEN)

content_list = [
    {"t": "﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾", "s": "القرآن الكريم"},
    {"t": "﴿وَبَشِّرِ الصَّابِرِينَ﴾", "s": "القرآن الكريم"},
    {"t": "أَشَدُّ الذُّنُوبِ مَا اسْتَهَانَ بِهِ صَاحِبُهُ.", "s": "نهج البلاغة"},
    {"t": "اللهم صل على محمد وآل محمد وعجل فرجهم.", "s": "أذكار"}
]

def send_random_post():
    try:
        item = random.choice(content_list)
        # أضفت كلمة (تحديث) لنعرف أنه الكود الجديد
        msg = f"✅ تحديث: {item['t']}\n\n📖 المرجع: {item['s']}\n\n🌿 صدقة جارية لروح المرحوم كاظم صالح خليفة"
        bot.send_message(CHAT_ID, msg)
        print("Done")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_random_post()
