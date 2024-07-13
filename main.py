import dataManager

content = dataManager.readFullFile('trabalho_1_PO/assets/exemplo1.txt')

listaSolucoes = dataManager.buildProblem(content)

solucoesViaveis = 0
solucoesInviaveis = 0
for solucao in listaSolucoes:
    solucao.toString()
    if solucao.viabilidade == 'viável':
        solucoesViaveis += 1
    else:
        solucoesInviaveis += 1

print(f'\nSoluções básicas viáveis:   {solucoesViaveis}\nSoluções básicas inviáveis: {solucoesInviaveis}')