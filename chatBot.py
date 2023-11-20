import telegram
import asyncio
import pytz
import datetime

token = "6444123553:AAF2S-JS4Yywqj6Tlm5duo9ndzX0gGLhYFM"
bot = telegram.Bot(token = token)

public_chat_name = "@osproject_test"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    await bot.sendMessage(chat_id=public_chat_name, text="30분에 한번씩 알림 보내는 중 !")

async def schedule_jobs():
    while True:
        await job()  # 실행
        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(schedule_jobs())
