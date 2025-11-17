from flask import Flask
from threading import Thread

port = int(os.environ.get("PORT", 8080)) # Just get the port to avoid 502 bad gateway error.

app = Flask('')
@app.route('/')
def home():
    return "Discord bot OK"

def run():
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
