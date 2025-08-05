import flask
import random
app = flask.Flask(__name__)

random_number = random.randint(1, 10)

@app.route('/')
def guess_a_number():
    return ('<h1>Guess a Number Game</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>')

@app.route('/<int:number>')
def guess_a_number_start(number):
    if random_number > number:
        return ('<h3>Too low, try again!</h3>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')
    elif random_number < number:
        return ('<h3>Too High, try again!</h3>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    else:
        return ('<h3>Congratulations! You guessed it right {random_number}!</h3>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')


if __name__ == '__main__':
    app.run(debug=True)
