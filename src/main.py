from typing import Final 
import os
from dotenv import load_dotenv
import logging

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from telegram import ForceReply, Update

load_dotenv()

BOT_TOKEN : Final[str] = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Oi! Leia os issues para conhecer o que planejamos adicionar como funcionalidades ao bot!")

#quando não encontra nenhum comando ou outro trigger corresponde
async def respostaGeral(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Oops! comando inválido, envie /Help para listar os comandos!")

def main():
    "Função princpal com os triggers do bot"
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respostaGeral))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

