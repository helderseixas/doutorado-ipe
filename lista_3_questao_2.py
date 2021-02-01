import numpy as np
import matplotlib.pyplot as plt
from numpy.ma import average, var, cov

def imprimir_estatisticas(distribuicao, nome_distribuicao):
    print(f"Média - {nome_distribuicao}: {average(distribuicao)}")
    print(f"Variância - {nome_distribuicao}: {var(distribuicao)}")

def criar_distribuicao_y(distribuicao):
    return 7 * distribuicao - 0.5

def criar_distribuicao_y_estimador(distribuicao, distribuicao_y):
    # return average(distribuicao_y) + (cov(distribuicao, distribuicao_y) / var(distribuicao)) * (distribuicao - average(distribuicao))
    return cov(distribuicao, distribuicao_y)

def plotar_histograma(distribuicao, titulo):
    plt.hist(distribuicao, 10, density=True, color='w', edgecolor='b')
    plt.title(titulo)
    plt.show()


tamanho = 1000000

distribuicao_uniforme = np.random.uniform(low=-10, high=10, size=tamanho)
imprimir_estatisticas(distribuicao_uniforme, "distribuição uniforme")
distribuicao_uniforme_y = criar_distribuicao_y(distribuicao_uniforme)
imprimir_estatisticas(distribuicao_uniforme_y, "distribuição uniforme y")
distribuicao_uniforme_y_estimador = criar_distribuicao_y_estimador(distribuicao_uniforme, distribuicao_uniforme_y)
print((str(distribuicao_uniforme_y_estimador)))
imprimir_estatisticas(distribuicao_uniforme_y_estimador, "distribuicao_uniforme_y_estimador")
# plotar_histograma(distribuicao_uniforme, "Distribuição uniforme")

distribuicao_bernoulli = np.random.binomial(1,0.5, tamanho)
imprimir_estatisticas(distribuicao_bernoulli, "distribuição bernoulli")
distribuicao_bernoulli_y = criar_distribuicao_y(distribuicao_bernoulli)
imprimir_estatisticas(distribuicao_bernoulli_y, "distribuição bernoulli y")
# plotar_histograma(distribuicao_bernoulli, "Distribuição Bernoulli")

distribuicao_binomial = np.random.binomial(10,0.5,tamanho)
imprimir_estatisticas(distribuicao_binomial, "distribuição binomial")
distribuicao_binomial_y = criar_distribuicao_y(distribuicao_binomial)
imprimir_estatisticas(distribuicao_binomial_y, "distribuição binomial y")
#plotar_histograma(distribuicao_binomial, "Distribuição binomial")

distribuicao_geometrica = np.random.geometric(0.5, tamanho)
imprimir_estatisticas(distribuicao_geometrica, "distribuição geométrica")
distribuicao_geometrica_y = criar_distribuicao_y(distribuicao_geometrica)
imprimir_estatisticas(distribuicao_geometrica_y, "distribuição geometrica y")
# plotar_histograma(distribuicao_geometrica, "Distribuição geométrica")

distribuicao_poisson = np.random.poisson(lam=10, size = tamanho)
imprimir_estatisticas(distribuicao_poisson, "distribuição de Poisson")
distribuicao_poisson_y = criar_distribuicao_y(distribuicao_poisson)
imprimir_estatisticas(distribuicao_poisson_y, "distribuição de Poisson y")
# plotar_histograma(distribuicao_poisson, "Distribuição Poisson")