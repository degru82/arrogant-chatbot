"""
Telegram Echo Bot

A simple Telegram chatbot that echoes back user messages.
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the /start command is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! I'm an echo bot. "
        "Send me any message and I'll repeat it back to you!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message when the /help command is issued."""
    await update.message.reply_text(
        "I'm an echo bot! Here's what I can do:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "Just send me any text message and I'll echo it back to you!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Get the bot token from environment variable
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

    # Create the Application
    application = Application.builder().token(token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot using polling
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
