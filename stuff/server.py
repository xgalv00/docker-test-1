from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<body>Hello world. <a href="/about/">About this page</a>.</body>'


@app.route('/about')
def about():
    return '<body>This is the about page</body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
