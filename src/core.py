import sys
from lark import Lark, Transformer

# Gramática base da Pyrus (EBNF)
pyrus_grammar = """
?start: program
program: stmt*
?stmt: var_decl | print_stmt
var_decl: "var" CNAME "=" ESCAPED_STRING ";"
print_stmt: "print" "(" CNAME ")" ";"

%import common.CNAME
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""

parser = Lark(pyrus_grammar, start='program', parser='lalr')

class PyrusEvaluator(Transformer):
    def __init__(self):
        self.env = {} # Memória volátil da linguagem

    def var_decl(self, args):
        name = str(args[0])
        value = str(args[1])[1:-1] # Limpeza das aspas
        self.env[name] = value

    def print_stmt(self, args):
        name = str(args[0])
        if name in self.env:
            print(f"[Pyrus Log] -> {self.env[name]}")
        else:
            print(f"❌ Erro de Execução: Variável '{name}' não foi declarada.")

def executar_codigo(codigo_fonte):
    try:
        tree = parser.parse(codigo_fonte)
        PyrusEvaluator().transform(tree)
    except Exception as e:
        print(f"⚠️ Erro de Sintaxe Pyrus:\n{e}")
  
