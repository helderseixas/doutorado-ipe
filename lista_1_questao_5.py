import random

JOGADORES = ["A", "B", "C"]
INDICE_JOGADOR_A = 0
INDICE_JOGADOR_B = 1


def obter_indice_proximo_adversario(jogadores_ultima_partida):
    for i in list(range(3)):
        if i not in jogadores_ultima_partida:
            return i


def simular_sequencia_vencedores_partida(indice_jogador_1, indice_jogador_2, vencendores_partidas):
    indice_vencedor_partida = random.choice([indice_jogador_1, indice_jogador_2])
    vencedor_partida = JOGADORES[indice_vencedor_partida]
    vencendores_partidas += vencedor_partida
    total_partidas = len(vencendores_partidas)

    if(total_partidas == 4):
        return vencendores_partidas
    elif(total_partidas >= 2):
        ultimo_vencedor = vencendores_partidas[total_partidas - 1]
        penultimo_vencedor = vencendores_partidas[total_partidas - 2]
        if ultimo_vencedor ==  penultimo_vencedor:
            return vencendores_partidas

    jogadores_ultima_partida = [indice_jogador_1, indice_jogador_2]
    indice_proximo_adversario = obter_indice_proximo_adversario(jogadores_ultima_partida)
    return simular_sequencia_vencedores_partida(indice_vencedor_partida, indice_proximo_adversario, vencendores_partidas)


def simular_sequencia_vencedores_partidas(quantidade):
    sequencia_simulacoes = []
    for i in list(range(quantidade)):
        vencendores_partidas = ""
        simulacao = simular_sequencia_vencedores_partida(INDICE_JOGADOR_A, INDICE_JOGADOR_B, vencendores_partidas)
        sequencia_simulacoes.append(simulacao)
    return sequencia_simulacoes


def imprimir_resultados(sequencia_simulacoes, sequencia_vencedores):
    quantidade_simulacoes = len(sequencia_simulacoes)
    quantidade_eventos_sucesso = sequencia_simulacoes.count(sequencia_vencedores)
    probabilidade = quantidade_eventos_sucesso / quantidade_simulacoes
    print(
        f"Nº sorteios: {quantidade_simulacoes} - Nº de eventos {sequencia_vencedores}: {quantidade_eventos_sucesso} - P({sequencia_vencedores}): {probabilidade}")


def imprimir_probabilidades_sequencia_vencedores_partidas(quantidade):
    sequencia_simulacoes = simular_sequencia_vencedores_partidas(quantidade)
    imprimir_resultados(sequencia_simulacoes, "ACBA")
    imprimir_resultados(sequencia_simulacoes, "ACBB")
    imprimir_resultados(sequencia_simulacoes, "ACC")
    imprimir_resultados(sequencia_simulacoes, "AA")
    imprimir_resultados(sequencia_simulacoes, "BCAA")
    imprimir_resultados(sequencia_simulacoes, "BCAB")
    imprimir_resultados(sequencia_simulacoes, "BCC")
    imprimir_resultados(sequencia_simulacoes, "BB")

imprimir_probabilidades_sequencia_vencedores_partidas(1000000)

