class AstNode: 
    def __init__(self, nome):
        self.nome = nome
        self.children = [] #vetor de filhos  
        self.value = 0
        self.op = None
        self.dataType = None

    def addFilho(self, filho):
        self.children.append(filho)

    # def __str__(self, level=0):
    #     ret = "   "*level+ repr(self) +"\n"
    #     if self.op != None: 
    #         ret += "   "*level+ self.op +"\n"
    #         level += 1
    #     for child in self.children:
    #         if (child != None):
    #             ret += child.__str__(level+1) #level+1
    #     return ret

class NoFuncao(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Funcao')

    def __repr__(self) -> str:
        return 'Funcao'

class NoRelOp(AstNode):
    def __init__(self, op):
        AstNode.__init__(self, 'RelOp')
        self.op = op

    def __repr__(self) -> str:
        return 'RelOp'

class NoArithOp(AstNode):
    def __init__(self, op):
        AstNode.__init__(self, 'NoArithOp')
        self.op = op

    def __repr__(self) -> str:
        return 'NoArithOp'

class NoAssign(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Assign')

    def __repr__(self) -> str:
        return 'Assign'

class NoIf(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'If')

    def addFilho(self, left, right, senao=None): #talvez n precise desse valor padrao
        self.children.append(left) #Condição do if
        self.children.append(right) #Comandos da parte verdadeira

        if senao != None: self.children.append(senao) #Comandos da parte false
    
    def __repr__(self) -> str:
        return 'If'

class NoWhile(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'While')

    def __repr__(self) -> str:
        return 'While'

class NoPrint(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Print')

    def attPularLinha(self, pularLinha):
        self.pularLinha = pularLinha

    def __repr__(self) -> str:
        return 'Print'

class NoReturn(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Return')

    def __repr__(self) -> str:
        return 'Return'

class NoCall(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Call')

    def __repr__(self) -> str:
        return 'Call'

class NoBloco(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Bloco')
        
    # def addFilho(self, filho): #filho é um vetor
    #     self.children = filho

    def __repr__(self) -> str:
        return 'Bloco'


class NoId(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'Id')
        # self.lexema = lexema
        # print(f'lex: {self.lexema}')

    def __repr__(self) -> str:
        return 'Id'

class NoIntConst(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'IntConst')
        self.dataType = 'Int'

    def __repr__(self) -> str:
        return 'IntConst'

class NoFloatConst(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'FloatConst')
        self.dataType = 'Float'

    def __repr__(self) -> str:
        return 'FloatConst'

class NoCharConst(AstNode):
    def __init__(self):
        AstNode.__init__(self, 'CharConst')
        self.dataType = 'Char'

    def __repr__(self) -> str:
        return 'CharConst'