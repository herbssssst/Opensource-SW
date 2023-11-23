# OpenSource-SW-Telegram-Bot-ChatGPT
**2023-2 오픈소스 SW 실습 강의 3번째 과제 (텔레그램 봇 with ChatGPT)**
📢 2번 과제와 연동하여 ChatGPT 연결 과제 (단, 카드를 적용하지 않을 경우도 동일하게 제출) <br/>
📢 2번 과제에 개설한 채널로 ChatGPT 연동 결과 제출 <br/>
    - 하지만, 채널로 연동하게 되면 자신의 계정은 관리자로 되어 채널에 메시지가 보내지지 않고 BOT으로 메시지가 보내지기 때문에 채널과 연동하지 않고 그냥 BOT과 연동하여 진행하였다. <br/>

📢 단, 카드 정보를 OpanAI에 제시하지 않을 학생들은 해당 코드에 별도의 텍스트 문자만 전달하는 Echo 함수 작성 <br/>

<br/><br/>

**텍스트 문자를 전달하는 ECHO 함수** <br/>
```
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
```

<br/><br/>

**실행 결과**
<img width="587" alt="CHATGPT" src="https://github.com/herbssssst/OpenSource-SW-Telegram-Bot-ChatGPT/assets/98319466/134993fc-f345-482f-9636-93d9793eacb6">
