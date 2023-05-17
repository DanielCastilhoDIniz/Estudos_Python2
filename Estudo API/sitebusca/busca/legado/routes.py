from flask import Flask, jsonify, request
from flask import render_template, redirect, url_for, flash, abort
import requests
import json

app = Flask(__name__)

with open('googleMapApiKey.json', 'r') as f:
    load_key = json.loads(f.read())

api_key = load_key['GOOGLE_MAPS_API_KEY']


@app.route('/api/places', methods=['GET'])
def get_nearbay_places():

    # Faz a consulta do CEP para obter o endereço completo
    # cep = request.args.get('cep')
    cep = 58051200
    
    if cep:
        cep_url = f"https://cep.awesomeapi.com.br/json/{cep}"
        cep_response = requests.get(cep_url)
        endereco_dic = cep_response.json()
        lat = endereco_dic['lat']
        lng = endereco_dic['lng'] 

        if endereco_dic.get('error'):
            return jsonify({'error': endereco_dic['error']}), 400
        else:
            # Se o CEP não foi fornecido, usa a latitude e a longitude diretamente
            location = f"{lat},{lng}"
# Faz a solicitação à API do Google Places para obter os locais próximos
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=1000&type=bar&language=pt-BR&key={api_key}"
    response = requests.get(url)
    dados = response.json()

    # Retorna os resultados em formato JSON
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)

