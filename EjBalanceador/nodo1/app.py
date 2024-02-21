from flask import Flask
app = Flask(__name__)

@app.route("/")
def mensaje():
	return "Hola desde el nodo 1!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
