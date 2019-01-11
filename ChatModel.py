import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core=telegram.Bot(token)
        self.updater=Updater(token)
        self.id="684198776"
        self.name=name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotTest(TelegramBot):
    def __init__(self):
        self.token='mytoken'
        TelegramBot.__init__(self, "테스트",self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd,func))

    def start(self):
        self.sendMessage("테스트 봇 시험 운행 시작")
        self.updater.start_polling()
        self.updater.idle()
