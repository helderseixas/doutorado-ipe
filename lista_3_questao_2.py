import numpy as np
import matplotlib.pyplot as plt
from numpy.ma import average, var, cov


def imprimir_estatisticas(distribuicao, nome_distribuicao):
    print(f"Média - {nome_distribuicao}: {average(distribuicao)}")
    print(f"Variância - {nome_distribuicao}: {var(distribuicao)}")


def criar_distribuicao_y(distribuicao):
    return 7 * distribuicao - 0.5


def plotar_histograma(distribuicao, titulo):
    plt.hist(distribuicao, 10, density=True, color='w', edgecolor='b')
    plt.title(titulo)
    plt.show()


def criar_estimadores(variavel_x, variavel_y, n):
    medias_estimadores = []
    media_y = np.average(variavel_y)
    variancia_x = np.var(variavel_x)
    media_x = np.var(variavel_x)
    covariancia = np.cov(variavel_x, variavel_y)[0][1]
    for i in range(100):
        amostra_base = np.random.choice(variavel_x, n)
        estimativas = []
        for x in amostra_base:
            estimativa = media_y + (covariancia / variancia_x) * (x - media_x)
            estimativas.append(estimativa)
        media = np.average(estimativas)
        medias_estimadores.append(media)
    return medias_estimadores


def imprimir_erro_predicao(distribuicao, estimativas, nome_estimador):
    media_distribuicao = np.average(distribuicao)
    media_estimativas = np.average(estimativas)
    erro = media_distribuicao - media_estimativas
    print(f"Erro - {nome_estimador}: {erro}")


