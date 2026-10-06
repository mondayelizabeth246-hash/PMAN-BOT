import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Fetch Environment Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
REGISTER_URL = os.getenv("REGISTER_URL", "https://ufanext.cc/register/")
WEBSITE_URL = os.getenv("WEBSITE_URL", "https://ufanext.cc")

# Promotional banner image filename saved in your repository
IMAGE_FILENAME = "photo_2026-10-06_12-51-51.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = user.first_name if user else "ลูกค้า"

    # Welcome message caption
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

    # Inline action buttons
    keyboard = [
        [InlineKeyboardButton("🎲 สมัครสมาชิก", url=REGISTER_URL)],
        [InlineKeyboardButton("📲 เข้าสู่เว็บไซต์", url=WEBSITE_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Check for local image file and send it with caption and buttons
    if os.path.exists(IMAGE_FILENAME):
        with open(IMAGE_FILENAME, "rb") as photo_file:
            await update.message.reply_photo(
                photo=photo_file,
                caption=caption,
                reply_markup=reply_markup
            )
    else:
        # Fallback if image file is not found
        fallback_image_url = os.getenv("IMAGE_URL", "https://ufanext.cc/logo.png")
        await update.message.reply_photo(
            photo=fallback_image_url,
            caption=caption,
            reply_markup=reply_markup
        )

def main() -> None:
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set!")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Railway server integration (supports Webhook and Long Polling)
    port = int(os.getenv("PORT", 8080))
    webhook_url = os.getenv("RAILWAY_STATIC_URL")

    if webhook_url:
        full_webhook_url = f"https://{webhook_url}/{BOT_TOKEN}"
        logging.info(f"Setting webhook to {full_webhook_url}")
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=BOT_TOKEN,
            webhook_url=full_webhook_url
        )
    else:
        logging.info("Starting long polling mode...")
        app.run_polling()

if __name__ == "__main__":
    main()
