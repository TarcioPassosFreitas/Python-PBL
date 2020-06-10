# -- coding: utf-8 --
import random

def bubbleSort(lista, posicao=0):
    for index in range(len(lista)):
        for count in range(len(lista)):
            if lista[index][posicao] < lista[count][posicao]:
                lista[index], lista[count] = lista[count], lista[index]


def ler_arquivos(nome_arquivo, codificacao):  # função para ler os arquivos
    file = open(nome_arquivo, "r", encoding=codificacao)
    linhas = file.readlines()
    ordem_nome = {}; contador = 0
    for nome in linhas[0].split(";"):
        ordem_nome[nome.replace("\n", "")] = contador; contador += 1
    armazenar_cartas = []
    for i in range(1, len(linhas)):
        armazenar_cartas.append(linhas[i].replace("\n", "").split(';'))
    return armazenar_cartas, ordem_nome


def distribuirCartas(matriz):
    decks = [list(), list()]
    decks[0] = matriz[:5]; decks[1] = matriz[5:10]; contador = 10
    while contador > 0: matriz.pop(); contador -= 1
    return decks

def jokempo(deck_1, deck_2, compara, posicao=0):
    ordem_vitoria = {"Tesoura":"Papel", "Pedra":"Tesoura", "Papel":"Pedra"}
    selecoes = [deck_1[posicao][compara], deck_2[posicao][compara]]
    if selecoes[0] == selecoes[1]:
        return 3 #empate
    elif ordem_vitoria[selecoes[0]] == selecoes[1]:
        return 0
    else:
        return 1


def quem_ganha(deck_1, deck_2, cava, compara, posicao = 0):
    vencedor = 0
    if deck_1[posicao][compara] > deck_2[posicao][compara]:
        deck_1.append(cava.pop()); vencedor = 0
    else:
        deck_2.append(cava.pop()); vencedor = 1
    deck_1.remove(deck_1[posicao]); deck_2.remove(deck_2[posicao])
    return vencedor

def partida():
    topo, ordem_nome = ler_arquivos("./cartas.txt", 'utf-8')

    print('Digite o nome do primeiro jogador')
    jogador1 = str(input())
    print('Digite o nome do segundo jogador')
    jogador2 = str(input())
    modo_jogo = 0
    while modo_jogo != 1 and modo_jogo != 2:
        print("qual o modo de jogo que vc deseja jogar:\n1 - Aleatório\n2 - Manual")
        modo_jogo = int(input())
    automatico = False
    if modo_jogo == 1:
        random.shuffle(topo)
        automatico = True
    decks = distribuirCartas(topo)
    modo_disputa = 0; cont = 0; posicao = 0
    vitorias = [0, 0]
    while len(decks[0]) > 0 and len(decks[1]) and cont < 10:
        print("Jogador %s ganhou %d disputas\nJogador %s ganhou %d disputas" % (jogador1, vitorias[0], jogador2, vitorias[1]))
        menor_quantidade = min(len(decks[0]), len(decks[1]))
        if modo_jogo == 1:
            posicao = 0
            if menor_quantidade > 1:
                posicao = random.randint(0, menor_quantidade - 1)
        else:
            posicao = int(input("Digite uma posicao da carta entre 0 e %d" % (menor_quantidade - 1)))

        print("Jogador %s Escolha o modo de disputa:\n1- Valor\n2- Força\n3- Energia\n4- Jokempô" % (cont % 2 == 0 and jogador1 or jogador2))
        print(len(decks[0]), len(decks[1]), posicao)
        modo_disputa = int(input())
        if modo_disputa == 1:
            if automatico:
                bubbleSort(decks[0], ordem_nome["Valor"]); bubbleSort(decks[1], ordem_nome["Valor"])
            else:
                bubbleSort(decks[0], ordem_nome["Personagem"]); bubbleSort(decks[1], ordem_nome["Personagem"])
            vitorias[quem_ganha(decks[0], decks[1], topo, ordem_nome["Valor"], posicao=posicao)] += 1
        elif modo_disputa == 3:
            if automatico:
                bubbleSort(decks[0], ordem_nome["Força"]); bubbleSort(decks[1], ordem_nome["Força"])
            else:
                bubbleSort(decks[0], ordem_nome["Personagem"]); bubbleSort(decks[1], ordem_nome["Personagem"])
            vitorias[quem_ganha(decks[0], decks[1], topo, ordem_nome["Força"], posicao=posicao)] += 1
        elif modo_disputa == 2:
            if automatico:
                bubbleSort(decks[0], ordem_nome["Energia"]); bubbleSort(decks[1], ordem_nome["Energia"])
            else:
                bubbleSort(decks[0], ordem_nome["Personagem"]); bubbleSort(decks[1], ordem_nome["Personagem"])
            vitorias[quem_ganha(decks[0], decks[1], topo, ordem_nome["Energia"], posicao=posicao)] += 1
        elif modo_disputa == 4:
            random.shuffle(decks[0]); random.shuffle([decks[1]])
            resultado = jokempo(decks[0], decks[1], ordem_nome["Jokempo"], posicao=posicao)
            decks[0].remove(decks[0][posicao]); decks[1].remove(decks[1][posicao])
            if resultado == 3:
                decks[0].append(topo.pop()); decks[1].append(topo.pop())
            else:
                decks[resultado].append(topo.pop())
                vitorias[resultado] += 1

        cont += 1

    if vitorias[0] > vitorias[1]:
        print("Jogador %s venceu" % jogador1)
    else:
        print("Jogador %s venceu" % jogador2)
    return {
        "Jogadores": [jogador1, jogador2],
        "Vencedor": vitorias[0] > vitorias[1] and jogador1 or jogador2,
    }

executa = True
jogadores = {}

def criarJogador(nome, jogadores):
    jogadores[nome] = {"partidas": 0, "vitorias": 0}

while executa:
    selecao = int(input("[1] Jogar\n[2] Ver Dados\n[3] Sair\n__.>"))
    if selecao == 1:
        resultado = partida()
        if resultado["Jogadores"][0] not in jogadores.keys():
            criarJogador(resultado["Jogadores"][0], jogadores)
        if resultado["Jogadores"][1] not in jogadores.keys():
            criarJogador(resultado["Jogadores"][1], jogadores)
        jogadores[resultado["Jogadores"][0]]["partidas"] += 1
        jogadores[resultado["Jogadores"][1]]["partidas"] += 1
        jogadores[resultado["Vencedor"]]["vitorias"] += 1
    elif selecao == 2:
        nome = input("Digite o nome do Jogador\n__.>")
        print(jogadores[nome], jogadores[nome]["vitorias"] * 100 / jogadores[nome]["partidas"])
    else:
        executa = False