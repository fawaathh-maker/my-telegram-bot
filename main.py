import os

try:
    import telebot
    from telebot import types
except ImportError:
    os.system('pip install pyTelegramBotAPI')
    import telebot
    from telebot import types

# التوكن الخاص بك
TOKEN = "8827423410:AAGMdjYyDIeVod1NpFozavtcH0gpYu3wYr4"
bot = telebot.TeleBot(TOKEN)

# عندما يضغط المستخدم على Start تظهر له الأزرار
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn1 = types.InlineKeyboardButton("📥 قسم البرامج المجانية", callback_data="programs")
    btn2 = types.InlineKeyboardButton("📱 قسم الأرقام والشروحات", callback_data="numbers")
    btn3 = types.InlineKeyboardButton("🔗 رابط قناتنا الرسمية", url="https://t.me/your_channel_username")
    
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "مرحباً بك في بوت الخدمات المجانية! اختر القسم الذي تريده من الأسفل👇:", reply_markup=markup)

# التحكم في ردود الأزرار عند الضغط عليها
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "programs":
        نص_البرامج = (
            "🚀 **قسم البرامج المجانية بروابط مباشرة:**\n\n"
            "1️⃣ تطبيق 1DM لتحميل الملفات بسرعة عالية.\n"
            "2️⃣ تطبيق كاب كات (CapCut) مهكر وبدون علامة مائية.\n\n"
            "اضغط على /start للعودة للقائمة الرئيسية."
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=نص_البرامج, parse_mode="Markdown")
        
    elif call.data == "numbers":
        # إنشاء أزرار داخلية مخصصة للأرقام والشروحات لتظهر للمستخدم
        markup_numbers = types.InlineKeyboardMarkup(row_width=1)
        
        # يمكنك تعديل هذه الروابط والأزرار ووضع روابط قناتك أو الأرقام مباشرة
        btn_num1 = types.InlineKeyboardButton("🇺🇸 احصل على رقم أمريكي جاهز", url="https://t.me/your_channel_username") 
        btn_num2 = types.InlineKeyboardButton("🤖 بوت توليد الأرقام المجانية", url="https://t.me/your_bot_username")
        btn_back = types.InlineKeyboardButton("⬅️ العودة للقائمة الرئيسية", callback_data="back_to_main")
        
        markup_numbers.add(btn_num1, btn_num2, btn_back)
        
        نص_الأرقام = (
            "📱 **قسم الأرقام المجانية والشروحات:**\n\n"
            "إليك الأرقام المتوفرة حالياً والشروحات الخاصة بها، اضغط على الزر المطلوب بالأسفل للحصول على الرقم أو الشرح المستهدف👇:"
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=نص_الأرقام, reply_markup=markup_numbers, parse_mode="Markdown")

    elif call.data == "back_to_main":
        # زر العودة للقائمة الرئيسية
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("📥 قسم البرامج المجانية", callback_data="programs")
        btn2 = types.InlineKeyboardButton("📱 قسم الأرقام والشروحات", callback_data="numbers")
        btn3 = types.InlineKeyboardButton("🔗 رابط قناتنا الرسمية", url="https://t.me/your_channel_username")
        
        markup.add(btn1, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="مرحباً بك في بوت الخدمات المجانية! اختر القسم الذي تريده من الأسفل👇:", reply_markup=markup)

print("البوت الاحترافي يعمل الآن بنجاح...")
bot.infinity_polling()
