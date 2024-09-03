import datetime
import time
import os
import pickle
import requests

def esperar(tempo: int):
    time.sleep(tempo)

# Verifica se já existem dados salvos
if os.path.exists('bib_artigos.pkl'):
    with open('bib_artigos.pkl', 'rb') as file:
        bibtex_list = pickle.load(file)
else:
    bibtex_list = []


inicio = datetime.datetime.now()

with open('arxiv/links_articles_DS.txt', 'r') as file_articles:
    links = file_articles.readlines()

qtd_rodada = 0
qtd_capturada = 0

for link in links:
    link = link.strip()

    if any(entry['link'] == link for entry in bibtex_list):
            qtd_capturada += 1
            print(f'{qtd_capturada}: {link} ja esta foi capturado')
            continue
    esperar(5)

    if(qtd_rodada == 5000):
        break
    try:
        url = link.replace('abs', 'bibtex')
        
        response = requests.get(url)
        if(response.status_code != 200):
            print("Bloqueado")
            break

        obj = {
            'bib': response.content.decode(),
            'link': link,
            'error': False
        }
        
        bibtex_list.append(obj)
        with open('bib_artigos.pkl', 'wb') as file:
            pickle.dump(bibtex_list, file)
            print(f'Completo {qtd_rodada} : - {link}')
        
        qtd_rodada += 1
    except:
        print(f'Erro no {link}')

end_time = time.time()
termino = datetime.datetime.now()

# Calcula a duração da execução
duracao = termino - inicio

print("BibTeX strings salvas em bib_artigos.pkl")
print(f"Tempo total de execução: {duracao} segundos")
print(f'Inicio: {inicio}')
print(f'Fim: {termino}')