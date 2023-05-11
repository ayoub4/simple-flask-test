from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my domain.'

if __name__ == '__main__':
    app.run(host='mzari.me', port=443)