from flask import Flask

app = Flask(_name_)

@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
