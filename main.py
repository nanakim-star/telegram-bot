from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio

# 봇 토큰 및 Webhook URL 환경변수에서 불러오기
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# FastAPI 앱 생성
app = FastAPI()

# Telegram Bot Application 초기화
telegram_app = Application.builder().token(TOKEN).build()

# /start 명령 처리 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Welcome ZERO ROOM에 오신 걸 환영합니다!")

# 핸들러 등록
telegram_app.add_handler(CommandHandler("start", start))

# 웹훅 라우트 정의
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}

# 서버 시작 시 Webhook 등록
@app.on_event("startup")
async def startup_event():
    await telegram_app.bot.set_webhook(url=WEBHOOK_URL)

# 종료 시 Webhook 제거 (선택사항)
@app.on_event("shutdown")
async def shutdown_event():
    await telegram_app.bot.delete_webhook()
