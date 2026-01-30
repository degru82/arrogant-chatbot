"""
Telegram Echo Bot
A simple bot that repeats everything the user sends.
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm an echo bot. Send me any message and I'll repeat it back to you!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "I'm a simple echo bot. Just send me any text, photo, or sticker and I'll repeat it back to you!\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )


async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user text message."""
    await update.message.reply_text(update.message.text)


async def echo_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user photo."""
    photo = update.message.photo[-1]  # Get the largest photo
    caption = update.message.caption if update.message.caption else ""
    await update.message.reply_photo(photo=photo.file_id, caption=caption)


async def echo_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user sticker."""
    await update.message.reply_sticker(sticker=update.message.sticker.file_id)


async def echo_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user voice message."""
    await update.message.reply_voice(voice=update.message.voice.file_id)


async def echo_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user video."""
    caption = update.message.caption if update.message.caption else ""
    await update.message.reply_video(video=update.message.video.file_id, caption=caption)


async def echo_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user document."""
    caption = update.message.caption if update.message.caption else ""
    await update.message.reply_document(document=update.message.document.file_id, caption=caption)


def main() -> None:
    """Start the bot."""
    # Get bot token from environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
        raise ValueError("TELEGRAM_BOT_TOKEN must be set")

    # Create the Application
    application = Application.builder().token(token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Register message handlers for different content types
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))
    application.add_handler(MessageHandler(filters.PHOTO, echo_photo))
    application.add_handler(MessageHandler(filters.Sticker.ALL, echo_sticker))
    application.add_handler(MessageHandler(filters.VOICE, echo_voice))
    application.add_handler(MessageHandler(filters.VIDEO, echo_video))
    application.add_handler(MessageHandler(filters.Document.ALL, echo_document))

    # Start the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
