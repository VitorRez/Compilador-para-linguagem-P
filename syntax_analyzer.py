from Token import *

class syntaxAnalyzer:

    def __init__(self, TokenP, TokenD):
        self.TokenP = TokenP
        self.TokenD = TokenD
        self.index = 0

    def imprimeErro(self, token):
        print('Erro sintático. Token ' + token.lexema + ' não esperado an entrada.')

    def match(self, token):
        if token.tokenind == self.TokenP[self.index].tokenind:
            self.index += 1
            if self.index < len(self.TokenP):
                token = self.TokenP[self.index]
        else:
            self.imprimeErro(token)

    def Programa(self):
        token = self.TokenP[0]