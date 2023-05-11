from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my domain.'

if __name__ == '__main__':
    app.run(host='https://mzari.tech/')