from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
    now = datetime.now()
    current_date_time = now.strftime("<strong>%A, %B %d %Y</strong> at <strong>%I:%M %p</strong>")
    return f"<p><strong>The current date time is:</strong> {current_date_time}</p>"

if __name__ == '__main__':
    app.run()

