import telegram
import sys
import ChatModel

#API 기본 설정
test_token = 'mytoken'
test = telegram.Bot(token = test_token)
updates = test.getUpdates()
for u in updates:
    print(u.message)

def proc_alert(bot, update):
    test.sendMessage("그러고도 잠이 오냐ㅋㅋㅋ")
    sound=firecracker()
    test.sendMessage(sound)
    test.sendMessage("ㅋㅋㅋㅋㅋㅋ")

def proc_stop(bot, update):
    test.sendMessage("빠잉~")
    test.stop()

def firecracker():
    return "에베베베베베베"


test=ChatModel.BotTest()
test.add_handler("alert", proc_alert)
test.add_handler("stop",proc_stop)
test.start()
