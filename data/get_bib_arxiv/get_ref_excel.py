import os
from pybtex.database import parse_string
from pybtex.style.formatting.plain import Style
import pandas as pd
import pickle

obj_padrao = {
    'referencia': None,
    'autor': None,
    'titulo': None,
    'ano': None,
}

# Verifica se o arquivo pickle existe
if os.path.exists('Projeto_Final_IA'):
    with open('Projeto_Final_IA/data/bib_artigos.pkl', 'rb') as file:
        bibtex_list = pickle.load(file)
else:
    raise FileNotFoundError("O arquivo bib_artigos.pkl não foi encontrado.")

lista_articles = []

for i, obj in enumerate(bibtex_list):
    try:
        bib_data = parse_string(obj['bib'], bib_format='bibtex')
        
        # Use o estilo padrão para formatar a entrada
        style = Style()

        # Gere a referência formatada
        formatted_entries = style.format_entries(bib_data.entries.values())
        item = obj_padrao.copy()

        # Converta a referência formatada para string
        for entry in formatted_entries:
            item['referencia'] = entry.text.render_as('text')

        # Pegar autor, titulo, ano
        for key, entry in bib_data.entries.items():
            item['autor'] = " and ".join(str(person) for person in entry.persons['author'])
            item['titulo'] = entry.fields['title']
            item['ano'] = entry.fields['year']

        lista_articles.append(item)
    except Exception as e:
        print(f"{i}: Erro ao fazer o parsing de BibTeX: {e}")
        continue

# Criar a planilha Excel
df = pd.DataFrame(lista_articles)
excel_path = "dados_artigos.xlsx"
df.to_excel(excel_path, index=False)

print(f"Dados salvos em {excel_path}")
print(len(df))