from flask import Flask  # type: ignore[import]
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from My DevOps Pipeline!"

@app.route('/health')
def health():
    return {"status": "healthy"}    