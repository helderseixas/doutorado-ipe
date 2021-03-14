from statistics import mean

import numpy as np
from numpy.ma import average, var, max

def main():
    simulacao(1000)
    simulacao(10000)
    simulacao(100000)
    simulacao(1000000)

def simulacao(tamanho_amostras):
    print(f"\n*Simulacão com {tamanho_amostras} amostras")
    epsilon = 0.00001
    teta = 10
    numero_amostras = 100
    valor_minimo = teta + epsilon
    valor_maximo = teta + 1 - epsilon
    estimadores_momentos = []
    erros_amostrais_estimadores_momentos = []
    estimadores_maxima_verossimilhanca = []
    erros_amostrais_estimadores_maxima_verossimilhanca = []

    for i in range(numero_amostras):
        distribuicao_uniforme = np.random.uniform(low=valor_minimo, high=valor_maximo, size=tamanho_amostras)

        estimador_momentos = average(distribuicao_uniforme) - 0.5
        estimadores_momentos.append(estimador_momentos)
        erro_amostral_estimador_momentos = estimador_momentos - teta
        erros_amostrais_estimadores_momentos.append(erro_amostral_estimador_momentos)

        estimador_maxima_verossimilhanca = min(distribuicao_uniforme) - epsilon
        estimadores_maxima_verossimilhanca.append(estimador_maxima_verossimilhanca)
        erro_amostral_estimador_maxima_verossimilhanca = estimador_maxima_verossimilhanca - teta
        erros_amostrais_estimadores_maxima_verossimilhanca.append(erro_amostral_estimador_maxima_verossimilhanca)

    imprimir_resultados("Momentos", erros_amostrais_estimadores_momentos, estimadores_momentos,
                        teta)
    imprimir_resultados("Máx. Veros.", erros_amostrais_estimadores_maxima_verossimilhanca,
                        estimadores_maxima_verossimilhanca, teta)


def imprimir_resultados(nome_estimador, erros_amostrais_estimadores, estimadores, teta):
    erro_quadratico_medio = average(erros_amostrais_estimadores) ** 2
    vies = average(estimadores) - teta
    variancia = var(estimadores)
    print(f"Estimador: {nome_estimador} \tEQM: {erro_quadratico_medio:.5f} \tViés: {vies:.5f} \tVariância: {variancia:.5f}")


if __name__ == '__main__':
    main()
