# SW-OpenSource-Telegram-Bot


2023-2오픈소스 SW 실습 강의 2번째 과제 (텔레그램 봇) <br/>
📢 30분 단위로 개설 채널에 메시지 전송 <br/>
📢 오후 11시 부터 아침 6시까지는 메시지 출력 금지<br/>
<br/>
<br/>
<br/>
_30분 단위 메시지 전송  및 전송 시간 제한 코드_<br/>
<br/>

`
def job():

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    #if now.hour >= 23 or now.hour <= 6:
    #    return

    asyncio.run(bot.sendMessage(chat_id=public_chat_name, text="30분에 한번씩 알림 보내는 중 !"))

schedule.every(30).minutes.do(job)`
<br/>
<br/>
<br/>
_실행 결과_<br/>
