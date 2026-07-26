import requests
import json

url="https://transparencia.api.ro.gov.br/api/v1/remuneracao-servidor"

parametros = {
	"Page": "1",
	"PageSize": "20",
	"Mes": "6",
	"Ano":"2026",
	"Nome": "Alex",
	"SiglaUg": "DETRAN",
	"Cargo": ""
}

contador = 1
qtd_paginas = requests.get(url, params=parametros).json()["totalDePaginas"]
dados_extraidos = []

while contador <= qtd_paginas:
	parametros["Page"] = contador
	contador += contador
	dados = requests.get(url, params=parametros).json()
	dados_extraidos.extend(dados["resultados"])

with open("../data/raw/dados.json", "w", encoding="UTF-8") as arquivo_extraido:
	json.dump(dados_extraidos, arquivo_extraido, ensure_ascii=False, indent=4)
