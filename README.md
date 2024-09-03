# Recuperação de Informação Utilizando BERT - Projeto de Testes em LLM

Este repositório contém o código e os materiais relacionados ao projeto de Recuperação de Informação (RI) utilizando o modelo BERT. O projeto foi desenvolvido para analisar como um modelo de Linguagem de Grande Escala (LLM) responde a perturbações nas referências de entrada e para avaliar a eficácia da recuperação de informações em um banco de dados bibliográfico. Este repositório inclui:

- **Código da IA**: Scripts que implementam o modelo de recuperação de informações utilizando BERT, incluindo a modificação e avaliação das consultas.
- **Criação do Banco de Dados**: Scripts necessários para a construção e armazenamento dos embeddings das referências bibliográficas.
- **Artigo Científico**: O artigo escrito no padrão IEEE, detalhando a metodologia, experimentos, e resultados do projeto.
- **Slides de Apresentação**: Slides criados para a apresentação do projeto, destacando os principais achados e conclusões.

## Descrição do Projeto

Este projeto visa explorar a robustez do modelo BERT em tarefas de Recuperação de Informação (RI), 
especificamente com referências bibliográficas, em um cenário onde as referências de entrada são modificadas por remoção ou substituição 
de palavras e caracteres. O objetivo principal é avaliar como essas perturbações afetam a capacidade do modelo 
de recuperar a referência correta e calcular o Mean Average Precision (MAP) em diferentes cenários de modificação.

### Estrutura do Repositório

- `src/`: Contém o código fonte da IA e modificações das consultas e avaliação dos resultados.
- `data/`: Scripts e arquivos para a construção do banco de dados de referências bibliográficas.
- `article/`: Versão final do artigo científico no padrão IEEE.
- `presentation/`: Slides de apresentação utilizados para expor os resultados do projeto.

### Links para artigo e apresentação
- `apresentação`: https://drive.google.com/file/d/1nPiwXFML6XCFdSm8bgjSBFPLtW9NegoP/view?usp=sharing
- `artigo`:  https://drive.google.com/file/d/1gICm85sKUNxu8dqtORUatMjuisJuw2rj/view?usp=sharing

### Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/SeuUsuario/SeuProjeto.git
   
### Tecnologias Utilizadas
