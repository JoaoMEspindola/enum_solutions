class Solucao:
    def __init__(self, variaveisDecisao, funcaoObjetivo, viabilidade) -> None:
        self.variaveisDecisao = variaveisDecisao
        self.funcaoObjetivo = funcaoObjetivo
        self.viabilidade = viabilidade
        self.otima = False
    
    def toString(self):
        print(f'Solução: x={self.variaveisDecisao}, z={self.funcaoObjetivo}, {self.viabilidade}', '==> ótima' if self.otima == True else '')

    def setOptimal(self):
        self.otima = True
