import dataManager

content = dataManager.readFullFile('trabalho_1_PO/assets/exemplo1.txt')

listaSolucoes = dataManager.buildProblem(content)

for solucao in listaSolucoes:
    solucao.toString()