import telebot

# 텔레그램 봇 토큰
bot_token = "6444123553:AAF2S-JS4Yywqj6Tlm5duo9ndzX0gGLhYFM"

# 채널 ID
#channel_id = "@osproject_test"

# 봇 인스턴스 생성
bot = telebot.TeleBot(bot_token)

# 유저가 입력한 메시지를 처리하는 함수 정의
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.from_user.id != bot.get_me().id:
        if message.text.lower() == '안녕':
            bot.reply_to(message, '안녕하세요')
        elif message.text.lower() == '오늘 날씨는 어때?':
            bot.reply_to(message, '오후 5시경 소나기와 우박이 내렸습니다.')
        else:
            bot.reply_to(message,'죄송합니다. 다른 질문을 해주세요')

# 봇 실행
bot.polling()
