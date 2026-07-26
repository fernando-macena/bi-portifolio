import requests
import json

url="https://transparencia.api.ro.gov.br/api/v1/remuneracao-servidor"

parametros = {
	"Page": "1",
	"PageSize": "100",
	"Mes": "6",
	"Ano":"2026",
	"Nome": "",
	"SiglaUg": "DETRAN",
	"Cargo": ""
}

def obter_pagina(url, parametros):
	"""Obtem uma pagina json atraves de uma url e parametros"""
	print("Entrou na obter_pagina")
	return requests.get(url, params=parametros).json()

def extrair_dados(pagina):
	"""Extrai dados de uma pagina json e retorna uma colecao"""
	contador = 1
	qtd_paginas = pagina["totalDePaginas"]
	dados_extraidos = []

	print(qtd_paginas)

	while contador <= qtd_paginas:
		parametros["Page"] = contador
		contador += 1
		dados = obter_pagina(url, parametros)
		dados_extraidos.extend(dados["resultados"])
		print(contador)
	return dados_extraidos

def salvar_arquivo(dados_extraidos):
	with open("../data/raw/dados.json", "w", encoding="UTF-8") as arquivo_extraido:
		json.dump(dados_extraidos, arquivo_extraido, ensure_ascii=False, indent=4)

def main():
	pagina = obter_pagina(url, parametros)
	dados_extraidos = extrair_dados(pagina)
	salvar_arquivo(dados_extraidos)

main()
