from flasj import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Olá, coloque o nome na URL assim: /Oi"

@app.route("/<nome>")
def mensagem(nome):
	return f"oi, se está vendo esta mensagem é porque conseguiu ;*"

if __name__ == "__main__"
	app.run(host="0.0.0.0", port=5000)
