import sys
from lark import Lark, Tree

# Gramática Pyrus v0.1.2 - Híbrida (Python + Lua)
# Removemos a obrigatoriedade de ';' e '{ }'
pyrus_grammar = """
?start: program
program: stmt*

?stmt: assign | print_stmt | if_stmt | comment

// Blocos Híbridos: Aceita Lua (then..end), C ({..}) ou Python-like (:..end)
block: "{" stmt* "}" 
     | "then" stmt* "end" 
     | ":" stmt* "end"

if_stmt: "if" condition block ["else" block]

// Variáveis podem ser declaradas com 'var', 'local' ou diretamente 'x = 10'
assign: ["var" | "local"] CNAME "=" expr [";"]

print_stmt: "print" "(" expr ")" [";"]

// Comentários: Python (#), Lua (--) ou C (//)
comment: "#" /.*/ | "--" /.*/ | "//" /.*/

?condition: expr "==" expr -> eq
          | expr "!=" expr -> ne
          | expr ">"  expr -> gt
          | expr "<"  expr -> lt
          | "(" condition ")"

?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub

?term: factor
     | term "*" factor -> mul
     | term "/" factor -> div

?factor: NUMBER         -> number
       | ESCAPED_STRING -> string
       | CNAME          -> var_ref
       | "(" expr ")"

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""

class PyrusInterpreter:
    def __init__(self):
        self.env = {}

    def run(self, tree):
        if isinstance(tree, Tree):
            method = getattr(self, tree.data, self.generic_visit)
            return method(tree)
        return tree

    def generic_visit(self, tree):
        for child in tree.children:
            self.run(child)

    def program(self, tree):
        for child in tree.children:
            self.run(child)

    def assign(self, tree):
        # Lida com declarações opcionais de 'var' ou 'local'
        name_node = tree.children[0] if len(tree.children) == 2 else tree.children[1]
        val_node = tree.children[1] if len(tree.children) == 2 else tree.children[2]
        
        name = str(name_node)
        value = self.run(val_node)
        self.env[name] = value

    def var_ref(self, tree):
        name = str(tree.children[0])
        if name in self.env:
            return self.env[name]
        raise NameError(f"Erro: Variável '{name}' não definida.")

    def print_stmt(self, tree):
        value = self.run(tree.children[0])
        print(f"[Pyrus] {value}")

    def if_stmt(self, tree):
        cond_tree = tree.children[0]
        if_block = tree.children[1]
        else_block = tree.children[2] if len(tree.children) > 2 else None

        if self.run(cond_tree):
            self.run(if_block)
        elif else_block:
            self.run(else_block)

    def block(self, tree):
        for stmt in tree.children:
            self.run(stmt)

    # Matemática e Lógica
    def eq(self, tree): return self.run(tree.children[0]) == self.run(tree.children[1])
    def ne(self, tree): return self.run(tree.children[0]) != self.run(tree.children[1])
    def gt(self, tree): return self.run(tree.children[0]) > self.run(tree.children[1])
    def lt(self, tree): return self.run(tree.children[0]) < self.run(tree.children[1])
    def add(self, tree): return self.run(tree.children[0]) + self.run(tree.children[1])
    def sub(self, tree): return self.run(tree.children[0]) - self.run(tree.children[1])
    def mul(self, tree): return self.run(tree.children[0]) * self.run(tree.children[1])
    def div(self, tree): return self.run(tree.children[0]) / self.run(tree.children[1])

    def number(self, tree):
        val = tree.children[0]
        return float(val) if '.' in val else int(val)

    def string(self, tree):
        return str(tree.children[0])[1:-1]

    def comment(self, tree): pass

pyrus_parser = Lark(pyrus_grammar, start='program', parser='lalr')

def executar(codigo):
    try:
        ast = pyrus_parser.parse(codigo)
        interpreter = PyrusInterpreter()
        interpreter.run(ast)
    except Exception as e:
        print(f"❌ Erro de Sintaxe/Execução:\n{e}")
              
