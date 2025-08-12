import flask

app = flask.Flask(__name__)

@app.route('/' , methods=['POST'])
def home():
    data = flask.request.get_json()
    return f'<h1>form received for name : {data["name"]} ,  email : {data["email"]}</h1>'



if __name__ == '__main__':
    app.run(debug=True)