import random
import matplotlib.pyplot as plt
import networkx as nx
import math

random.seed(32)
Ncidades = 8

cidades = {i:(random.uniform(0,100), random.uniform(0,100)) for i in range(Ncidades)}

G = nx.Graph()
for node, pos in cidades.items():
    G.add_node(node, pos=pos)

def distancia(c1, c2):  #TSP usa dist euclidiana
    x1, y1 = cidades[c1]
    x2, y2 = cidades[c2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def custo_total(percurso):  #custo total de um percurso
    total = 0
    for i in range(len(percurso)):
        c_atual = percurso[i]
        c_prox = percurso[(i + 1) % len(percurso)]  #retorno a origem
        total += distancia(c_atual, c_prox)
    return total

def criar_pop(tamanho_pop):  #cada individuo é uma permutacao das cidades
    pop = []
    for _ in range(tamanho_pop):
        individuo = list(cidades.keys())
        random.shuffle(individuo)
        pop.append(individuo)
    return pop

def aptidao(individuo):
    return 1 / custo_total(individuo)

def sel_torneio(pop, k=3):
    participantes = random.sample(pop, k)
    participantes.sort(key=lambda ind: custo_total(ind))
    return participantes[0]

def crossover_ox(pai1, pai2):  #ox foi escolhido
    a, b = sorted(random.sample(range(len(pai1)), 2))
    filho = [None] * len(pai1)

    #copia segmento do pai1
    filho[a:b] = pai1[a:b]

    #preenche resto com pai2
    pos = b
    for cidade in pai2:
        if cidade not in filho:
            if pos == len(filho):
                pos = 0
            filho[pos] = cidade
            pos += 1
    return filho

def mut_swap(individuo, taxa=0.03):
    if random.random() < taxa: 
        a, b = random.sample(range(len(individuo)), 2)
        individuo[a], individuo[b] = individuo[b], individuo[a]
    return individuo

def alg_genetico(pop_size=80, geracoes=200, num_elite=2):
    pop = criar_pop(pop_size)
    melhor_por_geracao = []

    melhor_anterior = float('inf')
    sem_melhora = 0
    limite_sem_melhora = 50


    for g in range(geracoes):
        elite = sorted(pop, key=custo_total)[:num_elite]
        nova_pop = []

        for _ in range(pop_size - num_elite):
            pai1 = sel_torneio(pop)
            pai2 = sel_torneio(pop)

            filho = crossover_ox(pai1, pai2)
            filho = mut_swap(filho)

            nova_pop.append(filho)

        nova_pop.extend(elite)#add elites

        pop = nova_pop

        # registra melhor da geração
        melhor = min(pop, key=custo_total)
        melhor_custo = custo_total(melhor)
        melhor_por_geracao.append(custo_total(melhor))

        print(f"Geração {g}: melhor custo = {melhor_custo:.2f}")

        if melhor_custo < melhor_anterior:
            melhor_anterior = melhor_custo
            sem_melhora = 0
        else:
            sem_melhora += 1
        
        if sem_melhora >= limite_sem_melhora:
            print("parada or estagnacao")
            break


    melhor_final = min(pop, key=custo_total)
    return melhor_final, melhor_por_geracao



melhor_rota, historico = alg_genetico()

#melhor distancia obtida
melhor_dist = custo_total(melhor_rota)
print(f"a) Melhor distancia obtida: {melhor_dist:.2f}")

#rota correspondente
print("b) Rota correspondente:", melhor_rota)

plt.figure(figsize=(6,6))
G2 = nx.Graph()

#adicionar nós
for node, pos in cidades.items():
    G2.add_node(node, pos=pos)

#adicionar arestas da melhor rota
for i in range(len(melhor_rota)):
    c1 = melhor_rota[i]
    c2 = melhor_rota[(i+1) % len(melhor_rota)]
    G2.add_edge(c1, c2)

pos = nx.get_node_attributes(G2, 'pos')
nx.draw(G2, pos, with_labels=True, node_size=600)
plt.title("c) Melhor Rota Encontrada")
plt.savefig("melhor_rota.png", dpi=300)
plt.show()

plt.figure(figsize=(8,4))
plt.plot(historico, linewidth=2)
plt.title("d)evolução da Aptidao -vMenor custo por geracao")
plt.xlabel("geracao")
plt.ylabel("custo")
plt.grid(True)
plt.savefig("evolucao_aptidao.png", dpi=300)
plt.show()
