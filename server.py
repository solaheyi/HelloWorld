from flask import Flask

PORT = 8000
MESSAGE = 'Hello World'
app = Flask(__name__)

def root():
    result = MESSAGE.encode('utf-8')
    return result

@app.route('/helloworld')
def hello():
    return MESSAGE


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')


