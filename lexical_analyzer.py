from Token import *

def LexicalAnalyzer(filename):

    TD = TokenDict()
    TokenP = TokenPile()

    selfLoop = ["{","}","[","]","(",")",",",";",":","+","*","/"]

    lineNum = 0

    with open(filename, 'r') as file:

        for line in file.readlines():

            index = 0

            while index < len(line):

                if line[index] in selfLoop:
                    token = Token(TD.d[line[index]][0], TD.d[line[index]][1], lineNum)
                    TokenP.addToPile(token)

                if line[index] == '=':
                    if line[index+1] == '=':
                        token = Token('Operators', 'Equal', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Operators', 'Assign', lineNum)
                        TokenP.addToPile(token)

                if line[index] == '!':
                    if line[index+1] == '=':
                        token = Token('Operators', 'NotEqual', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Error', 'Não sei ;-;', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '<':
                    if line[index+1] == '=':
                        token = Token('Operators', 'LessThanEqual', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Operators', 'LessThan', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '>':
                    if line[index+1] == '=':
                        token = Token('Operators', 'GreaterThanEqual', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Operators', 'GreaterThan', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '-':
                    if line[index+1] == '>':
                        token = Token('Operators', 'Arrow', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Operators', 'Minus', lineNum)
                        TokenP.addToPile(token)

                if line[index].isalpha():
                    aux = ""
                    while (line[index].isalpha() or line[index].isnumeric()) and index < len(line) and line[index] != ' ':
                        aux += line[index]
                        index += 1
                    token = Token('Identifier', str(aux), lineNum)
                    if aux == 'fn':
                        token = Token('ReservedWords', 'Function', lineNum)
                    if aux == 'let':
                        token = Token('ReservedWords', 'Let', lineNum)
                    if aux == 'println':
                        token = Token('ReservedWords', 'Println', lineNum)
                    if aux == 'print':
                        token = Token('ReservedWords', 'Print', lineNum)
                    if aux == 'main':
                        token = Token('ReservedWords', 'Main', lineNum)
                    if aux == 'return':
                        token = Token('ReservedWords', 'Return', lineNum)
                    if aux == 'char':
                        token = Token('ReservedWords', 'Char', lineNum)
                    if aux == 'int':
                        token = Token('ReservedWords', 'Int', lineNum)
                    if aux == 'float':
                        token = Token('ReservedWords', 'Float', lineNum)
                    if aux == 'if':
                        token = Token('ReservedWords', 'If', lineNum)
                    if aux == 'else':
                        token = Token('ReservedWords', 'Else', lineNum)
                    if aux == 'while':
                        token = Token('ReservedWords', 'While', lineNum)
                    TokenP.addToPile(token)
                    index -= 1

                if line[index] == '"':
                    aux = ""
                    index += 1
                    while index < len(line) and line[index] != '"':
                        aux += line[index]
                        index += 1
                    token = Token('CharConst', aux, lineNum)
                    if aux == '{'+'}':
                        token = Token('FormattedString', '{'+'}', lineNum)
                    TokenP.addToPile(token)
                
                if line[index].isnumeric():
                    aux = ""
                    f = 0
                    while (line[index].isnumeric() or line[index] == '.') and index < len(line) and line[index] != ' ':
                        aux += line[index]
                        if line[index] == '.':
                            f = 1
                        index += 1
                    if f == 0:
                        token = Token('IntConst', str(aux), lineNum)
                    else:
                        token = Token('FloatConst', str(aux), lineNum)
                    TokenP.addToPile(token)
                    index -= 1
                     

                index += 1

            lineNum += 1
        
    
    for p in TokenP.pile:
        print(p.tokenind, p.lexema, p.num_linha)
                

LexicalAnalyzer("tests/calculadora.p")