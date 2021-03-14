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
    numero_amostras = 100
    valor_minimo = 0
    valor_maximo = 10
    estimadores_momentos_valor_maximo = []
    erros_amostrais_estimadores_momentos = []
    estimadores_maxima_verossimilhanca_valor_maximo = []
    erros_amostrais_estimadores_maxima_verossimilhanca = []

    for i in range(numero_amostras):
        distribuicao_uniforme = np.random.uniform(low=valor_minimo, high=valor_maximo, size=tamanho_amostras)

        estimador_momentos = 2 * average(distribuicao_uniforme)
        estimadores_momentos_valor_maximo.append(estimador_momentos)
        erro_amostral_estimador_momentos = estimador_momentos - valor_maximo
        erros_amostrais_estimadores_momentos.append(erro_amostral_estimador_momentos)

        estimador_maxima_verossimilhanca = max(distribuicao_uniforme)
        estimadores_maxima_verossimilhanca_valor_maximo.append(estimador_maxima_verossimilhanca)
        erro_amostral_estimador_maxima_verossimilhanca = estimador_maxima_verossimilhanca - valor_maximo
        erros_amostrais_estimadores_maxima_verossimilhanca.append(erro_amostral_estimador_maxima_verossimilhanca)

    imprimir_resultados("Momentos", erros_amostrais_estimadores_momentos, estimadores_momentos_valor_maximo,
                        valor_maximo)
    imprimir_resultados("Máx. Veros.", erros_amostrais_estimadores_maxima_verossimilhanca,
                        estimadores_maxima_verossimilhanca_valor_maximo, valor_maximo)


def imprimir_resultados(nome_estimador, erros_amostrais_estimadores, estimadores_valor_maximo,
                        valor_maximo):
    erro_quadratico_medio = average(erros_amostrais_estimadores) ** 2
    vies = average(estimadores_valor_maximo) - valor_maximo
    variancia = var(estimadores_valor_maximo)
    print(f"Estimador: {nome_estimador} \tEQM: {erro_quadratico_medio:.5f} \tViés: {vies:.5f} \tVariância: {variancia:.5f}")


if __name__ == '__main__':
    main()
