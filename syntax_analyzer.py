from Token import *

class syntaxAnalyzer:

    def __init__(self, TokenP):
        self.TokenP = TokenP
        self.CurrentToken = TokenP[0].tokenind
        self.index = 0

    def imprimeErro(self):
        print('Erro sintático. Token ' + self.TokenP[self.index].tokenind + ' não esperado na entrada.')

    def match(self, token):
        #print(token, self.TokenP[self.index].tokenind)
        if token == self.TokenP[self.index].tokenind:
            self.index += 1
            if self.index < len(self.TokenP):
                token = self.TokenP[self.index].tokenind
        else:
            self.imprimeErro()
        
    def Programa(self):
        if self.TokenP[self.index].tokenind == "Function":
            self.Funcao()
            self.FuncaoSeq()
            if(self.TokenP[self.index].tokenind == 'EOF'):
                self.match('EOF')
                print('Fim da análise sinetática')
        else:
            self.imprimeErro()

    def FuncaoSeq(self):
        if self.TokenP[self.index].tokenind == "Function":
            self.Funcao()
            self.FuncaoSeq()

    def Funcao(self):
        if self.TokenP[self.index].tokenind == "Function":
            self.match("Function")
            self.match("ID")
            self.match("LParen")
            self.ListaParams()
            self.match("RParen")
            self.TipoRetornoFuncao()
            self.Bloco()
        else:
            self.imprimeErro()

    def ListaParams(self):
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            self.match("Colon")
            self.Type()
            self.ListaParams2()
        
    def ListaParams2(self):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            self.match("ID")
            self.match("Colon")
            self.Type()
            self.ListaParams2()

    def TipoRetornoFuncao(self):
        if self.TokenP[self.index].tokenind == "Arrow":
            self.match("Arrow")
            self.Type()
    
    def Bloco(self):
        if self.TokenP[self.index].tokenind == "LBrace":
            self.match("LBrace")
            self.Sequencia()
            self.match("RBrace")
        else:
            self.imprimeErro()

    def Sequencia(self):
        if self.TokenP[self.index].tokenind == "Let":
            self.Declaracao()
            self.Sequencia()
        elif(self.TokenP[self.index].tokenind == "ID" or self.TokenP[self.index].tokenind == "If" or
             self.TokenP[self.index].tokenind == "While" or self.TokenP[self.index].tokenind == "Print" or
             self.TokenP[self.index].tokenind == "Println" or self.TokenP[self.index].tokenind == "Return"):
            self.Comando()
            self.Sequencia()

    def Declaracao(self):
        if self.TokenP[self.index].tokenind == "Let":
            self.match("Let")
            self.VarList()
            self.match("Colon")
            self.Type()
            self.match("Semicolon")
        else:
            self.imprimeErro()
    
    def VarList(self):
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            self.VarList2()
        else:
            self.imprimeErro()

    def VarList2(self):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            self.match("ID")
            self.VarList2()

    def Type(self):
        if self.TokenP[self.index].tokenind == "Int":
            self.match("Int")
        elif self.TokenP[self.index].tokenind == "Float":
            self.match("Float")
        elif self.TokenP[self.index].tokenind == "Char":
            self.match("Char")
        else:
            self.imprimeErro()

    def Comando(self):
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            self.AtribuicaoOuChamada()
        elif self.TokenP[self.index].tokenind == "If":
            self.ComandoIf()
        elif self.TokenP[self.index].tokenind == "While":
            self.match("While")
            self.Expr()
            self.Bloco()
        elif self.TokenP[self.index].tokenind == "Print":
            self.match("Print")
            self.match("LParen")
            self.match("FormattedString")
            self.match("Comma")
            self.ListaArgs()
            self.match("RParen")
            self.match("Semicolon")
        elif self.TokenP[self.index].tokenind == "Println":
            self.match("Println")
            self.match("LParen")
            self.match("FormattedString")
            self.match("Comma")
            self.ListaArgs()
            self.match("RParen")
            self.match("Semicolon")
        elif self.TokenP[self.index].tokenind == "Return":
            self.match("Return")
            self.Expr()
            self.match("Semicolon")
        else:
            self.imprimeErro()
    
    def AtribuicaoOuChamada(self):
        if self.TokenP[self.index].tokenind == "Assign":
            self.match("Assign")
            self.Expr()
            self.match("Semicolon")
        elif self.TokenP[self.index].tokenind == "LParen":
            self.match("LParen")
            self.ListaArgs()
            self.match("RParen")
        else:
            self.imprimeErro()
    
    def ComandoIf(self):
        if self.TokenP[self.index].tokenind == "If":
            self.match("If")
            self.Expr()
            self.Bloco()
            self.ComandoSenao()
        elif self.TokenP[self.index].tokenind == "LBrace":
            self.match("LBrace")
            self.Sequencia()
            self.match("RBrace")
        else:
            self.imprimeErro()

    def ComandoSenao(self):
        if self.TokenP[self.index].tokenind == "Else":
            self.match("Else")
            self.ComandoIf()
    
    def Expr(self):
        self.Rel()
        self.ExprOpc()

    def ExprOpc(self):
        if self.TokenP[self.index].tokenind == "Equal" or self.TokenP[self.index].tokenind == "NotEqual":
            self.OpIgual()
            self.Rel()
            self.ExprOpc()

    def OpIgual(self):
        if self.TokenP[self.index].tokenind == "Equal":
            self.match("Equal")
        elif self.TokenP[self.index].tokenind == "NotEqual":
            self.match("NotEqual")
        else:
            self.imprimeErro()
    
    def Rel(self):
        self.Adicao()
        self.RelOpc()

    def RelOpc(self):
        if(self.TokenP[self.index].tokenind == "LessThan" or self.TokenP[self.index].tokenind == "LessThanEqual" or
           self.TokenP[self.index].tokenind == "GreaterThan" or self.TokenP[self.index].tokenind == "GreaterThanEqual"):
            self.OpRel()
            self.Adicao()
            self.RelOpc()
    
    def OpRel(self):
        if self.TokenP[self.index].tokenind == "LessThan":
            self.match("LessThan")
        elif self.TokenP[self.index].tokenind == "LessThanEqual":
            self.match("LessThanEqual")
        elif self.TokenP[self.index].tokenind == "GreaterThan":
            self.match("GreaterThan")
        elif self.TokenP[self.index].tokenind == "GreaterThanEqual":
            self.match("GreaterThanEqual")
        else:
            self.imprimeErro()

    def Adicao(self):
        self.Termo()
        self.AdicaoOpc()

    def AdicaoOpc(self):
        if(self.TokenP[self.index].tokenind == "Plus" or self.TokenP[self.index].tokenind == "Minus"):
            self.OpAdicao()
            self.Termo()
            self.AdicaoOpc()

    def OpAdicao(self):
        if self.TokenP[self.index].tokenind == "Plus":
            self.match("Plus")
        elif self.TokenP[self.index].tokenind == "Minus":
            self.match("Minus")
        else:
            self.imprimeErro()
    
    def Termo(self):
        self.Fator()
        self.TermoOpc()

    def TermoOpc(self):
        if(self.TokenP[self.index].tokenind == "Multiplication" or self.TokenP[self.index].tokenind == "Division"):
            self.OpMult()
            self.Fator()
            self.TermoOpc()
    
    def OpMult(self):
        if self.TokenP[self.index].tokenind == "Multiplication":
            self.match("Multiplication")
        elif self.TokenP[self.index].tokenind == "Division":
            self.match("Division")
        else:
            self.imprimeErro()

    def Fator(self):
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            self.ChamadaFuncao()
        elif self.TokenP[self.index].tokenind == "IntConst":
            self.match("IntConst")
        elif self.TokenP[self.index].tokenind == "FloatConst":
            self.match("FloatConst")
        elif self.TokenP[self.index].tokenind == "CharConst":
            self.match("CharConst")
        elif self.TokenP[self.index].tokenind == "LParen":
            self.match("LParen")
            self.Expr()
            self.match("RParen")
        else:
            self.imprimeErro()

    def ChamadaFuncao(self):
        if self.TokenP[self.index].tokenind == "LParen":
            self.match("LParen")
            self.ListaArgs()
            self.match("RParen")
    
    def ListaArgs(self):
        if(self.TokenP[self.index].tokenind == "ID" or self.TokenP[self.index].tokenind == "IntConst" or
           self.TokenP[self.index].tokenind == "FloatConst" or self.TokenP[self.index].tokenind == "CharConst" or
           self.TokenP[self.index].tokenind == "LParen"):
            self.Fator()
            self.ListaArgs2()
    
    def ListaArgs2(self):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            self.Fator()
            self.ListaArgs2()
        