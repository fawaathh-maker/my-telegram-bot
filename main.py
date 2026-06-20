import os

try:
    import telebot
    from telebot import types
except ImportError:
    os.system('pip install pyTelegramBotAPI')
    import telebot
    from telebot import types

TOKEN = "8827423410:AAGMdjYyDIeVod1NpFozavtcH0gpYu3wYr4"
bot = telebot.TeleBot(TOKEN)

# معرف قناتك الجديدة
CHANNEL_ID = "@fawaathh_tech" 

def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking sub: {e}")
        return False

@bot.message_handler(commands=['start'])
def welcome(message):
    if not check_subscription(message.chat.id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("اشترك في القناة لتفعيل البوت 📢", url="https://t.me/fawaathh_tech")
        check_btn = types.InlineKeyboardButton("تحقق من الاشتراك ✅", callback_data="check")
        markup.add(btn, check_btn)
        bot.send_message(message.chat.id, "❌ عذراً، يجب عليك الاشتراك في قناتنا أولاً لاستخدام البوت:", reply_markup=markup)
    else:
        show_main_menu(message.chat.id)

def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("📥 قسم البرامج المجانية", callback_data="programs")
    btn2 = types.InlineKeyboardButton("📱 قسم الأرقام والشروحات", callback_data="numbers")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "مرحباً بك في بوت الخدمات المجانية! اختر القسم الذي تريده من الأسفل👇:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "check":
        if check_subscription(call.message.chat.id):
            bot.answer_callback_query(call.id, "✅ تم التحقق! شكراً لاشتراكك.")
            show_main_menu(call.message.chat.id)
        else:
            bot.answer_callback_query(call.id, "⚠️ لم تشترك بعد! اشترك في القناة أولاً.")
            
    elif call.data == "programs":
        نص_البرامج = "🚀 **قسم البرامج المجانية بروابط مباشرة:**\n\n1️⃣ تطبيق 1DM لتحميل الملفات.\n2️⃣ تطبيق كاب كات مهكر."
        bot.edit_message_text(text=نص_البرامج, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown")
        
    elif call.data == "numbers":
        نص_الأرقام = "📱 **قسم الأرقام والشروحات:**\n\nقريباً سيتم نشر أرقام وهمية مجانية هنا!"
        bot.edit_message_text(text=نص_الأرقام, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown")

print("البوت يعمل الآن بنجاح مع ميزة الاشتراك الإجباري...")
bot.infinity_polling()
