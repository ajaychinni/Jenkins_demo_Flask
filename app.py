from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask to the world of systemd!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
