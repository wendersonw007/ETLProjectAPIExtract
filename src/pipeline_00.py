import requests
from tinydb import TinyDB
from datetime import datetime
#EXTRAINDO DADOS DO BITCOIN
def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados

print(extract_dados_bitcoin())
print('--------------------------------')
print(extract_dados_bitcoin()['data'])
print('--------------------------------')
print(extract_dados_bitcoin()['data']['amount'])


#TRANSFORMANDO DADOS DO BITCOIN
def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now().timestamp()

    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda,
        'timestamp': timestamp
    }

    return dados_transformados

def salvar_dados_tinydb(dados, db_row='dados_bitcoin.json'):
    db = TinyDB(db_row)
    db.insert(dados)
    print('Dados salvos com sucesso!')

if __name__ == "__main__":
    dados = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados)
    salvar_dados_tinydb(dados_transformados)

