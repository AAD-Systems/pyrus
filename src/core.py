import sys
from lark import Lark, Transformer, v_args

# Gramática Pyrus v0.2 - Suporte a Blocos Lógicos, If/Else e Comparações
pyrus_grammar = """
?start: program
program: stmt*

?stmt: var_decl | print_stmt | comment | if_stmt | block

# Blocos de código permitem agrupar comandos dentro de { }
block: "{" stmt* "}"

# Definição do If/Else: O 'else' é opcional (?)
if_stmt: "if" "(" condition ")" block ["else" block]

var_decl: "var" CNAME "=" expr ";"
print_stmt: "print" "(" expr ")" ";"
comment: "//" /.*/

# Condições lógicas para o IF
?condition: expr "==" expr -> eq
          | expr "!=" expr -> ne
          | expr ">" expr  -> gt
          | expr "<" expr  -> lt

# Matemática e Expressões (Mantendo v0.1)
?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub
     | expr "*" term   -> mul
     | expr "/" term   -> div

?term: NUMBER          -> number
     | ESCAPED_STRING  -> string
     | CNAME           -> var_ref

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""

class PyrusEvaluator(Transformer):
    def __init__(self):
        self.env = {} # Dicionário que serve como memória (RAM) da linguagem

    # --- GERENCIAMENTO DE VARIÁVEIS ---
    def var_decl(self, args):
        name, value = args
        self.env[str(name)] = value
        return value

    def var_ref(self, name):
        name = str(name[0])
        if name in self.env:
            return self.env[name]
        raise NameError(f"Erro: Variável '{name}' não definida.")

    # --- SAÍDA ---
    def print_stmt(self, args):
        value = args[0]
        print(f"[Pyrus Out] -> {value}")

    # --- LÓGICA DE DECISÃO (O coração da v0.2) ---
    def if_stmt(self, args):
        condition, if_block = args[0], args[1]
        else_block = args[2] if len(args) > 2 else None

        # Se a condição for verdadeira, executa o primeiro bloco
        if condition:
            return if_block
        # Se houver um 'else' e a condição for falsa, executa o segundo
        elif else_block:
            return else_block

    # Transforma o conteúdo do bloco em uma lista de comandos executáveis
    def block(self, args):
        return args

    # --- COMPARADORES ---
    def eq(self, args): return args[0] == args[1]
    def ne(self, args): return args[0] != args[1]
    def gt(self, args): return args[0] > args[1]
    def lt(self, args): return args[0] < args[1]

    # --- TIPOS DE DADOS ---
    def number(self, n):
        return float(n[0]) if '.' in n[0] else int(n[0])

    def string(self, s):
        return str(s[0])[1:-1]

    # --- OPERAÇÕES MATEMÁTICAS ---
    def add(self, args): return args[0] + args[1]
    def sub(self, args): return args[0] - args[1]
    def mul(self, args): return args[0] * args[1]
    def div(self, args): return args[0] / args[1]
    
    def comment(self, args): pass

# Usamos o parser LALR para garantir velocidade e evitar ambiguidades
parser = Lark(pyrus_grammar, start='program', parser='lalr', transformer=PyrusEvaluator())

def executar_codigo(codigo_fonte):
    try:
        # Na v0.2, o transformer já está integrado no parser para execução imediata
        parser.parse(codigo_fonte)
    except Exception as e:
        print(f"❌ Erro Pyrus v0.2:\n{e}")
