from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
WEBHOOK_URL = "https://discord.com/api/webhooks/1390721110567551036/6mFcNlUthjNZ4FNu9NHIirGFPZykYlepUT3xN3wIGhoy_IUiAck0EePUaslhO6yYy07I"

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    content = data.get("content", "Brak treści")
    r = requests.post(WEBHOOK_URL, json={"content": content})
    return jsonify({"status": "OK", "discord_status": r.status_code})

@app.route('/')
def home():
    return "Bot działa! Wyślij POST na /send"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
