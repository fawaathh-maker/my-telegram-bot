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
    except:
        return False

@bot.message_handler(commands=['start'])
def welcome(message):
    if not check_subscription(message.chat.id):
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("اشترك في القناة لتفعيل البوت 📢", url=f"https://t.me/fawaathh_tech")
        check_btn = types.InlineKeyboardButton("تحقق من الاشتراك ✅", callback_data="check")
        markup.add(btn, check_btn)
        bot.send_message(message.chat.id, "❌ عذراً، يجب عليك الاشتراك في قناتنا أولاً لاستخدام البوت:", reply_markup=markup)
    else:
        show_main_menu(message.chat.id)

def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("📥 قسم البرامج", callback_data="programs")
    btn2 = types.InlineKeyboardButton("📱 قسم الأرقام", callback_data="numbers")
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "أهلاً بك! اختر القسم الذي تريده من الأسفل:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "check":
        if check_subscription(call.message.chat.id):
            bot.answer_callback_query(call.id, "✅ شكراً لاشتراكك!")
            show_main_menu(call.message.chat.id)
        else:
            bot.answer_callback_query(call.id, "⚠️ لم تشترك بعد!")
            
    elif call.data == "programs":
        bot.edit_message_text("هنا ستجد روابط البرامج المجانية.", call.message.chat.id, call.message.message_id)
    elif call.data == "numbers":
        bot.edit_message_text("سيتم نشر الأرقام في القناة قريباً.", call.message.chat.id, call.message.message_id)

bot.infinity_polling()
