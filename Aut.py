import pandas as pd
import os
import requests
import json

ler = pd.read_excel("Livros.xls")
#crie uma variavel com a key da api#

for titulo, autor in zip(ler["Unnamed: 1"].iloc[3:100], ler["Unnamed: 2"].iloc[3:100]):
    params = {
        "q": f"sinopse do livro {titulo} de {autor}","api_key": #coloque a variavel aqui#
   }
    resposta = requests.get("https://serpapi.com/search", params=params)
    resposta.raise_for_status()
    dados = resposta.json()
    try:
        sinopse = dados['related_questions'][0].get('snippet')
        print(sinopse)
    except:
        print("Sinopse não encontrada")
print(json.dumps(sinopse, indent=2))