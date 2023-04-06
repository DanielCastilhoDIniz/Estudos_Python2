"""
criando api com flask
"""

from flask import Flask


app = Flask(__name__)

# criando rota


@app.route("/<numero>", methods=['GET', 'POST'])
def ola(numero):
    return f'olá mundo. {numero}'


if __name__ == "__main__":
    app.run(debug=True)
