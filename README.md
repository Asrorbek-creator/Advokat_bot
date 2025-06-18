# Advokat_bot
# Advokat Telegram Bot

## Tavsif
Bu bot quyidagi funksiyalarni bajaradi:
- Uchrashuv band qilish
- PDF/rasm hujjat qabul qilish
- FAQ bo‘limi
- Orqa tarafda admin (`+998975017003`) ga xabarlar yuboradi

Sozlashlar:
- `BOT_TOKEN` va `ADMIN_CHAT_ID` joylarini o‘zingizga moslang.

## Joylashtirish Railways’da
1. GitHub’da yangi repo yarating (+ `advokat_bot.py`, `requirements.txt`, `README.md` yuklang)
2. Railway’da:
   - “New Project” → “Deploy from GitHub”
   - Sizdagi `advokat_bot` repo’sini tanlang
3. `BOT_TOKEN` va `ADMIN_CHAT_ID` ni sozlamalar → Environment Variables bo‘limiga qo‘shing
4. Deploy tugmasini bosing — hammasi avtomatik ishga tushadi
