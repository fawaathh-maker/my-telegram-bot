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

# معرف قناتك (يجب أن يبدأ بـ @ مثل @mychannel)
CHANNEL_ID = "@your_channel_username" 

def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def welcome(message):
    if not check_subscription(message.chat.id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("اشترك في القناة أولاً", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
        check_btn = types.InlineKeyboardButton("تحقق من الاشتراك", callback_data="check")
        markup.add(btn, check_btn)
        bot.send_message(message.chat.id, "❌ عذراً، يجب عليك الاشتراك في القناة أولاً لاستخدام البوت:", reply_markup=markup)
    else:
        show_main_menu(message.chat.id)

def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("📥 قسم البرامج", callback_data="programs")
    btn2 = types.InlineKeyboardButton("📱 قسم الأرقام", callback_data="numbers")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "مرحباً بك! اختر القسم:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "check":
        if check_subscription(call.message.chat.id):
            bot.answer_callback_query(call.id, "✅ شكراً لاشتراكك!")
            show_main_menu(call.message.chat.id)
        else:
            bot.answer_callback_query(call.id, "⚠️ لم تشترك بعد!")
            
    elif call.data == "programs":
        bot.edit_message_text("هنا توضع روابط البرامج بعد اختصارها.", call.message.chat.id, call.message.message_id)
    elif call.data == "numbers":
        bot.edit_message_text("قسم الأرقام العربية.", call.message.chat.id, call.message.message_id)

bot.infinity_polling()
