from SymbolTable import *
from Token import *
from ASA import *
import sys

class syntaxAnalyzer:

    def __init__(self, TokenP):
        self.TokenP = TokenP
        self.function_tables = {}
        self.SymbolTable = SymbolTable()
        self.GlobalTable = SymbolTable()
        self.index = 0
        self.current_function = None

    def imprimeErro(self):
        print('Erro sintático. Token ' + self.TokenP[self.index].tokenind + ' não esperado na entrada.' + str(self.TokenP[self.index].num_linha))
        sys.exit()

    def imprimeErroS(self, message):
        print(message)
        sys.exit()

    def match(self, token):
        if token == self.TokenP[self.index].tokenind:
            if self.index < len(self.TokenP):
                self.index += 1
        else:
            self.imprimeErro()
        
    def Programa(self):
        global vecArvores
        vecArvores = [] 

        if self.TokenP[self.index].tokenind == "Function":
            self.Funcao()
            self.FuncaoSeq()
            if(self.TokenP[self.index].tokenind == 'EOF'):
                self.match('EOF')
                print('Fim da análise sintática')
                for i in vecArvores: print(i)
        else:
            self.imprimeErro()

    def FuncaoSeq(self):
        if self.TokenP[self.index].tokenind == "Function":
            self.Funcao()
            self.FuncaoSeq()

    def Funcao(self):
        global vecArvores
        
        num_args = 0
        if self.TokenP[self.index].tokenind == "Function":
            self.match("Function")
            noFunc = NoFuncao()
            vecArvores.append(noFunc)
            self.match("ID")
            self.current_function = self.TokenP[self.index-1].lexema
            if self.current_function in self.function_tables.keys():
                self.imprimeErroS(f"Erro na linha {self.TokenP[self.index-1].num_linha}: redeclaração da função {self.current_function}.")
                sys.exit()
            self.function_tables[self.current_function] = SymbolTable()
            name = self.TokenP[self.index-1].lexema
            self.match("LParen")
            args = []
            num_args = self.ListaParams(num_args, args)
            self.match("RParen")
            return_type = self.TipoRetornoFuncao()
            entry = SymbolTableEntry(
                name,
                return_type,
                -1,
                True,
                num_args,
                args)
            self.GlobalTable.insert(entry)
            noBloco = self.Bloco()
            noFunc.addFilho(noBloco)
        else:
            self.imprimeErro()

    def ListaParams(self, param_count, args):
        if self.TokenP[self.index].tokenind == "ID":
            param_name = self.TokenP[self.index].lexema
            self.match("ID")
            self.match("Colon")
            args.append(param_name)
            param_type = self.Type()
            param_pos = param_count
            entry = SymbolTableEntry(
                param_name,
                param_type,
                param_pos,
                False,
                -1,
                []
            )
            self.function_tables[self.current_function].insert(entry)
            param_count = self.ListaParams2(param_count, args)
        return param_count + 1
        
        
    def ListaParams2(self, param_count, args):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            param_name = self.TokenP[self.index].lexema
            args.append(param_name)
            self.match("ID")
            self.match("Colon")
            param_type = self.Type()
            param_count += 1
            param_pos = param_count
            entry = SymbolTableEntry(
                param_name,
                param_type,
                param_pos,
                False,
                -1,
                []
            )
            self.function_tables[self.current_function].insert(entry)
            param_count = self.ListaParams2(param_count, args)
        return param_count

    def TipoRetornoFuncao(self):
        tipo = -1
        if self.TokenP[self.index].tokenind == "Arrow":
            self.match("Arrow")
            tipo = self.Type()
        return tipo
    
    def Bloco(self):
        no = NoBloco()

        if self.TokenP[self.index].tokenind == "LBrace":
            self.match("LBrace")
            self.Sequencia(no)
            print(f'flhos Bloco: {no.children}') #pra verificar se precisa de um retorno na linha de cima
            self.match("RBrace")
        else:
            self.imprimeErro()

        return no

    def Sequencia(self, noBloco=None): #n sei se precisar desse valor padrao
        if self.TokenP[self.index].tokenind == "Let":
            seq = self.Declaracao()
            noBloco.addFilho(seq)
            self.Sequencia(noBloco)
        elif(self.TokenP[self.index].tokenind == "ID" or self.TokenP[self.index].tokenind == "If" or
             self.TokenP[self.index].tokenind == "While" or self.TokenP[self.index].tokenind == "Print" or
             self.TokenP[self.index].tokenind == "Println" or self.TokenP[self.index].tokenind == "Return"):
            seq = self.Comando()
            noBloco.addFilho(seq)
            self.Sequencia(noBloco)

    def Declaracao(self):
        if self.TokenP[self.index].tokenind == "Let":
            var_names = []
            num_linha = self.TokenP[self.index].num_linha
            self.match("Let")
            self.VarList(var_names)
            self.match("Colon")
            var_type = self.Type()
            for var_name in var_names:
                entry = SymbolTableEntry(
                    var_name,  
                    var_type,
                    -1,
                    False,
                    -1,
                    []
                )
                try:
                    self.function_tables[self.current_function].insert(entry)
                except:
                    print(f"Erro na linha {num_linha}: redeclaração da variável {var_name}.")
                    sys.exit()
            self.match("Semicolon")
        else:
            self.imprimeErro()
    
    def VarList(self, var_names):
        if self.TokenP[self.index].tokenind == "ID":
            var_names.append(self.TokenP[self.index].lexema)
            self.match("ID")
            self.VarList2(var_names)
        else:
            self.imprimeErro()

    def VarList2(self, var_names):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            var_names.append(self.TokenP[self.index].lexema)
            self.match("ID")
            self.VarList2(var_names)

    def Type(self):
        if self.TokenP[self.index].tokenind == "Int":
            self.match("Int")
            return(1)
        elif self.TokenP[self.index].tokenind == "Float":
            self.match("Float")
            return(2)
        elif self.TokenP[self.index].tokenind == "Char":
            self.match("Char")
            return(0)
        else:
            self.imprimeErro()

    def Comando(self):
        arg_count = 0
        args = ["sys_call(print)"]
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            noId = NoId()
            node = self.AtribuicaoOuChamada(noId)
            return node
        elif self.TokenP[self.index].tokenind == "If":
            node = self.ComandoIf()
            return node
        elif self.TokenP[self.index].tokenind == "While":
            self.match("While")
            noWhile = NoWhile()
            expr = self.Expr()
            bloco = self.Bloco()
            noWhile.addFilho(expr)
            noWhile.addFilho(bloco)
            return noWhile
        elif self.TokenP[self.index].tokenind == "Print":
            self.match("Print")
            noPrint = NoPrint()
            self.match("LParen")
            self.match("FormattedString")
            self.match("Comma")
            argFilhos = self.ListaArgs(arg_count, args)
            noPrint.addFilho(argFilhos)
            self.match("RParen")
            self.match("Semicolon")
            entry = SymbolTableEntry(
                "print",
                -1,
                -1,
                True,
                2,
                args
            )
            self.function_tables[self.current_function].insert(entry)
            return noPrint
        elif self.TokenP[self.index].tokenind == "Println":
            self.match("Println")
            noPrint = NoPrint()
            self.match("LParen")
            self.match("FormattedString")
            self.match("Comma")
            argsFilho = self.ListaArgs(arg_count, args)
            noPrint.addFilho(argsFilho)
            self.match("RParen")
            self.match("Semicolon")
            entry = SymbolTableEntry(
                "println",
                -1,
                -1,
                True,
                2,
                args
            )
            self.function_tables[self.current_function].insert(entry)
            return noPrint
        elif self.TokenP[self.index].tokenind == "Return":
            self.match("Return")
            noReturn = NoReturn()
            expr = self.Expr()
            noReturn.addFilho(expr)
            self.match("Semicolon")
            return noReturn
        else:
            self.imprimeErro()
    
    def AtribuicaoOuChamada(self, id):
        if self.TokenP[self.index].tokenind == "Assign":
            self.match("Assign")
            noAssign = NoAssign()
            noAssign.addFilho(id)
            noExpr = self.Expr()
            noAssign.addFilho(noExpr)
            self.match("Semicolon")
            return noAssign
        elif self.TokenP[self.index].tokenind == "LParen":
            self.match("LParen")
            noCall = NoCall()
            args = self.ListaArgs(0, [])
            noCall.addFilho(args)
            self.match("RParen")
            return noCall
        else:
            self.imprimeErro()
    
    def ComandoIf(self):
        if self.TokenP[self.index].tokenind == "If":
            self.match("If")
            noIf = NoIf()
            condicao = self.Expr()
            bloco = self.Bloco()
            senao = self.ComandoSenao()
            noIf.addFilho(condicao, bloco, senao)
            return noIf
        elif self.TokenP[self.index].tokenind == "LBrace":
            self.match("LBrace")
            noBloco = NoBloco()
            seq = self.Sequencia()
            noBloco.addFilho(seq)
            self.match("RBrace")
            return noBloco
        else:
            self.imprimeErro()

    def ComandoSenao(self):
        if self.TokenP[self.index].tokenind == "Else":
            self.match("Else")
            blocoSeNao = self.ComandoIf()
            return blocoSeNao 
    
    def Expr(self):
        rel = self.Rel()
        expr = self.ExprOpc(rel)
        return expr

    def ExprOpc(self, operando):
        if self.TokenP[self.index].tokenind == "Equal" or self.TokenP[self.index].tokenind == "NotEqual":
            noIgual = self.OpIgual()
            noIgual.addFilho(operando)
            rel = self.Rel()
            noIgual.addFilho(rel)
            self.ExprOpc(noIgual)
        else:
            return operando

    def OpIgual(self):
        if self.TokenP[self.index].tokenind == "Equal":
            self.match("Equal")
            noRel = NoRelOp('==')
            return noRel
        elif self.TokenP[self.index].tokenind == "NotEqual":
            self.match("NotEqual")
            noRel = NoRelOp('!=')
            return noRel
        else:
            self.imprimeErro()
    
    def Rel(self):
        adicao = self.Adicao()
        rel = self.RelOpc(adicao)
        return rel

    def RelOpc(self, operando):
        if(self.TokenP[self.index].tokenind == "LessThan" or self.TokenP[self.index].tokenind == "LessThanEqual" or
           self.TokenP[self.index].tokenind == "GreaterThan" or self.TokenP[self.index].tokenind == "GreaterThanEqual"):
            opRel = self.OpRel()
            opRel.addFilho(operando)
            operando2 = self.Adicao()
            opRel.addFilho(operando2)
            self.RelOpc(opRel)
        else:
            return operando
    
    def OpRel(self):
        if self.TokenP[self.index].tokenind == "LessThan":
            self.match("LessThan")
            noRel = NoRelOp('<')
            return noRel
        elif self.TokenP[self.index].tokenind == "LessThanEqual":
            self.match("LessThanEqual")
            noRel = NoRelOp('<=')
            return noRel
        elif self.TokenP[self.index].tokenind == "GreaterThan":
            self.match("GreaterThan")
            noRel = NoRelOp('>')
            return noRel
        elif self.TokenP[self.index].tokenind == "GreaterThanEqual":
            self.match("GreaterThanEqual")
            noRel = NoRelOp('>=')
            return noRel
        else:
            self.imprimeErro()

    def Adicao(self):
        termo = self.Termo()
        adic = self.AdicaoOpc(termo)
        return adic

    def AdicaoOpc(self, operando):
        if(self.TokenP[self.index].tokenind == "Plus" or self.TokenP[self.index].tokenind == "Minus"):
            noAdic = self.OpAdicao()
            noAdic.addFilho(operando)
            operando2 = self.Termo()
            noAdic.addFilho(operando2)
            self.AdicaoOpc(noAdic)
        else:
            return operando

    def OpAdicao(self):
        if self.TokenP[self.index].tokenind == "Plus":
            self.match("Plus")
            noArith = NoArithOp('+')
            return noArith
        elif self.TokenP[self.index].tokenind == "Minus":
            self.match("Minus")
            noArith = NoArithOp('-')
            return noArith
        else:
            self.imprimeErro()
    
    def Termo(self):
        fator = self.Fator()
        termo = self.TermoOpc(fator)
        return termo

    def TermoOpc(self, operando):
        if(self.TokenP[self.index].tokenind == "Multiplication" or self.TokenP[self.index].tokenind == "Division"):
            noMult = self.OpMult()
            noMult.addFilho(operando)
            operando2 = self.Fator()
            noMult.addFilho(operando2)
            self.TermoOpc(noMult)
        else:
            return operando
    
    def OpMult(self):
        if self.TokenP[self.index].tokenind == "Multiplication":
            self.match("Multiplication")
            noArith = NoArithOp('*')
            return noArith
        elif self.TokenP[self.index].tokenind == "Division":
            self.match("Division")
            noArith = NoArithOp('/')
            return noArith
        else:
            self.imprimeErro()

    def Fator(self):
        if self.TokenP[self.index].tokenind == "ID":
            self.match("ID")
            noId = NoId()
            callNode = self.ChamadaFuncao(noId)
            return callNode
        elif self.TokenP[self.index].tokenind == "IntConst":
            self.match("IntConst")
            noInt = NoIntConst()
            return noInt
        elif self.TokenP[self.index].tokenind == "FloatConst":
            self.match("FloatConst")
            noFloat = NoFloatConst()
            return noFloat
        elif self.TokenP[self.index].tokenind == "CharConst":
            self.match("CharConst")
            noChar = NoCharConst()
            return noChar
        elif self.TokenP[self.index].tokenind == "LParen":
            print("fator")
            self.match("LParen")
            expr = self.Expr()
            self.match("RParen")
            return expr
        else:
            self.imprimeErro()

    def ChamadaFuncao(self, noId=None):
        num_args = 0
        if self.TokenP[self.index].tokenind == "LParen":
            func_name = self.TokenP[self.index-1].lexema
            func_entry = self.GlobalTable.lookup(func_name)
            if not func_entry or not func_entry.is_call:
                self.imprimeErro()
            self.match("LParen")
            callNode = NoCall()
            args = []
            num_args += self.ListaArgs(num_args, args, callNode)
            print(f'args: {callNode.children}')
            if num_args != func_entry.num_args:
                self.imprimeErroS(f"Erro na linha {self.TokenP[self.index-2].num_linha}: {func_entry.name} espera {func_entry.num_args} parametros, foram dados {num_args}.")
            entry = SymbolTableEntry(
                func_name,
                func_entry.data_type,
                -1,
                True,
                num_args,
                args
            )
            self.function_tables[self.current_function].insert(entry)
            self.match("RParen")

            return callNode
        else:
            return noId
    
    def ListaArgs(self, num_args, args, noCall=None):
        if(self.TokenP[self.index].tokenind == "ID" or self.TokenP[self.index].tokenind == "IntConst" or
           self.TokenP[self.index].tokenind == "FloatConst" or self.TokenP[self.index].tokenind == "CharConst" or
           self.TokenP[self.index].tokenind == "LParen"):
            args.append(self.TokenP[self.index].lexema)
            fator = self.Fator()
            if noCall != None: noCall.addFilho(fator)
            num_args += self.ListaArgs2(num_args, args, noCall)
            num_args += 1
        return num_args
    
    def ListaArgs2(self, num_args, args, noCall):
        if self.TokenP[self.index].tokenind == "Comma":
            self.match("Comma")
            args.append(self.TokenP[self.index].lexema)
            fator = self.Fator()
            if noCall != None: noCall.addFilho(fator)
            num_args += self.ListaArgs2(num_args, args, noCall)
            num_args += 1
        return num_args
    
    def imprimeTabelas(self):
        for function_name, table in self.function_tables.items():
            print(f"Tabela de símbolos da função {function_name}:")
            print("Chave          | Nome           | Tipo           | Param. Pos     | Call           | Num. Args      | Args")
            print("---------------------------------------------------------------------------------------------------------------------")
            print(table)
            print()

    def imprime(self):
        for function_name, table in self.function_tables.items():
            print(function_name)
            for name, entry in table.table.items():
                print(entry.name, entry.data_type, entry.param_pos, entry.is_call, entry.num_args, entry.args)
