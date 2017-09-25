from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simpleWeb/callback', methods=['POST'])
def callback():
    f = open('/data/ylfinCallback', 'a')
    for key in request.form:
        f.write(key + ':' + request.form[key])
        f.write("\t")
    f.write("\n")
    f.close()
    return 'SUCCESS'


if __name__ == '__main__':
    app.run()

