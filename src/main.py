import dataManager

while True:
    try:
        filename = input()
        content = dataManager.readFullFile(f'assets/{filename}.txt')
        break
    except FileNotFoundError:
        print("Arquivo não encontrado. Tente novamente.")


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