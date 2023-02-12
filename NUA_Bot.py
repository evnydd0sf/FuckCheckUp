#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

import logging
import requests
from bs4 import BeautifulSoup

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BOOKNAME, PICKBOOK, LOCATION, BIO = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "你好，欢迎使用 NUA-图书馆助手。请输入想要查询的书籍名称",
        reply_markup=ReplyKeyboardRemove(),
    )
    return BOOKNAME

async def bookName(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Book of %s: %s", user.first_name, update.message.text)
    bookCount = len(list)
    result = requests.get("http://10.20.108.131:8080/opac/openlink.php?strSearchType=title&match_flag=forward&historyCount=1&strText="+update.message.text+"&doctype=ALL&with_ebook=on&displaypg=20&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL")
    soup = BeautifulSoup(result.text, "html.parser")
    list = soup.select('.book_list_info')
    if len(list) == 0:
        await update.message.reply_text("没有找到相关书籍",
        reply_markup=ReplyKeyboardRemove(),
        )
    else:
        if bookCount > 10:
            bookCount = 10
        else: bookCount = len(list)
        book = ""
        # bookLink = []
        for i in range(bookCount):
            name = soup.select('.book_list_info h3 a')[i].text
            # link = soup.select('.book_list_info h3 a')[i].get('href')
            link = "http://baidu.com"
            hyperName = "<a href=" + link + ">" + name + "</a>"
            
            number = soup.select('.book_list_info p span')[i].text.replace(" ", "").replace("\t", "").replace("(0)馆藏", "")
            author = soup.select('.book_list_info p')[i].text.replace(" ", "").replace("\t", "").replace(number, "").replace("(0)馆藏", "")
            book += hyperName + "\n" + author + number + "\n\n"
            # bookLink.append(soup.select('.book_list_info h3 a')[i]['href'][17:65])
        await update.message.reply_text(
            "好的，找到了这些：\n\n" + book + "重新查询？ 试试 /retry", 
            # parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove(),
        )
    return PICKBOOK

async def pick(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Book of %s: %s", user.first_name, update.message.text)
    # bookLink
    await update.message.reply_text(
        "Gorgeous! Now, send me your location please, or send /skip if you don't want to."
    )

    return LOCATION


async def skip_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    await update.message.reply_text(
        "I bet you look great! Now, send me your location please, or send /skip."
    )

    return LOCATION


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    await update.message.reply_text(
        "Maybe I can visit you sometime! At last, tell me something about yourself."
    )

    return BIO


async def skip_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Skips the location and asks for info about the user."""
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    await update.message.reply_text(
        "You seem a bit paranoid! At last, tell me something about yourself."
    )

    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thank you! I hope we can talk again some day.")

    return ConversationHandler.END

async def retry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "你好，输入想要查询的书籍名称",
        reply_markup=ReplyKeyboardRemove(),
    )
    return BOOKNAME

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5426940917:AAGRlAmtYwvkr_3RZrASLoWjoW54s6oMhbU").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            BOOKNAME: [MessageHandler(filters.TEXT, bookName)],
            PICKBOOK: [MessageHandler(filters.TEXT & ~filters.COMMAND, pick), CommandHandler("retry", retry)],
            LOCATION: [
                MessageHandler(filters.LOCATION, location),
                CommandHandler("skip", skip_location),
            ],
            BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()