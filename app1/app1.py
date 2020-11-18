from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    html = "<h3>The system is up and running: {name}!</h3>" \
           "<b>Docker App1</b> <br/>"
    return 'Docker, App1!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
