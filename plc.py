import sys
from Token import *
from lexical_analyzer import *
from syntax_analyzer import *

filename = sys.argv[1]
TokenP = []
TokenD = TokenDict()

TokenP = LexicalAnalyzer(filename)
for i in TokenP:
    if i.tokenind == 'Error':
        print('Erro léxico. ' + i.lexema)
        sys.exit()

DescidaRecursiva = syntaxAnalyzer(TokenP)

DescidaRecursiva.Programa()

DescidaRecursiva.imprimeTabelas()