from Token import *

def LexicalAnalyzer(filename):

    TD = TokenDict()
    TokenP = TokenPile()

    selfLoop = ["{","}","(",")",",",";",":","+","*","/"]
    knownCharacters = ["{","}","(",")",",",";",":","+","-","*","/","=","!",">","<","."," ","\n",'"',"'"]

    lineNum = 1

    with open(filename, 'r') as file:

        for line in file.readlines():

            index = 0

            while index < len(line):

                if line[index] in selfLoop:
                    token = Token(TD.d[line[index]][0], TD.d[line[index]][1], lineNum)
                    TokenP.addToPile(token)

                if line[index] not in knownCharacters and not line[index].isalpha() and not line[index].isnumeric():
                    token = Token('Error', "Unknown char " + line[index], lineNum)
                    TokenP.addToPile(token)

                if line[index] == '=':
                    if line[index+1] == '=':
                        token = Token('Equal', '==', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Assign', '=', lineNum)
                        TokenP.addToPile(token)

                if line[index] == '!':
                    if line[index+1] == '=':
                        token = Token('NotEqual', '!=', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Error', 'Unknown char !', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '<':
                    if line[index+1] == '=':
                        token = Token('LessThanEqual', '<=', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('LessThan', '<', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '>':
                    if line[index+1] == '=':
                        token = Token('GreaterThanEqual', '>=', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('GreaterThan', '>', lineNum)
                        TokenP.addToPile(token)
                
                if line[index] == '-':
                    if line[index+1] == '>':
                        token = Token('Arrow', '->', lineNum)
                        TokenP.addToPile(token)
                        index += 1
                    else:
                        token = Token('Minus', '-', lineNum)
                        TokenP.addToPile(token)

                if line[index].isalpha():
                    aux = ""
                    while (line[index].isalpha() or line[index].isnumeric()) and index < len(line) and line[index] != ' ':
                        aux += line[index]
                        index += 1
                    token = Token('ID', str(aux), lineNum)
                    if aux == 'fn':
                        token = Token('Function', 'fn', lineNum)
                    if aux == 'let':
                        token = Token('Let', 'let', lineNum)
                    if aux == 'println':
                        token = Token('Println', 'println', lineNum)
                    if aux == 'print':
                        token = Token('Print', 'print', lineNum)
                    if aux == 'main':
                        token = Token('Main', 'main', lineNum)
                    if aux == 'return':
                        token = Token('Return', 'return', lineNum)
                    if aux == 'char':
                        token = Token('Char', 'char', lineNum)
                    if aux == 'int':
                        token = Token('Int', 'int', lineNum)
                    if aux == 'float':
                        token = Token('Float', 'float', lineNum)
                    if aux == 'if':
                        token = Token('If', 'if', lineNum)
                    if aux == 'else':
                        token = Token('Else', 'else', lineNum)
                    if aux == 'while':
                        token = Token('While', 'while', lineNum)
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

                if line[index] == "'":
                    aux = ""
                    index += 1
                    while index < len(line) and line[index] != "'":
                        aux += line[index]
                        index += 1
                    #print(aux)
                    token = Token('CharConst', aux, lineNum)
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
        #if(p.tokenind == "Error"):
        print(p.tokenind, p.lexema, p.num_linha)
    
    return TokenP
                

LexicalAnalyzer("tests/calculadora.p")