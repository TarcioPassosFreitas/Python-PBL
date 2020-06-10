'''/*******************************************************************************
Autor: Tarcio Passos Freitas
Componente Curricular: Algoritmos I
Concluido em: 15/08/2019
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''
# -*- coding: utf-8 -*-
def ler_arquivos(nome_arquivo, codificacao): #função para ler os arquivos
    file = open(nome_arquivo, "r", encoding=codificacao) #abertura dos arquivos
    lines = file.readlines() #leitura de linha por linha
    firstLine = lines[0]
    arquivo_retornado = {}
    nameOrder = []
    for name in firstLine.split(";"): #vamos percorrer o arquivo vendo o ;
        arquivo_retornado[name] = list() #o arquivo separado por ; vai ser colocado em uma lista
        nameOrder.append(name) #colocando o retorno do arquivo dentro de uma lista
    for index in range(1, len(lines)):
        elements = lines[index].split(";")
        for count in range(0, len(nameOrder)):
            arquivo_retornado[nameOrder[count]].append(elements[count])
    return arquivo_retornado


regioes = ler_arquivos("./regioes.txt", 'utf-8')
print(regioes)
tecnicosIBGE = ler_arquivos("./tecnicosIBGE.txt", None)
print(tecnicosIBGE)
exemploPesquisa = ler_arquivos("./exemploPesquisa.txt", 'utf-8')
print(exemploPesquisa)
for pesquisa in exemploPesquisa["Técnico"]:
    if pesquisa not in tecnicosIBGE["Matrícula"]:
        indice = exemploPesquisa["Técnico"].index(pesquisa)
        exemploPesquisa["Técnico"].remove(pesquisa)
        exemploPesquisa["1.01"].remove(pesquisa)
        exemploPesquisa["1.02"].remove(indice)
        exemploPesquisa["1.03"].remove(indice)
        exemploPesquisa["2.01"].remove(indice)
        exemploPesquisa["2.02"].remove(indice)
        exemploPesquisa["2.03"].remove(indice)
        exemploPesquisa["2.04"].remove(indice)
        exemploPesquisa["2.05"].remove(indice)
        exemploPesquisa["2.06"].remove(indice)
        exemploPesquisa["2.07"].remove(indice)
        exemploPesquisa["2.08"].remove(indice)
        exemploPesquisa["3.01"].remove(indice)
        exemploPesquisa["3.02"].remove(indice)
        exemploPesquisa["4.01"].remove(indice)
        exemploPesquisa["4.021"].remove(indice)
        exemploPesquisa["4.022"].remove(indice)
        exemploPesquisa["4.03"].remove(indice)
        exemploPesquisa["4.04"].remove(indice)
        exemploPesquisa["4.05"].remove(indice)

print("Números de domicílios utilizados para a coleta:\n")
print(len(exemploPesquisa['CEP']))
print("Números de domicílios particulares que já estão pagos, quantos ainda estão pagando e alugados, respectivamente:")
len(exemploPesquisa['2.01'])
domic_pago = 0;
domic_pagando = 0;
domic_alugados = 0
for percorrer in exemploPesquisa['2.01']:
    if percorrer == '1':
        domic_pago += 1
    elif percorrer == '2':
        domic_pagando += 1
    elif percorrer == '3':
        domic_alugados += 1
print(domic_pago)
print(domic_pagando)
print(domic_alugados)
print("Quantos domicílios por cidade possuem banheiro e quantos não possuem, respectivamente:\n")
banheiro_sim = 0
banheiro_nao = 0
for percorrer in exemploPesquisa['2.02']:
    if percorrer == '1':
        banheiro_sim += 1
    elif percorrer != '1':
        banheiro_nao += 1
print(banheiro_sim)
print(banheiro_nao)
print("A forma  mais comum de abastecimento de água por cidade:\n")
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for percorrer in exemploPesquisa['2.05']:
    vetor[int(percorrer) - 1] += 1
maior_valor = 0
if maior_valor < vetor[0]:
    maior_velor = vetor[0]
elif maior_valor < vetor[1]:
    maior_valor = vetor[1]
elif maior_valor < vetor[2]:
    maior_valor = vetor[2]
elif maior_valor < vetor[3]:
    maior_valor = vetor[3]
elif maior_valor < vetor[4]:
    maior_valor = vetor[4]
elif maior_valor < vetor[5]:
    maior_valor = vetor[5]
elif maior_valor < vetor[6]:
    maior_valor = vetor[6]
elif maior_valor < vetor[7]:
    maior_valor = vetor[7]
elif maior_valor < vetor[8]:
    maior_valor = vetor[8]
elif maior_valor < vetor[9]:
    maior_valor = vetor[9]
print(maior_valor)
print("o percentual de domicílios por cidade que ainda não possuem energia elétrica:\n")
vetor = [0, 0, 0]
for percorrer in exemploPesquisa['2.07']:
    vetor[int(percorrer) - 1] += 1
total = vetor[0] + vetor[1] + vetor[2]
porcentagem = vetor[2] * 100 / total
print(porcentagem, '%')
print("o percentual de moradores que participaram da entrevista por cor ou raça:\n")
vetor = [0, 0, 0, 0, 0]
for percorrer in exemploPesquisa['4.03']:
    vetor[int(percorrer) - 1] += 1
total_cor = vetor[0] + vetor[1] + vetor[2] + vetor[3] + vetor[4]
cor_branca_porcentagem = vetor[0] * 100 / total_cor
cor_preta_porcentagem = vetor[1] * 100 / total_cor
cor_amarela_porcentagem = vetor[2] * 100 / total_cor
cor_parda_porcentagem = vetor[3] * 100 / total_cor
cor_indigena_porcentagem = vetor[4] * 100 / total_cor
print(cor_branca_porcentagem, '%')
print(cor_preta_porcentagem, '%')
print(cor_amarela_porcentagem, '%')
print(cor_parda_porcentagem, '%')
print(cor_indigena_porcentagem, '%')
print("A região com maior número de municípios pesquisados:\n")
nome_municipio = []
contador_municipio = []
for percorrer in exemploPesquisa['1.01']:
    if percorrer not in nome_municipio:
        nome_municipio.append(percorrer)
        contador_municipio.append(0)
    contador_municipio[nome_municipio.index(percorrer)] += 1
maior_valor_municipio = -1
cont_municipio = 0
posic_municipio = 0
for valor in contador_municipio:
    if valor > maior_valor_municipio:
        maior_valor_municipio = valor
        posic_municipio = nome_municipio[cont_municipio]
    cont_municipio += 1
nome_da_regiao = regioes['Posição'].index(posic_municipio)
print(regioes["Município"][nome_da_regiao])
