from lexical_analyzer import *
from syntax_analyzer import *
from Token import *

TokenP = []
TokenD = TokenDict()

TokenP = LexicalAnalyzer("tests/media.p")

DescidaRecursiva = syntaxAnalyzer(TokenP)

DescidaRecursiva.Programa()
