import os
import requests
import telegram.ext
TOKEN = '1917773290:AAFK2yGFDJCUwLcdmiIdn8VfVGcOtPLwQ6A'
def start(update, context):
  update.message.reply_text("أخبرني عن ماذا تريد أن تتحدث؟")
def chab(update, context):
  A = requests.get(f'https://w-aqol.com/search?s={update.message.text}').text
  A = A.split("<td>")[2]
  RD = A.split("</td>")[0]
  print(RD)
  update.message.reply_text(RD)
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, chab))
updater.start_polling()
updater.idle()
