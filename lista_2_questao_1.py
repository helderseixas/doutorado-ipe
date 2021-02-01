import itertools
import random

ALFABETO = {"a","b","c","d","e","s"}
S = "s"

def extrair_palavras_iniciando_com_s(palavras_com_3_letras):
    indice_verificacao = 0
    return extrar_palavras_com_s(indice_verificacao, palavras_com_3_letras)


def extrair_palavras_com_s_no_meio(palavras_com_3_letras):
    indice_verificacao = 1
    return extrar_palavras_com_s(indice_verificacao, palavras_com_3_letras)

def extrar_palavras_com_s(indice_verificacao_da_letra_s, palavras_com_3_letras):
    conjunto = []
    for palavra in palavras_com_3_letras:
        if (palavra[indice_verificacao_da_letra_s] == S):
            conjunto.append(palavra)
    return conjunto


def extrair_palavras_com_exatamente_2_letras_iguais(palavras_com_3_letras):
    conjunto = []
    for palavra in palavras_com_3_letras:
        if palavra[0] == palavra[1] and palavra[0] != palavra[2]:
            conjunto.append(palavra)
        elif palavra[0] == palavra[2] and palavra[0] != palavra[1]:
            conjunto.append(palavra)
        elif palavra[1] == palavra[2] and palavra[1] != palavra[0]:
            conjunto.append(palavra)
    return conjunto


def simular(quantidade_sorteios):
    palavras_com_3_letras = gerar_palavras_com_3_letras()
    A = extrair_palavras_iniciando_com_s(palavras_com_3_letras)
    B = extrair_palavras_com_s_no_meio(palavras_com_3_letras)
    C = extrair_palavras_com_exatamente_2_letras_iguais(palavras_com_3_letras)

    quantidade_sorteada_a = 0
    quantidade_sorteada_b = 0
    quantidade_sorteada_c = 0
    quantidade_sorteada_a_interscessao_b = 0
    quantidade_sorteada_a_interscessao_c = 0
    quantidade_sorteada_b_interscessao_c = 0
    quantidade_sorteada_a_interscessao_b_interscessao_c = 0
    for i in range(quantidade_sorteios):
        palavra_sorteada = random.choice(palavras_com_3_letras)
        if palavra_sorteada in A:
            quantidade_sorteada_a += 1
            if palavra_sorteada in B:
                quantidade_sorteada_a_interscessao_b += 1
            if palavra_sorteada in C:
                quantidade_sorteada_a_interscessao_c += 1
        if palavra_sorteada in B:
            quantidade_sorteada_b += 1
            if palavra_sorteada in C:
                quantidade_sorteada_b_interscessao_c += 1
        if palavra_sorteada in C:
            quantidade_sorteada_c += 1
            if palavra_sorteada in A and palavra_sorteada in B:
                quantidade_sorteada_a_interscessao_b_interscessao_c += 1

    probabilidade_a = quantidade_sorteada_a / quantidade_sorteios
    probabilidade_b = quantidade_sorteada_b / quantidade_sorteios
    probabilidade_c = quantidade_sorteada_c / quantidade_sorteios
    probabilidade_a_interscessao_b = quantidade_sorteada_a_interscessao_b / quantidade_sorteios
    probabilidade_a_interscessao_c = quantidade_sorteada_a_interscessao_c / quantidade_sorteios
    probabilidade_b_interscessao_c = quantidade_sorteada_b_interscessao_c / quantidade_sorteios
    probabilidade_a_interscessao_b_interscessao_c = quantidade_sorteada_a_interscessao_b_interscessao_c / quantidade_sorteios

    print(f"Nº sorteios: {quantidade_sorteios}")
    imprimir("A", probabilidade_a, quantidade_sorteada_a)
    imprimir("B", probabilidade_b, quantidade_sorteada_b)
    imprimir("C", probabilidade_c, quantidade_sorteada_c)
    imprimir("A interscessão B", probabilidade_a_interscessao_b, quantidade_sorteada_a_interscessao_b)
    imprimir("A interscessão C", probabilidade_a_interscessao_c, quantidade_sorteada_a_interscessao_c)
    imprimir("B interscessão C", probabilidade_b_interscessao_c, quantidade_sorteada_b_interscessao_c)
    imprimir("A interscessão B interscessão C", probabilidade_a_interscessao_b_interscessao_c, quantidade_sorteada_a_interscessao_b_interscessao_c)

def imprimir(evento, probabilidade_a, quantidade_sorteada_a):
    print(f"Evento: {evento} - Nº eventos: {quantidade_sorteada_a} - P: {probabilidade_a}")


def gerar_palavras_com_3_letras():
    return list(itertools.product(ALFABETO, repeat=3))


simular(1000000)