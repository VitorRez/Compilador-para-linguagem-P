import sys
import os
from Token import *
from lexical_analyzer import *
from syntax_analyzer import *

# Obter o nome do arquivo de entrada e remover a extensão
filename = sys.argv[1]
file_base_name = os.path.splitext(os.path.basename(filename))[0]

# Criar diretório "results" se ele não existir
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Nome do arquivo de saída dinâmico
output_file_path = os.path.join(output_dir, f'saida_{file_base_name}.txt')

# Redirecionar a saída padrão para o arquivo com codificação UTF-8
with open(output_file_path, 'w', encoding='utf-8') as saida:
    sys.stdout = saida

    TokenP = []
    TokenD = TokenDict()

    TokenP = LexicalAnalyzer(filename)

    for i in TokenP:
        if i.tokenind == 'Error':
            print('Erro léxico. ' + i.lexema)
            sys.exit()

    DescidaRecursiva = syntaxAnalyzer(TokenP)

    DescidaRecursiva.Programa()

    DescidaRecursiva.imprimeArvores()

    DescidaRecursiva.imprimeTabelas()

    # Restaurar a saída padrão
    sys.stdout = sys.__stdout__