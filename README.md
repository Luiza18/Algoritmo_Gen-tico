# Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)
Este projeto aplica um Algoritmo Genético (AG) para resolver uma versão simplificada do problema do Caixeiro Viajante (Traveling Salesman Problem - TSP). A interface gráfica é construída com PySimpleGUI para facilitar a interação do usuário com o algoritmo.

## Sobre Algoritmos Genéticos 🧬
Os algoritmos genéticos são métodos de otimização inspirados nos princípios da seleção natural e evolução das espécies. Eles operam com uma "população" de soluções candidatas, evoluindo essas soluções ao longo de várias "gerações". Em cada geração, as soluções são avaliadas por uma função de aptidão, e as melhores soluções são "reproduzidas" (cruzadas) para gerar novas soluções. Essas novas soluções sofrem pequenas mutações, introduzindo diversidade e permitindo que o algoritmo explore o espaço de soluções em busca de ótimos locais ou globais.

## Principais componentes de um AG:
* *População:* Um conjunto de soluções candidatas.
* *Seleção:* Escolha das soluções mais aptas para gerar novas soluções.
* *Cruzamento (Recombinação)*: Combinação de duas soluções (pais) para gerar novas soluções (filhos).
* *Mutação:* Pequenas alterações aleatórias nas soluções, mantendo a diversidade.
* *Avaliação:* Uma função que mede o quão boa é cada solução em resolver o problema.

## Sobre o Problema do Caixeiro Viajante (TSP) 🗺️
O TSP é um problema clássico de otimização combinatória, onde um vendedor deve visitar várias cidades, passando por cada uma apenas uma vez, e retornando à cidade de origem. O objetivo é encontrar a rota de menor distância que completa o percurso. Este problema é de complexidade NP-difícil, ou seja, não há solução exata eficiente para grandes conjuntos de cidades.

## Como o Algoritmo Genético resolve o TSP:
O algoritmo genético implementado neste projeto gera diversas rotas iniciais aleatórias para o caixeiro viajante e então evolui essas rotas ao longo das gerações, usando seleção, cruzamento e mutação para buscar uma rota de menor distância.

## Executando o Projeto ▶️

Para baixar e executar o projeto, siga as instruções abaixo:

1. Clone o repositório em sua máquina local:
2. Navegue até o diretório do projeto:
3. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv env 
````
4. Ative o ambiente virtual (caso tenha criado):

    -No Windows
   ```bash
        .\env\Scripts\activate
    ````
    -No Linux/Mac
    ```bash
        source env/bin/activate
    ````
5. Instale as dependências do projeto a partir do arquivo requirements.txt:
    ```bash
    pip install -r requirements.txt
     ````
