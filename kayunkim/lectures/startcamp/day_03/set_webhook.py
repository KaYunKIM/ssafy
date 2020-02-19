from decouple import config
import requests 


token = config("TELEGRAM_BOT_TOKEN")
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'https://c8b9cbae.ngrok.io'
python_anywhere_url = 'gayun1109.pythonanywhere.com'

set_webhook_url = f'{app_url}/setWebhook?url={python_anywhere_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)


