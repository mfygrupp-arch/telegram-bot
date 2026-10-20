import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest

BOT_TOKEN = "8952988531:AAGgC75p5DmLnSDppcNYPnA6vodJnm-XNmc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def auto_approve(request: ChatJoinRequest):
    try:
        await request.approve()
        print(f"Onaylandi: {request.from_user.full_name}")
    except Exception as e:
        print(f"Hata olustu: {e}")

async def main():
    print("Yeni bot baslatiliyor...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
