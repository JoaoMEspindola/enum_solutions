import itertools
import numpy as np
from solucao import Solucao

def readFullFile(fileName):
    with open(fileName, 'r') as textFile:
        return textFile.read()
    
def buildProblem(content):
    lines = content.strip().split('\n')
    qntdVariaveis, nmRestricoes = map(int, lines[0].split())

    coeficientesFuncaoObjetivo = np.array(list(map(int, lines[1].split())))

    coeficientesVariaveis = np.array([list(map(int, lines[i].split())) for i in range(2, 2 + nmRestricoes)])

    termosIndependentes = np.array(list(map(int, lines[2 + nmRestricoes].split())))

    return findCombinations(qntdVariaveis, nmRestricoes, coeficientesFuncaoObjetivo, coeficientesVariaveis, termosIndependentes)

def findCombinations(qntdVariaveis, nmRestricoes, coeficientesFuncaoObjetivo, coeficientesVariaveis, termosIndependentes):
    combinacoes = list(itertools.combinations(range(coeficientesVariaveis.shape[1]), nmRestricoes))
    listaDeVariaveis = []

    for combinacao in combinacoes:
        variaveisDecisao = solveCombination(combinacao, coeficientesVariaveis, termosIndependentes, qntdVariaveis)
        if variaveisDecisao is not None:
            listaDeVariaveis.append(variaveisDecisao)

    return buildSolutions(listaDeVariaveis, coeficientesFuncaoObjetivo)
   
def solveCombination(combinacoes, coeficientesVariaveis, termosIndependentes, qntdVariaveis):
    matrizCombinada = [coeficientesVariaveis[:, col] for col in combinacoes]

    try:
        variaveisDecisao = np.linalg.solve(np.transpose(matrizCombinada), termosIndependentes)
        coeficienteFinal = np.zeros(qntdVariaveis)
        for i in range(len(variaveisDecisao)):
            coeficienteFinal[combinacoes[i]] = variaveisDecisao[i]
        return tuple(coeficienteFinal)
    except np.linalg.LinAlgError:
        return None
    
def buildSolutions(listaDeVariaveis, coeficientesFuncaoObjetivo):
    listaSolucoes = []
    for v in listaDeVariaveis:
        estado = 'inviável' if any(num < 0 for num in v) else 'viável'
        funcaoObjetivo = sum(v*coeficientesFuncaoObjetivo)
        solucao = Solucao(v, funcaoObjetivo, estado)
        listaSolucoes.append(solucao)

    findBestSolution(listaSolucoes)
    return listaSolucoes

def findBestSolution(listaSolucoes):
    minimum = 0
    bestSolution = Solucao('', '', '')
    for solucao in listaSolucoes:
        if (solucao.viabilidade == 'viável' and solucao.funcaoObjetivo < minimum):
            minimum = solucao.funcaoObjetivo
            bestSolution = solucao
    bestSolution.setOptimal()