readme: |
  # Problema do Caixeiro Viajante (TSP) com Algoritmo Genético

  Este projeto implementa uma solução para o **Problema do Caixeiro Viajante (TSP)** utilizando um **Algoritmo Genético (AG)**.
  Ele foi desenvolvido para fins acadêmicos, na disciplina de **Sistemas Inteligentes**, com o objetivo de explorar técnicas evolutivas aplicadas a problemas NP-difíceis.

  ---

  ## Objetivo
  Encontrar a menor rota que visita todas as cidades exatamente uma vez e retorna ao ponto inicial, minimizando a distância total percorrida.

  ---

  ## Técnicas Utilizadas
  
  ### Algoritmo Genético
  - **Representação:** permutação das cidades  
  - **Avaliação:** custo total da rota (distância euclidiana)  
  - **Seleção:** Torneio  
  - **Cruzamento (Crossover):** *OX – Order Crossover*  
  - **Mutação:** Swap com taxa de 3%  
  - **Elitismo:** preserva os melhores indivíduos  
  - **Critério de parada:** estagnação após 50 gerações  

  ### Bibliotecas Utilizadas
  - `random`
  - `math`
  - `matplotlib`
  - `networkx`

  ---

  ## 📂 Estrutura do Projeto

Caixeiro_Viajante/
├── tsp_ag.py # Código principal
├── melhor_rota.png # Imagem da melhor rota encontrada
├── evolucao_aptidao.png # Gráfico da evolução do custo
└── README.md # Este arquivo


---

## Como Executar

1. Instale as dependências:
   ```bash
   pip install matplotlib networkx
   ```
2. Execute o arquivo principal:
   ```bash
   python tsp_ag.py
   ```

---

## Resultados Gerados

O programa produz automaticamente:

- **Melhor rota encontrada**
- **Menor distância total**
- **Gráfico da evolução da aptidão**
- **Imagem com a rota final**

---

## Exemplos de Saída

- `melhor_rota.png` — Mapa com a rota ótima
- `evolucao_aptidao.png` — Gráfico da melhora por geração

---

## Observações

- O valor de `random.seed(32)` garante resultados reprodutíveis.  
- Para aumentar a dificuldade, basta mudar o número de cidades (`Ncidades`).  
- O código é fácil de adaptar para outros métodos de seleção, mutação ou crossover.

---

## Autor
Projeto desenvolvido como parte dos estudos em **Sistemas Inteligentes**, com foco em heurísticas evolutivas aplicadas a problemas de otimização.
