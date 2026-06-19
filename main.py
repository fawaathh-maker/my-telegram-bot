import os

try:
    import telebot
    from telebot import types
except ImportError:
    os.system('pip install pyTelegramBotAPI')
    import telebot
    from telebot import types

# ⚠️ ضع التوكن الجديد الخاص بك هنا بين علامات التنصيص
TOKEN = "8827423410:AAGMdjYyDIeVod1NpFozavtcH0gpYu3wYr4"
bot = telebot.TeleBot(TOKEN)

# عندما يضغط المستخدم على Start تظهر له الأزرار
@bot.message_handler(commands=['start'])
def welcome(message):
    # إنشاء لوحة الأزرار
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # تعريف الأزرار (يمكنك تغيير الأسماء المكتوبة بالعربي كما تحب)
    btn1 = types.InlineKeyboardButton("📥 قسم البرامج المجانية", callback_data="programs")
    btn2 = types.InlineKeyboardButton("📱 قسم الأرقام والشروحات", callback_data="numbers")
    btn3 = types.InlineKeyboardButton("🔗 رابط قناتنا الرسمية", url="https://t.me/your_channel_username") # ضع رابط قناتك هنا بدل your_channel_username
    
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, "مرحباً بك في بوت الخدمات المجانية! اختر القسم الذي تريده من الأسفل👇:", reply_markup=markup)

# التحكم في ردود الأزرار عند الضغط عليها
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "programs":
        # النص الذي يظهر عند الضغط على زر البرامج
        نص_البرامج = (
            "🚀 **قسم البرامج المجانية بروابط مباشرة:**\n\n"
            "1️⃣ تطبيق 1DM لتحميل الملفات بسرعة عالية.\n"
            "2️⃣ تطبيق كاب كات (CapCut) مهكر وبدون علامة مائية.\n\n"
            "اضغط على /start للعودة للقائمة الرئيسية."
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=نص_البرامج, parse_mode="Markdown")
        
    elif call.data == "numbers":
        # النص الذي يظهر عند الضغط على زر الأرقام
        نص_الأرقام = (
            "📱 **قسم الأرقام والشروحات:**\n\n"
            "قريباً سيتم نشر أرقام وهمية مجانية لتفعيل الواتساب والتليجرام مباشرة من هنا! انتظرونا."
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nص_الأرقام, parse_mode="Markdown")

print("البوت الاحترافي يعمل الآن بنجاح...")
bot.infinity_polling()
