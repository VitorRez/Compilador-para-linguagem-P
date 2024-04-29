from lexical_analyzer import *
from syntax_analyzer import *
from Token import *

TokenP = []
TokenD = TokenDict()

TokenP = LexicalAnalyzer("tests/fibonacci.p")

DescidaRecursiva = syntaxAnalyzer(TokenP)

DescidaRecursiva.Programa()
