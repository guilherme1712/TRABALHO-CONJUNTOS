# Guilherme De Quadro Daudt
arquivo = open('ex1.txt')  # variavel que abre o arquivo txt

operador = arquivo.readlines()  # variavel que lê as linhas do arquivo
nuemroOperacoes = int(operador[0])
contador = 0

cartesianoResposta = []  # matriz de resposta
diferencaResposta = []  # matriz de resposta
intersecaoResposta = []  # matriz de resposta
uniaoResposta = []  # matriz de resposta

for i in range(nuemroOperacoes): # for para repetição do tamanho do arquivo txt

    con0 = operador[2 + contador].split(',')
    con1 = []
    con2 = []

    for i in con0:
        con1.append(i.strip()) # for para preencher o conjunto 1

    con0 = operador[3 + contador].split(',')

    for i in con0:
        con2.append(i.strip()) # for para preencher o conjunto 2

    if operador[1 + contador].strip() == 'U': # checagem se a operação é de união
        for a in range(len(con1)):
            uniaoResposta.append(con1[a]) # preenche a resposta com o conjunto 1 de união
        for a in range(len(con2)):
            if con2[a] not in uniaoResposta: # checagem de repetição
                uniaoResposta.append(con2[a]) # preenche a resposta com o conjunto 2 de união
        print("União: conjunto 1 {" + ', '.join(con1) + "}, " + "conjunto 2 {" + ', '.join(
            con2) + "}. Resultado: {" + ', '.join(uniaoResposta) + "}")

    elif operador[1 + contador].strip() == 'I':
        for b in range(len(con1)):
            if con1[b] in con2:
                intersecaoResposta.append(con1[b])
        print("Interseção: conjunto 1 {" + ', '.join(con1) + "}, " + "conjunto 2 {" + ', '.join(
            con2) + "}. Resultado: {" + ', '.join(intersecaoResposta) + "}")

    elif operador[1 + contador].strip() == 'C':
        for d in range(len(con1)):
            for e in range(len(con2)):
                x = con1[d].replace(",", "")
                y = con2[e].replace(",", "")
                posicao = (x, y)
                cartesianoResposta.append(posicao)
        print("Produto Cartesiano: conjunto 1 {" + ', '.join(con1) + "}, " + "conjunto 2 {" + ', '.join(
            con2) + "}. Resultado: {", cartesianoResposta, "}")

    else:
        for c in range(len(con1)):
            if con1[c] not in con2:
                diferencaResposta.append(con1[c])
        for c in range(len(con2)):
            if con2[c] not in con1:
                diferencaResposta.append(con2[c])
        print("Diferença: conjunto 1 {" + ', '.join(con1) + "}, " + "conjunto 2 {" + ', '.join(
            con2) + "}. Resultado: {" + ', '.join(diferencaResposta) + "}")

    contador = contador + 3
'''Desenvolvido por Guilherme de Quadro Daudt!'''