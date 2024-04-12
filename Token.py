class Token:

    def __init__(self, tokenind, lexema, num_linha):
        self.tokenind = tokenind
        self.lexema = lexema
        self.num_linha = num_linha

class TokenPile:

    def __init__(self):
        self.pile = []

    def addToPile(self, token):
        self.pile.append(token)

class TokenDict:

    def __init__(self):
        self.d = {
            '{' : ['Punctuation', 'LBrace'],
            '}' : ['Punctuation', 'RBrace'],
            '(' : ['Punctuation', 'LParen'],
            ')' : ['Punctuation', 'RParen'],
            ',' : ['Punctuation', 'Comma'],
            ';' : ['Punctuation', 'Semicolon'],
            ':' : ['Punctuation', 'Colon'],
            '=' : ['Operators', 'Assign'],
            '!' : ['Operators', 'Exclamation'],
            '<' : ['Operators', 'LessThan'],
            '>' : ['Operators', 'GreaterThan'],
            '+' : ['Operators', 'Plus'],
            '-' : ['Operators', 'Minus'],
            '*' : ['Operators', 'Multiplication'],
            '/' : ['Operators', 'Division'],
            'fn' : ['ReservedWords', 'Function'],
            'char' : ['ReservedWords', 'Char'],
            'int' : ['ReservedWords', 'Int'],
            'float' : ['ReservedWords', 'Float'],
            'if' : ['ReservedWords', 'If'],
            'else' : ['ReservedWords', 'Else'],
            'return' : ['ReservedWords', 'Return'],
            'let' : ['ReservedWords', 'Let'],
            'println' : ['ReservedWords', 'Println'],
            'print' : ['ReservedWords', 'Print'],
            'main' : ['ReservedWords', 'Main'],
            'while' : ['ReservedWords', 'While']
        }