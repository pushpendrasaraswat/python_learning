from flask import Flask

from decorator_app import make_bold
from decorator_app import make_italic
from decorator_app import make_underline

app = Flask(__name__)

# to start the server, run the command: flask --app hello run


@app.route('/')
def hello():
    return '<Strong>Hello, World!</Strong>'

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'Bye!'

@app.route('/<name>/<int:age>')
def greet(name,age):
    return f'<Strong>Hello  {name}!, you are {age} years old.</Strong>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)