import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
REGISTER_URL = "https://ufanext.cc/register/"
WEBSITE_URL = "https://ufanext.cc"
IMAGE_FILE = "photo_2026-10-06_12-51-51.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.first_name if user else "ลูกค้า"

    caption = (
        f"สวัสดี {username} ยินดีต้อนรับสู่ เว็บ UFANEXT ตรงจาก UFABET! 🎉\n"
        f"🧧💥 สมัครวันนี้รับเครดิตฟรี 300 บาท หรือฟรีสปิน 300 ครั้ง 💥🧧\n\n"
        f"🎰 คืนเงินเดิมพันทุกวัน!\n\n"
        f"❤️ แจ็คพอตแตกทุกชั่วโมง! 😮 คุณอาจเป็นคนต่อไป 🔥\n"
        f"🎁 ลุ้นโชคกับรางวัล LUCKY SPIN REWARDS !!\n\n"
        f"💥รับรางวัลเงินสด! 20,545,200 บาท ที่นี่!!💥\n\n"
        f"เราให้โบนัสต้อนรับ 1,500 บาท แก่คุณหากเข้าร่วมวันนี้!!\n"
        f"🎲 สมัครคลิ๊ก {REGISTER_URL}\n\n"
        f"📲 เว็บ UFANEXT {WEBSITE_URL}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎲 สมัครสมาชิก", url=REGISTER_URL)],
        [InlineKeyboardButton("📲 เข้าสู่เว็บไซต์", url=WEBSITE_URL)]
    ])

    if os.path.exists(IMAGE_FILE):
        with open(IMAGE_FILE, "rb") as photo:
            await update.message.reply_photo(photo=photo, caption=caption, reply_markup=keyboard)
    else:
        await update.message.reply_text(caption, reply_markup=keyboard)

def main():
    if not BOT_TOKEN:
        raise ValueError("Please add BOT_TOKEN to your Railway Variables!")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
