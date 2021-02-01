import itertools
import random

def gerar_conjunto(a, b):
    conjunto = []
    for x in list(range(a+1)):
        for y in list(range(b+1)):
            ponto = (x, y)
            conjunto.append(ponto)
    return conjunto

def imprimir(evento, quantidade_sorteada, probabilidade):
    print(f"Evento: {evento} - Nº eventos: {quantidade_sorteada} - P: {probabilidade}")

def simular(quantidade_sorteios, a, b):
    conjunto = gerar_conjunto(a, b)
    evento_a = 0
    evento_b = 0
    evento_c = 0
    evento_d = 0
    for i in range(quantidade_sorteios):
        ponto_sorteado = random.choice(conjunto)
        x = ponto_sorteado[0]
        y = ponto_sorteado[1]
        if x < y:
            evento_a += 1
        if b*x + a*y <= a*b/2:
            evento_b += 1
        if b*x + a*y >= a*b/3:
            evento_c += 1
        if x+y < 1/3:
            evento_d += 1
    probabilidade_evento_a = evento_a / quantidade_sorteios
    probabilidade_evento_b = evento_b / quantidade_sorteios
    probabilidade_evento_c = evento_c / quantidade_sorteios
    probabilidade_evento_d = evento_d / quantidade_sorteios

    print(f"Nº sorteios: {quantidade_sorteios}")
    imprimir("Evento A", evento_a, probabilidade_evento_a)
    imprimir("Evento B", evento_b, probabilidade_evento_b)
    imprimir("Evento C", evento_c, probabilidade_evento_c)
    imprimir("Evento D", evento_d, probabilidade_evento_d)


simular(1000000, 10000, 100)