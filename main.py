from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ChatMemberHandler

import os

TOKEN = os.getenv("BOT_TOKEN")

# /start 명령어 처리
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Welcome! ZERO ROOM에 오신 걸 환영합니다!")

# 단톡방에 새 멤버가 들어왔을 때 자동 환영 메시지 보내기
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_member = update.chat_member.new_chat_member.user
    await update.effective_chat.send_message(
        f"👋 {new_member.full_name}님, 환영합니다! 즐거운 시간 보내세요!"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

print("봇 실행 중...")
app.run_polling()
