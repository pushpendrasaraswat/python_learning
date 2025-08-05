import flask
import requests


Gender_URL ="https://api.genderize.io?name=<name>"
AGE_URL ="https://api.agify.io/?name=<name>"

app = flask.Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(Gender_URL.replace("<name>", name))
    data = response.json()
    print(data)
    gender = data['gender']
    response_age = requests.get(AGE_URL.replace("<name>", name))
    age = response_age.json()["age"]
    print(response_age.json())
    print(age, gender)
    return flask.render_template('index.html', name=name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app on port 5000