def main():
    tamanho = 1000000
    M = 10
    p = 0.5
    lambda_poison = 10

    print(f"Considerando:\nTamanho das variáveis aleatórias: {tamanho}\t M: {M}\t p (probabilidade): {p}\t lambda: {lambda_poison}\n")

    distribuicao_uniforme = np.random.uniform(low=-1 * M, high=M, size=tamanho)
    imprimir_estatisticas(distribuicao_uniforme, "distribuição uniforme")
    distribuicao_uniforme_y = criar_distribuicao_y(distribuicao_uniforme)
    imprimir_estatisticas(distribuicao_uniforme_y, "distribuição uniforme y")
    estimadores_uniforme_y_1k = criar_estimadores(distribuicao_uniforme, distribuicao_uniforme_y, 1000)
    imprimir_estatisticas(estimadores_uniforme_y_1k, "estimadores_uniforme_y com n = mil")
    estimadores_uniforme_y_10k = criar_estimadores(distribuicao_uniforme, distribuicao_uniforme_y, 10000)
    imprimir_estatisticas(estimadores_uniforme_y_10k, "estimadores_uniforme_y com n = 10 mil")
    estimadores_uniforme_y_100k = criar_estimadores(distribuicao_uniforme, distribuicao_uniforme_y, 100000)
    imprimir_estatisticas(estimadores_uniforme_y_100k, "estimadores_uniforme_y com n = 100 mil")
    imprimir_erro_predicao(distribuicao_uniforme_y, estimadores_uniforme_y_100k, "estimadores_uniforme_y com n = 100 mil")
    # plotar_histograma(distribuicao_uniforme_y, "Y Distribuição uniforme")

    distribuicao_bernoulli = np.random.binomial(1, p, tamanho)
    imprimir_estatisticas(distribuicao_bernoulli, "distribuição bernoulli")
    distribuicao_bernoulli_y = criar_distribuicao_y(distribuicao_bernoulli)
    imprimir_estatisticas(distribuicao_bernoulli_y, "distribuição bernoulli y")
    estimadores_bernoulli_y_1k = criar_estimadores(distribuicao_bernoulli, distribuicao_bernoulli_y, 1000)
    imprimir_estatisticas(estimadores_bernoulli_y_1k, "estimadores_bernoulli_y com n = mil")
    estimadores_bernoulli_y_10k = criar_estimadores(distribuicao_bernoulli, distribuicao_bernoulli_y, 10000)
    imprimir_estatisticas(estimadores_bernoulli_y_10k, "estimadores_bernoulli_y com n = 10 mil")
    estimadores_bernoulli_y_100k = criar_estimadores(distribuicao_bernoulli, distribuicao_bernoulli_y, 100000)
    imprimir_estatisticas(estimadores_bernoulli_y_100k, "estimadores_bernoulli_y com n = 100 mil")
    imprimir_erro_predicao(distribuicao_bernoulli_y, estimadores_bernoulli_y_100k, "estimadores_bernoulli_y com n = 100 mil")
    # plotar_histograma(distribuicao_bernoulli_y, "Y Distribuição Bernoulli")

    distribuicao_binomial = np.random.binomial(M, p, tamanho)
    imprimir_estatisticas(distribuicao_binomial, "distribuição binomial")
    distribuicao_binomial_y = criar_distribuicao_y(distribuicao_binomial)
    imprimir_estatisticas(distribuicao_binomial_y, "distribuição binomial y")
    estimadores_binomial_y_1k = criar_estimadores(distribuicao_binomial, distribuicao_binomial_y, 1000)
    imprimir_estatisticas(estimadores_binomial_y_1k, "estimadores_binomial_y com n = mil")
    estimadores_binomial_y_10k = criar_estimadores(distribuicao_binomial, distribuicao_binomial_y, 10000)
    imprimir_estatisticas(estimadores_binomial_y_10k, "estimadores_binomial_y com n = 10 mil")
    estimadores_binomial_y_100k = criar_estimadores(distribuicao_binomial, distribuicao_binomial_y, 100000)
    imprimir_estatisticas(estimadores_binomial_y_100k, "estimadores_binomial_y com n = 100 mil")
    imprimir_erro_predicao(distribuicao_binomial_y, estimadores_binomial_y_100k, "estimadores_binomial_y com n = 100 mil")
    # plotar_histograma(distribuicao_binomial_y, "Y Distribuição binomial")

    distribuicao_geometrica = np.random.geometric(p, tamanho)
    imprimir_estatisticas(distribuicao_geometrica, "distribuição geométrica")
    distribuicao_geometrica_y = criar_distribuicao_y(distribuicao_geometrica)
    imprimir_estatisticas(distribuicao_geometrica_y, "distribuição geometrica y")
    estimadores_geometrica_y_1k = criar_estimadores(distribuicao_geometrica, distribuicao_geometrica_y, 1000)
    imprimir_estatisticas(estimadores_geometrica_y_1k, "estimadores_geometrica_y com n = mill")
    estimadores_geometrica_y_10k = criar_estimadores(distribuicao_geometrica, distribuicao_geometrica_y, 10000)
    imprimir_estatisticas(estimadores_geometrica_y_10k, "estimadores_geometrica_y com n = 10 mill")
    estimadores_geometrica_y_100k = criar_estimadores(distribuicao_geometrica, distribuicao_geometrica_y, 100000)
    imprimir_estatisticas(estimadores_geometrica_y_100k, "estimadores_geometrica_y com n = 100 mill")
    imprimir_erro_predicao(distribuicao_geometrica_y, estimadores_geometrica_y_100k, "estimadores_geometrica_y com n = 100 mill")
    # plotar_histograma(distribuicao_geometrica_y, "Y Distribuição geométrica")

    distribuicao_poisson = np.random.poisson(lam=lambda_poison, size=tamanho)
    imprimir_estatisticas(distribuicao_poisson, "distribuição de Poisson")
    distribuicao_poisson_y = criar_distribuicao_y(distribuicao_poisson)
    imprimir_estatisticas(distribuicao_poisson_y, "distribuição de Poisson y")
    estimadores_poisson_y_1k = criar_estimadores(distribuicao_poisson, distribuicao_poisson_y, 1000)
    imprimir_estatisticas(estimadores_poisson_y_1k, "estimadores_poisson_y com mil")
    estimadores_poisson_y_10k = criar_estimadores(distribuicao_poisson, distribuicao_poisson_y, 10000)
    imprimir_estatisticas(estimadores_poisson_y_10k, "estimadores_poisson_y com 10 mil")
    estimadores_poisson_y_100k = criar_estimadores(distribuicao_poisson, distribuicao_poisson_y, 100000)
    imprimir_estatisticas(estimadores_poisson_y_100k, "estimadores_poisson_y com 100 mil")
    imprimir_erro_predicao(distribuicao_poisson_y, estimadores_poisson_y_100k, "estimadores_poisson_y com 100 mil")
    # plotar_histograma(distribuicao_poisson_y, "Y Distribuição Poisson")


if __name__ == '__main__':
    main()
