from flask import Flask
import MainScores
app = Flask(__name__)

@app.route('/')
def hello():
	return MainScores.score_server(3)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)