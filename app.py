from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return('Labas!')

@app.route('/puslapis')
def puslapis():
    return('kitas puslapis')


if __name__ == '__main__':
    app.run('localhost', '80')
