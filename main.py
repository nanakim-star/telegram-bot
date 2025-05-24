from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("7622493232:AAFtDWDvx8giDqSOmuH4K6QB9m5K3ljCzRs")  # Render 환경변수에서 토큰 불러오기
CHAT_ID = os.getenv("4831865253")  # 메시지를 보낼 그룹방 ID

bot = Bot(token=TOKEN)

async def send_periodic_message():
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="🎯 Welcome! ZERO ROOM에 오신것을 환영합니다!")
            print("메시지 전송됨")
        except Exception as e:
            print(f"오류 발생: {e}")
        await asyncio.sleep(180)  # 3분 = 180초

if __name__ == "__main__":
    print("봇 자동 메시지 시작됨...")
    asyncio.run(send_periodic_message())
