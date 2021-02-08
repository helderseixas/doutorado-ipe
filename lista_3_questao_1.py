import networkx as nx
import matplotlib.pyplot as plt
import random
from statistics import mean, variance

def simular(quantidade_simulacoes, m):
    grafo = nx.cycle_graph(m+1)
    quantidade_eventos_terminando_em_i = [0] * (m+1)
    lista_ultimo_vertice_evento = list()

    for i in list(range(quantidade_simulacoes)):
        vertice_particula = 0
        vertices_nao_visitados = set(grafo.nodes)
        vertices_nao_visitados.remove(0)

        passos = list()

        while(len(vertices_nao_visitados) > 0):
            vertice_particula = random.choice(list(grafo[vertice_particula].keys()))
            # print(str(vertice_particula), end="-")
            if (vertice_particula in vertices_nao_visitados):
                vertices_nao_visitados.remove(vertice_particula)
            passos.append(vertice_particula)
        quantidade_eventos_terminando_em_i[vertice_particula] += 1
        lista_ultimo_vertice_evento.append(vertice_particula)
        # print("\n")

        if i < 1:
            plt.xlabel("Passos")
            plt.ylabel("Vértices")
            plt.plot(passos)
            plt.show()

    print(f"Nº simulações: {quantidade_simulacoes}")
    print(f"m = {m}")
    print(f"Média: {mean(lista_ultimo_vertice_evento)}")
    print(f"Variância: {variance(lista_ultimo_vertice_evento)}")
    for i in range(m + 1):
        quantidade_eventos = quantidade_eventos_terminando_em_i[i]
        probabilidade = quantidade_eventos / quantidade_simulacoes
        print(f"Evento terminado em: {i} - Nº eventos: {quantidade_eventos} - P: {probabilidade}")

simular(100000, 10)