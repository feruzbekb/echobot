from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from settings import TOKEN
from callbacks import start, help, send_menu


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(
        handler=CommandHandler(command=["start", "boshlash"], callback=start)
    )
    dispatcher.add_handler(
        handler=CommandHandler(command=["help", "yordam"], callback=help)
    )

    # message handlers
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("Menu"),
            callback=send_menu,
        )
    )

    updater.start_polling()
    updater.idle()


main()
