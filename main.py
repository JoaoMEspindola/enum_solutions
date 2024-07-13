import dataManager

filename = input()
content = dataManager.readFullFile(f'trabalho_1_PO/assets/{filename}.txt')

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