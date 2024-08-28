class Token:

    def __init__(self, tokenind, lexema, num_linha):
        self.tokenind = tokenind
        self.lexema = lexema
        self.num_linha = num_linha

class TokenDict:

    def __init__(self):
        self.d = {
            '{' : ['LBrace', '{'],
            '}' : ['RBrace', '}'],
            '(' : ['LParen', '('],
            ')' : ['RParen', ')'],
            ',' : ['Comma', ','],
            ';' : ['Semicolon', ';'],
            ':' : ['Colon', ':'],
            '=' : ['Assign', '='],
            '!' : ['Exclamation', '!'],
            '<' : ['LessThan', '<'],
            '>' : ['GreaterThan', '>'],
            '+' : ['Plus', '+'],
            '-' : ['Minus', '-'],
            '*' : ['Multiplication', '*'],
            '/' : ['Division', '/'],
            'fn' : ['Function', 'fn'],
            'char' : ['Char', 'char'],
            'int' : ['Int', 'int'],
            'float' : ['Float', 'float'],
            'if' : ['If', 'if'],
            'else' : ['Else', 'else'],
            'return' : ['Return', 'eeturn'],
            'let' : ['Let', 'let'],
            'println' : ['Println', 'println'],
            'print' : ['Print', 'print'],
            'main' : ['Main', 'main'],
            'while' : ['While', 'while']
        }