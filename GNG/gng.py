#implementacao simples GNG

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# gerar dados

def make_circles(n_samples=2000, noise=0.05, seed=7):
    rng = np.random.default_rng(seed)
    n = n_samples // 2
    t = rng.uniform(0, 2*np.pi, n)
    outer = np.stack([np.cos(t), np.sin(t)], axis=1)
    inner = 0.5 * np.stack([np.cos(t), np.sin(t)], axis=1)
    X = np.vstack([outer, inner])
    X += rng.normal(0, noise, X.shape)
    return X

X = make_circles(n_samples=3000, noise=0.05)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=2)
plt.axis('equal')
plt.title("Dataset - Círculos Concêntricos")
plt.show()

# hiperparametros do GNG
max_nodes = 180
max_age = 70
lambda_steps = 120
eps_b = 0.06
eps_n = 0.008
alpha = 0.5
d = 0.996
seed = 11
np.random.seed(seed)

#inicializaçao do grafo

G = nx.Graph()

#começa com 2 nós escolhidos aleatoriamente
G.add_node(0, w=X[np.random.randint(0, len(X))], error=0.0)
G.add_node(1, w=X[np.random.randint(0, len(X))], error=0.0)
G.add_edge(0, 1, age=0)

# func principal de treino do GNG

for step in range(20000): #num max de iteraçoes
    x = X[np.random.randint(0, len(X))]  # amostra aleatoria

    #encontra os 2 neuronios mais proximos
    nodes = list(G.nodes())
    dists = [np.linalg.norm(x - G.nodes[n]['w']) for n in nodes]
    s1, s2 = np.argsort(dists)[:2]
    n1, n2 = nodes[s1], nodes[s2]

    #incrementa a idade das arestas conectadas a n1
    for neighbor in list(G.neighbors(n1)):
        G[n1][neighbor]['age'] += 1

    #atualiza o vencedor (n1) e seus vizinhos
    G.nodes[n1]['w'] += eps_b * (x - G.nodes[n1]['w'])
    for neighbor in list(G.neighbors(n1)):
        G.nodes[neighbor]['w'] += eps_n * (x - G.nodes[neighbor]['w'])

    #atualiza erro
    G.nodes[n1]['error'] += np.linalg.norm(x - G.nodes[n1]['w'])**2

    #conecta n1 e n2
    if G.has_edge(n1, n2):
        G[n1][n2]['age'] = 0
    else:
        G.add_edge(n1, n2, age=0)

    #remove arestas velhas
    old_edges = [(u, v) for u, v, a in G.edges(data='age') if a > max_age]
    G.remove_edges_from(old_edges)

    #remove nós isolados
    isolated = list(nx.isolates(G))
    G.remove_nodes_from(isolated)

    #a cada lambda passos, insere novo nó
    if step % lambda_steps == 0 and len(G.nodes) < max_nodes and step > 0:
        #nó com maior erro
        q = max(G.nodes, key=lambda n: G.nodes[n]['error'])
        #vizinho com maior erro
        f = max(G.neighbors(q), key=lambda n: G.nodes[n]['error'])

        # cria novo nó r
        w_r = 0.5 * (G.nodes[q]['w'] + G.nodes[f]['w'])
        r = max(G.nodes) + 1
        G.add_node(r, w=w_r, error=0.0)

        # substitui arestas antigas
        G.remove_edge(q, f)
        G.add_edge(q, r, age=0)
        G.add_edge(r, f, age=0)

        #reduz eros
        G.nodes[q]['error'] *= alpha
        G.nodes[f]['error'] *= alpha
        G.nodes[r]['error'] = G.nodes[q]['error']

    # Reduz erro globalmente
    for n in G.nodes():
        G.nodes[n]['error'] *= d

    # Critério de parada simples (opcional)
    if step % 5000 == 0:
        print(f"Iteração {step}, nós: {len(G.nodes)}")
        if len(G.nodes) >= max_nodes:
            break

#visualizaçaqo final
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], s=2, alpha=0.3, label='Dados')

#desenha as arestas
for (u, v) in G.edges():
    w_u = G.nodes[u]['w']
    w_v = G.nodes[v]['w']
    plt.plot([w_u[0], w_v[0]], [w_u[1], w_v[1]], 'k-', linewidth=0.5)

# desenha os nós
weights = np.array([G.nodes[n]['w'] for n in G.nodes()])
plt.scatter(weights[:, 0], weights[:, 1], c='red', s=10, label='Neurônios')

plt.axis('equal')
plt.title("Growing Neural Gas - Rede Final")
plt.legend()
plt.show()

