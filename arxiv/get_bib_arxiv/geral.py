import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pybtex.database import parse_string
from pybtex.style.formatting.plain import Style
import pandas as pd

def esperar(tempo:int):
    time.sleep(tempo)

obj = {
    'referencia': None,
    'autor': None,
    'titulo': None,
    'ano': None,
    'link': None
}

# link = 'https://arxiv.org/abs/alg-geom/9202001'

lista_articles = []

with open('arxiv/links_articles.txt', 'r') as file_articles:
    for link in file_articles.readlines():
        driver = webdriver.Chrome()

        driver.get(link)

        esperar(5)

        driver.find_element(By.ID, 'bib-cite-trigger').click()

        esperar(10)

        bibtex_str = driver.find_element(By.ID, 'bib-cite-target').get_attribute('value')

        with open('bib_artigos.pkl', 'a') as file:
            file.write(bibtex_str + '\n')
            
        bib_data = parse_string(bibtex_str, bib_format='bibtex')

        # Use o estilo padrão para formatar a entrada
        style = Style()

        # Gere a referência formatada
        formatted_entries = style.format_entries(bib_data.entries.values())
        item = obj.copy()
        item['link'] = link
        # Converta a referência formatada para string
        for entry in formatted_entries:
            item['referencia'] = (entry.text.render_as('text'))

        # Pegar autor, titulo, ano
        for key, entry in bib_data.entries.items():
            item['autor'] = " and ".join(str(person) for person in entry.persons['author'])
            item['titulo'] = entry.fields['title']
            item['ano'] = entry.fields['year']

        lista_articles.append(item)
        driver.quit()

df = pd.DataFrame(lista_articles)
excel_path = "dados_artigos.xlsx"
df.to_excel(excel_path, index=False)