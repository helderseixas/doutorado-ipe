import random

CARA = "C"
COROA = "R"

def sortear(quantidade):
    sorteios = []
    for i in list(range(quantidade)):
        sorteios.append(random.choice([CARA, COROA]))
    return sorteios


def imprimir_sortear_3_caras_sequencia(quantidade):
    sorteios = sortear(quantidade)
    quantidade_3_caras_sequencia = 0
    for i in list(range(2, quantidade)):
        primeiro_item_sequencia = sorteios[i-2]
        segundo_item_sequencia = sorteios[i-1]
        terceiro_item_sequencia = sorteios[i]
        if(primeiro_item_sequencia == CARA and segundo_item_sequencia == CARA and terceiro_item_sequencia == CARA):
            quantidade_3_caras_sequencia += 1
    probabilidade = quantidade_3_caras_sequencia / (quantidade - 2)
    print(f"Nº sorteios: {quantidade} - Nº 3 caras em sequência: {quantidade_3_caras_sequencia} - P(3 caras em sequência): {probabilidade}")


imprimir_sortear_3_caras_sequencia(100000)
imprimir_sortear_3_caras_sequencia(1000000)
imprimir_sortear_3_caras_sequencia(10000000)
imprimir_sortear_3_caras_sequencia(100000000)
