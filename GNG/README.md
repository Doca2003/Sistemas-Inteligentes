title: "Growing Neural Gas (GNG) - Implementação Simples"
description: >
  Este projeto contém uma implementação simples do algoritmo
  Growing Neural Gas (GNG) aplicado a um dataset de círculos concêntricos.
  O objetivo é demonstrar o funcionamento do algoritmo, sua capacidade de
  adaptação incremental e a formação de estruturas topológicas.

sections:

  - header: "Sobre o Projeto"
    content: >
      O Growing Neural Gas (GNG) é um algoritmo de redes neurais que
      aprende incrementalmente a topologia de um conjunto de dados.
      Ele adiciona e remove nós e arestas dinamicamente, buscando
      representar a estrutura do espaço de entrada.

  - header: "Funcionalidades"
    list:
      - Geração de dataset com círculos concêntricos.
      - Construção e atualização incremental da rede GNG.
      - Inserção e remoção dinâmica de nós e arestas.
      - Parâmetros clássicos do algoritmo configurados.
      - Visualização gráfica do dataset e do grafo final.

  - header: "Estrutura do Projeto"
    content: |
      ```
      GNG/
      ├── gng_simples.py        # Código principal
      ├── resultado_gng.png     # Imagem da rede final (se incluir)
      └── README.md             # Este arquivo
      ```

  - header: "Como Executar"
    steps:
      - "Certifique-se de possuir **Python 3.8+** instalado."
      - "Instale as dependências necessárias:"
      - |
        ```bash
        pip install numpy networkx matplotlib
        ```
      - "Execute o script:"
      - |
        ```bash
        python gng_simples.py
        ```

  - header: "Hiperparâmetros Utilizados"
    table:
      max_nodes: 180
      max_age: 70
      lambda_steps: 120
      eps_b: 0.06
      eps_n: 0.008
      alpha: 0.5
      d: 0.996

  - header: "Descrição do Código"
    content: >
      O script inicia gerando um dataset artificial com dois círculos concêntricos.
      Em seguida, inicializa um grafo com dois neurônios aleatórios.  
      A cada iteração:
        - Um ponto aleatório do dataset é amostrado.
        - Os dois neurônios mais próximos são encontrados.
        - O vencedor e seus vizinhos são movidos em direção ao ponto.
        - Arestas antigas são removidas.
        - Nós isolados são excluídos.
        - A cada *λ* passos, um novo neurônio é inserido na região de maior erro.
      Ao final, uma figura mostra a estrutura da rede aprendida.

  - header: "Saída Esperada"
    content: >
      O script exibe:
        - O dataset original (pontos azuis).
        - A rede GNG final com suas arestas (linhas pretas).
        - Os neurônios aprendidos (pontos vermelhos).

  - header: "Referências"
    list:
      - "Fritzke, B. (1995). A Growing Neural Gas Network Learns Topologies."
      - "https://github.com/berndfritzke"

