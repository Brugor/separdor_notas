from interface import titulos_textos as tx
from decimal import Decimal

notas = [100, 50, 20, 10]
indices = [0.1, 0.3, 0.3, 0.3]



def saca_metodo01(valor):
    for nota in notas:
        quantidade = valor // nota
        valor -= quantidade * nota
        print(f"{quantidade} notas de {nota} = {quantidade * nota}")

    tx.linha_dupla()

def saca_metodo02(valor):
    pass

def equalizador(valor):
    saldos = [10000, 5000, 2000, 1000]
    notas = [100, 50, 20, 10]
    quantidade_notas = []

    indices = []
    quant_temp = []
    notas_necessarias = []

    for i in range(4):
        if saldos[i] == 0:
            quantidade_notas.append(0)
        else:
            quantidade_notas.append(saldos[i] / notas[i])

        if notas[i] < valor:
            notas_necessarias.append(notas[i])
            quant_temp.append(quantidade_notas[i])

    for i in notas_necessarias:
        index_temp = notas.index(i)
        index = quantidade_notas[index_temp] / sum(quant_temp)
        indices.append(round(index, 3))



    print(f"Notas necessarias {notas_necessarias} e index são {indices}")
