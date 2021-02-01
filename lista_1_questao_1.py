import random

PESSOA_EM_CASA = "C"
PESSOA_FORA_CASA = "F"

def sortear(quantidade):
    sorteios = []
    for i in list(range(quantidade)):
        sorteio = []
        for j in list(range(4)):
            item_sorteio = random.choices([PESSOA_EM_CASA, PESSOA_FORA_CASA], [0.4, 0.6])[0]
            sorteio.append(item_sorteio)
        sorteios.append(sorteio)
    return sorteios


def imprimir_probabilidade_minimo_2_pessoas_fora_casa(quantidade):
    sorteios = sortear(quantidade)
    quantidade_minimo_2_pessoas_fora_casa = 0
    for i in list(range(quantidade)):
        sorteio = sorteios[i]
        if(sorteio.count(PESSOA_FORA_CASA) >= 2):
            quantidade_minimo_2_pessoas_fora_casa += 1
    probabilidade = quantidade_minimo_2_pessoas_fora_casa / quantidade
    print(f"Nº sorteios: {quantidade} - Nº eventos sucesso: {quantidade_minimo_2_pessoas_fora_casa} - P(eventos sucesso): {probabilidade}")

imprimir_probabilidade_minimo_2_pessoas_fora_casa(1000000)

