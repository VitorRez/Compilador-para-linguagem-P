#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 10:28:28 2017

@author: alexandre
"""

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.lexema = value
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER_CONST, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {lexema})'.format(
            type= tokenNames[self.type],
            lexema=self.lexema
        )

    def __repr__(self):
        return self.__str__()

"""
 A tabela de símbolos é implementada como uma classe com o seguinte campo:
     - Map<string,TableEntry> symbolTable; //Um mapa de objetos tableEntry
"""
"""
 TableEntry é uma classe que possui os seguintes campos:
     - lexema
     - tipo
     - ponteiro para o valor
     - num da linha
"""
class SymbolTable(object):
    def __init__(self):
        self.symbolTable = {}

    def insertEntry(self, lexema, entry):
        self.symbolTable[lexema] = entry;

    def getEntry(self, lexema):
        return self.symbolTable[lexema]

class TableEntry(object):
    def __init__(self, lexema, tipo, num_linha, ref_valor):
        self.lexema = lexema
        self.tipo = tipo
        self.num_linha = num_linha
        self.ref_valor = ref_valor

    def setTipo(self, tipo):
        self.tipo = tipo

    def setRefValor(self, rv):
        self.ref_valor = rv

#Lista de Tokens
EOF = -1
ID = 0
NUM = 1
LBRACKET = 2
RBRACKET = 3
PLUS = 4
MINUS = 5
MULT = 6
DIV = 7

opmap = {}
opmap[PLUS] = '+'
opmap[MINUS] = '-'
opmap[MULT] = '*'
opmap[DIV] = '/'
currentOp = None

#Dicionário (Map) que mapeia os nomes dos tokens aos códigos dos tokens
tokenNames = {}
tokenNames[EOF] = 'EOF';
tokenNames[ID] = 'ID'
tokenNames[NUM] = 'NUM'
tokenNames[LBRACKET] = 'LBRACKET'
tokenNames[RBRACKET] = 'RBRACKET'
tokenNames[PLUS] = 'PLUS'
tokenNames[MINUS] = 'MINUS'
tokenNames[MULT] = 'MULT'
tokenNames[DIV] = 'DIV'

#vetorTokens = ['ID','PLUS','LBRACKET','NUM','RBRACKET', 'EOF']

tk1 = Token(ID, 'a')
tkplus = Token(PLUS, '+')

tk4 = Token(NUM, '12')

tkdiv = Token(DIV, '/')
tk6 = Token(ID, 'b')

tkeof = Token(EOF, 'EOF')
tklbracket = Token(LBRACKET, '(')
tkrbracket = Token(RBRACKET, ')')
tkminus = Token(MINUS, '-')
tkmult = Token(MULT, '*')

tknum1 = Token(NUM, '3')
tknum2 = Token(NUM, '5')
tknum3 = Token(NUM, '2')

#vetorTokens = [ID, PLUS, LBRACKET, NUM, DIV,LBRACKET, ID, MINUS, ID, RBRACKET, RBRACKET, MULT, ID, MULT, ID, EOF]
#vetorTokens = [tk1, tk2, tklbracket, tk4, tk5, tklbracket, tk1, tkminus, tk1,
 #              tkrbracket, tkrbracket, tkmult, tk1, tkmult, tk1, tkeof]

#vetorTokens = [tknum1, tkmult, tknum2,tkmult,tknum3, tkeof]
#vetorTokens = [tknum1, tkmult, tknum2, tkdiv, tklbracket, tknum2, tkplus, tknum2,
#              tkrbracket, tkmult, tknum1, tkmult, tknum2, tkeof]

#Entrada a + 12 * b  ID PLUS NUM MULT ID EOF 
vetorTokens = [tk1, tkplus, tk6, tkeof] #vetor de objetos do tipo Token

#vetorTokens = [ID, MULT, ID, MULT, ID, MULT, NUM, EOF]

i = 0
token = vetorTokens[i]

Follow = {}
Follow[NUM] = ['MULT','DIV','PLUS','MINUS','RBRACKET','EOF']
Follow[ID] = ['MULT','DIV','PLUS','MINUS','RBRACKET','EOF']
Follow[LBRACKET] = ['ID','NUM', 'LBRACKET']
Follow[MINUS] = ['ID','NUM', 'LBRACKET']
Follow[PLUS] = ['ID','NUM', 'LBRACKET']
Follow[MULT] = ['ID','NUM', 'LBRACKET']
Follow[DIV] = ['ID','NUM', 'LBRACKET']
conjSincronismo = [NUM, ID,LBRACKET,MULT,DIV,PLUS,MINUS,RBRACKET,EOF]

# def sincroniza(sync_token):
#     global token, i;
#     print('Sincronizando token ' + repr(sync_token))
#     while (i < len(vetorTokens)):
#         token = vetorTokens[i]
#         print('Analisando token ' + repr(token))
#         if (tokenNames[token.type] in Follow[sync_token.type]):
#             print('Sincronizado com o token ' + repr(token))
#             i = i + 1
#             token = vetorTokens[i]
#             print('A análise irá continuar do token ' + repr(token))
#             return;
#         i = i + 1
#     print('Não foi possível sincronizar. Saindo.')

def imprimeErro():
    global token, i
    print('Erro sintático. Token ' + repr(token) + ' não esperado na entrada.')
    i = i - 1
    sync_token = vetorTokens[i]
    print('Tokens ' + str(Follow[sync_token.type]) + ' esperados na entrada.')
    #continua a análise para verificar outros erros
    i = i + 1
    token = vetorTokens[i]
    #sincroniza(sync_token)

def match(tok):
    global token, i
    if(token.type == tok):
        print('Token ' + repr(token) + ' reconhecido na entrada.')
        i = i + 1
        if (i < len(vetorTokens)):
            token = vetorTokens[i]
    else:
        imprimeErro()

def E():
    print("Ativação de E()")
    global token
    if (token.type == ID or token.type == NUM or token.type == LBRACKET):
        T()
        E_()
        if(token.type == EOF):
            match(EOF)
            print('Fim da análise sintática.')
    else:
        imprimeErro()

def E_():
    print("Ativação de E_()")
    global token
    if(token.type == PLUS):        
        match(PLUS)
        T()
        E_()
    elif (token.type == MINUS):
        match(MINUS)
        T()
        E_()

def T():
    print("Ativação de T()")
    global token
    if (token.type == ID or token.type == NUM or token.type == LBRACKET):
        F()
        T_()
    else: 
        imprimeErro()

def T_():
    print("Ativação de T_()")
    global token
    if (token.type == MULT):
        match(MULT)
        F()
        T_()
    elif(token.type == DIV):
        match(DIV)
        F()
        T_()

def F():
    print("Ativação de F()")
    global token
    if(token.type == LBRACKET):
        match(LBRACKET)
        E()
        match(RBRACKET)
    elif (token.type == ID):
        match(ID)
    elif(token.type == NUM):
        match(NUM)
    else:
        imprimeErro()

"""
Início da análise sintática de descida recursiva
"""
E()
