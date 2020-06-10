setores = list()
consumo = list()
print('Bem vindo ao simulador de consumo de energia. Por favor informe a quantidade de setores')
setores = list(); consumo = list()
idEquipamentos = ("Ar-condicionado", "Computador", "Geladeira", "Lampada", "Televisor")
potenciaEquipamentos = [-1, -1, -1, -1, -1]
total = int(input("Digite quantos setores existem\n"))
valor_equipamento_rs = list()
valor_consumo_total_real = list(); valor_consumo_total = list()
for count in range(0, total):
    n = 1; totalEquipamentos = [0, 0, 0, 0, 0]
    while n != 0:
        print("Escolha qual aparelho tem nesse setor:\n")
        print("1- Ar-condicionado\n2- Computador\n3- Geladeira\n4- Lampada\n5- Televisor\n")
        opc = int(input("Digite a opcao do aparelho\n"))
        totalEquipamentos[opc - 1] += 1; setorAtual = list()
        if not len(setores) < count + 1:
            setorAtual = setores[count]
        else:
            setores.append(setorAtual)
        equipamentos = list(); equipamentos.append(opc - 1)
        if potenciaEquipamentos[opc - 1] < 0:
            potenciaEquipamentos[opc - 1] = int(input("digite sua potencia\n"))
        equipamentos.append(int(input("digite a quantidade de horas de uso por dia\n")))
        equipamentos.append(int(input("digite a quantidade de dia de uso no mes\n")))
        setorAtual.append(equipamentos)
        n = int(input("Deseja colocar outro equipamento nesse setor?\n0- Nao\n1- Sim\n"))

    consumo_total = 0; consumo_equipamento_real = 0
    for equipamento in setores[count]:
        consumo = equipamento[1] * equipamento[2] * totalEquipamentos[equipamento[0]]
        consumo_total += consumo
        if consumo >= 0 and consumo < 31:
            valor_equipamento_rs = consumo * 0.17512250
        elif consumo >= 31 and consumo < 101:
            valor_equipamento_rs = consumo * 0.30021000
        elif consumo >= 101 and consumo < 150:
            valor_equipamento_rs = consumo * 0.45031500
        elif consumo > 150:
            valor_equipamento_rs = consumo * 0.50035000
        consumo_equipamento_real += valor_equipamento_rs
    valor_consumo_total_real.append(consumo_equipamento_real)

    if consumo_total >= 0 and consumo_total < 31:
        valor_consumo_total.append(consumo_total * 0.17512250)
    elif consumo_total >= 31 and consumo_total < 101:
        valor_consumo_total.append(consumo_total * 0.30021000)
    elif consumo_total >= 101 and consumo_total < 150:
        valor_consumo_total.append(consumo_total * 0.45031500)
    elif consumo_total > 150:
        valor_consumo_total.append(consumo_total * 0.50035000)

    valor_consumo_total_geral = 0
    for valor in valor_consumo_total:
        valor_consumo_total_geral += valor
    valor_consumo_total_geral_real = 0
    for valor in valor_consumo_total_real:
        valor_consumo_total_geral_real += valor

print("o consumo em Kwh de cada setor eh:\n", valor_consumo_total)
print("o valor em reais de cada setor eh\n", valor_consumo_total_real)
print("o consumo em Kwh geral eh:\n", valor_consumo_total_geral)
print("o valor em reais de cada setor eh\n", valor_consumo_total_geral_real)
valor_da_conta = valor_consumo_total_geral_real + (valor_consumo_total_geral_real * 0.27) + (valor_consumo_total_geral_real * 0.0165) + (valor_consumo_total_geral_real * 0.0761)
print("o valor da conta de energia eh:\n", valor_da_conta)
