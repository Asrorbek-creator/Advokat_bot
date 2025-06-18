from docx import Document

# Create a new README-style document
doc = Document()
doc.add_heading('README – Advokat Bot (Telegram)', level=1)

doc.add_paragraph("""
🇺🇿 Ushbu loyiha — Telegram orqali foydalanuvchilarga yuridik xizmatlar ko‘rsatish uchun mo‘ljallangan botdir.
Bu bot aiogram kutubxonasi asosida yozilgan va Render platformasida ishlaydi.
""")

doc.add_heading('📁 Loyihaning Tuzilishi', level=2)
doc.add_paragraph("""
- advokat_bot.py – Bot kodi (asosiy fayl)
- requirements.txt – Zaruriy Python kutubxonalari roʻyxati
- README.md – Ushbu hujjat

*Ixtiyoriy:* `.env` fayli agar siz localda ishga tushirsangiz (Renderda kerak emas)
""")

doc.add_heading('🚀 Deploy qilish (Render)', level=2)
doc.add_paragraph("""
1. https://render.com saytiga kiring va GitHub bilan login qiling.
2. "New → Web Service" tanlang.
3. GitHub'dan `Advokat_bot` repozitoriyasini tanlang.
4. Quyidagilarni to'ldiring:
   - Build Command: pip install -r requirements.txt
   - Start Command: python advokat_bot.py
5. Environment Variables qismiga quyidagilarni kiriting:
   - BOT_TOKEN = sizning Telegram bot tokeningiz
6. "Create Web Service" tugmasini bosing.
7. Logs oynasida `Bot is running...` chiqishini kuting.
""")

doc.add_heading('✅ Foydalanish', level=2)
doc.add_paragraph("""
1. Telegram'da botingizga /start yuboring.
2. Bot avtomatik javob beradi.
""")

doc.add_heading('📞 Bog‘lanish', level=2)
doc.add_paragraph("""
Agar sizga yordam kerak bo‘lsa: @Dtx_ache (Telegram orqali)
""")

# Save the document
output_path = "/mnt/data/README_Advokat_Bot.docx"
doc.save(output_path)

output_path
