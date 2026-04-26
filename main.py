import telebot
import os
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = "@Norham313"
bot = telebot.TeleBot(BOT_TOKEN)

# قائمة المحتوى: صور دينية + نصوص دينية
content_list = [
    {"type": "photo", "t": "﴿فَسَبِّحْ بِحَمْدِ رَبِّكَ وَاسْتَعِنْهُ﴾", "s": "سورة النصر", "img": "https://images.unsplash.com/photo-1519817650390-64a93db51149?w=800"},
    {"type": "text", "t": "اللهم ارحم من غابوا عنا وجعل قبورهم روضة من رياض الجنة.", "s": "دعاء للميت"},
    {"type": "photo", "t": "﴿إِنَّ اللَّهَ مَعَ الصَّابِرِينَ﴾", "s": "سورة البقرة", "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800"},
    {"type": "text", "t": "أستغفر الله العظيم لي ولوالدي وللمؤمنين والمؤمنات.", "s": "أذكار"},
    {"type": "photo", "t": "يا رب اجعل قبر كل غالٍ فقدناه برداً وسلاماً.", "s": "مناجاة", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800"},
    {"type": "text", "t": "﴿وَآتَاكُم مِّن كُلِّ مَا سَأَلْتُمُوهُ﴾", "s": "سورة إبراهيم"},
    {"type": "photo", "t": "صلوا على من يشفع لنا يوم القيامة..", "s": "اللهم صل على محمد وآل محمد", "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800"},
    {"type": "text", "t": "سبحان الله، والحمد لله، ولا إله إلا الله، والله أكبر.", "s": "الباقيات الصالحات"},
    {"type": "photo", "t": "﴿وَأُفَوِّضُ أَمْرِي إِلَى اللَّهِ﴾", "s": "سورة غافر", "img": "https://images.unsplash.com/photo-1470252649358-96957c053e9a?w=800"},
    {"type": "text", "t": "يا رب إنك عفو كريم تحب العفو فاعفُ عنا.", "s": "أدعية"},
    {"type": "photo", "t": "اللهم ارحم (كاظم صالح خليفة) واغفر له.", "s": "صدقة جارية", "img": "https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=800"},
    {"type": "text", "t": "لا إله إلا أنت سبحانك إني كنت من الظالمين.", "s": "دعاء ذي النون"}
]

def send_random_post():
    try:
        item = random.choice(content_list)
        # هنا العبارة التي تضمن الثواب للوالد وتظهر أسفل كل منشور
        caption = f"✨ {item['t']}\n\n📖 المصدر: {item['s']}\n\n🌿 صدقة جارية لروح المرحوم كاظم صالح خليفة"
        
        if item['type'] == "photo":
            bot.send_photo(CHAT_ID, item['img'], caption=caption)
        else:
            bot.send_message(CHAT_ID, caption)
            
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_random_post()
