from flask import Flask, jsonify, request
import requests
from datetime import date,datetime

app = Flask(__name__)


@app.route('/<username>')
def obterusuario(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    dados = response.json()
    ultimo_update=dados['updated_at']
    ultimo_update=ultimo_update[:10]
    data_atual = date.today()
    ultimo_update =datetime.strptime(ultimo_update, '%Y-%m-%d').date()
    dias_dif=(data_atual-ultimo_update)
    if (dias_dif.days>30):
        return jsonify(f'Atualize seu GitHub, já são {dias_dif.days} sem atualizar!')
    else:
        return jsonify(f'Seu Github está atualizado, são apenas {dias_dif.days} sem atualizar =D')
    
    

app.run(port=5000,host='localhost',debug=True)