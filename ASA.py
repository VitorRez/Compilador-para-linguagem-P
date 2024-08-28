class No: 
    def __init__(self, nome):
        self.nome = nome
        self.children = [] #vetor de filhos  
        self.value = 0
        self.op = None

    def __str__(self, level=0):
        ret = "   "*level+ repr(self) +"\n"
        if self.op != None: 
            ret += "   "*level+ self.op +"\n"
            level += 1
        for child in self.children:
            if (child != None):
                ret += child.__str__(level+1) #level+1
        return ret

class NoPrograma(No):
    def __init__(self, filhos): #filho é um vetor com NoFuncão
        No.__init__(self, 'Programa')
        self.children = filhos

    def __repr__(self):
        return 'Programa'

class NoFuncao(No):
    def __init__(self, filhos):
        No.__init__(self, 'Funcao')
        self.children = filhos

    def __repr__(self) -> str:
        return 'Funcao'

class NoFuncaoSeq(No):
    def __init__(self, filhos):    
        No.__init__(self, 'FuncaoSeq')
        self.children = filhos

    def __repr__(self) -> str:
        return 'FuncaoSeq'

class NoListaParams(No):
    def __init__(self, filhos):    
        No.__init__(self, 'ListaParams')
        self.children = filhos

    def __repr__(self) -> str:
        return 'ListaParams'

class NoTipoRetornoFuncao(No):
    def __init__(self, filhos):    
        No.__init__(self, 'TipoRetornoFuncao')
        self.children = filhos

    def __repr__(self) -> str:
        return 'TipoRetornoFuncao'

class NoListaParams2(No):
    def __init__(self, filhos):    
        No.__init__(self, 'ListaParams2')
        self.children = filhos

    def __repr__(self) -> str:
        return 'ListaParams2'

class NoType(No):
    def __init__(self, filhos):    
        No.__init__(self, 'Type')
        self.children = filhos

    def __repr__(self) -> str:
        return 'Type'

class NoBloco(No):
    def __init__(self, left, right):
        No.__init__(self, 'Bloco')
        self.children.append(left)
        self.children.append(right)

    def __repr__(self) -> str:
        return 'Bloco'

class NoSequencia(No):
    def __init__(self, left, right):
        No.__init__(self, 'Sequencia')
        self.children.append(left)
        self.children.append(right)

    def __repr__(self) -> str:
        return 'Sequencia'

class NoDeclaracao(No):
    def __init__(self, filhos):    
        No.__init__(self, 'Declaracao')
        self.children = filhos

    def __repr__(self) -> str:
        return 'Declaracao'

class VarList(No):
    def __init__(self, filhos):    
        No.__init__(self, 'VarList')
        self.children = filhos

    def __repr__(self) -> str:
        return 'VarList'

class NoVarList2(No):
    def __init__(self, filhos):    
        No.__init__(self, 'VarList2')
        self.children = filhos

    def __repr__(self) -> str:
        return 'VarList2'

class NoComando(No):
    def __init__(self, filhos):    
        No.__init__(self, 'Comando')
        self.children = filhos

    def __repr__(self) -> str:
        return 'Comando'

class NoAtribuicaoChamada(No):
    def __init__(self, filhos):    
        No.__init__(self, 'AtribuicaoChamada')
        self.children = filhos

    def __repr__(self) -> str:
        return 'AtribuicaoChamada'

class NoComandoIf(No):
    def __init__(self, filhos):    
        No.__init__(self, 'ComandoIf')
        self.children = filhos

    def __repr__(self) -> str:
        return 'ComandoIf'

class NoComandoSenao(No):
    def __init__(self, filhos):    
        No.__init__(self, 'ComandoSenao')
        self.children = filhos

    def __repr__(self) -> str:
        return 'ComandoSenao'

class NoExprAritmetica(No): #talvez mudar depois
    def __init__(self, op, left, right):
        No.__init__(self,'ExprAritmetica')
        self.children.append(left)
        self.children.append(right)
        self.op = op

    def __repr__(self):
        return "ExprAritmetica: " 
        
class NoExprOpc(No):
    def __init__(self, filhos):    
        No.__init__(self, 'ExprOpc')
        self.children = filhos

    def __repr__(self) -> str:
        return 'ExprOpc'

class NoOpIgual(No):
    def __init__(self, filhos):    
        No.__init__(self, 'OpIgual')
        self.children = filhos

    def __repr__(self) -> str:
        return 'OpIgual'

class NoRel(No):
    def __init__(self, filhos):    
        No.__init__(self, 'Rel')
        self.children = filhos

    def __repr__(self) -> str:
        return 'Rel'

class NoRelOpc(No):
    def __init__(self, filhos):    
        No.__init__(self, 'RelOpc')
        self.children = filhos

    def __repr__(self) -> str:
        return 'RelOpc'

class NoOpRel(No):
    def __init__(self, filhos):    
        No.__init__(self, 'OpRel')
        self.children = filhos

    def __repr__(self) -> str:
        return 'OpRel'

class NoId(No):
    def __init__(self, nome):
        No.__init__(self,nome)

    def __repr__(self):
        return "NoId: " + str(self.nome) 

class NoIntConst(No):
    def __init__(self, value):
        No.__init__(self,"NoInt")
        self.value = value

    def __repr__(self):
        return "NoInt: " + str(self.value)

class NoFloatConst(No):
    def __init__(self, value):
        No.__init__(self,"NoFloat")
        self.value = value

    def __repr__(self):
        return "NoFloat: " + str(self.value)
