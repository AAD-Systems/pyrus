import sys
from lark import Lark, Tree

# Gramática Pyrus v0.2.1 - Estabilidade de Blocos e Precedência
pyrus_grammar = """
?start: program
program: stmt*

?stmt: var_decl | print_stmt | if_stmt | block | comment

block: "{" stmt* "}"
if_stmt: "if" "(" condition ")" block ["else" block]
var_decl: "var" CNAME "=" expr ";"
print_stmt: "print" "(" expr ")" ";"
comment: "//" /.*/

?condition: expr "==" expr -> eq
          | expr "!=" expr -> ne
          | expr ">" expr  -> gt
          | expr "<" expr  -> lt

# Precedência: expr (soma) -> term (mult) -> factor (base)
?expr: term
     | expr "+" term   -> add
     | expr "-" term   -> sub

?term: factor
     | term "*" factor -> mul
     | term "/" factor -> div

?factor: NUMBER        -> number
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

    def var_decl(self, tree):
        name = str(tree.children[0])
        value = self.run(tree.children[1])
        self.env[name] = value

    def var_ref(self, tree):
        name = str(tree.children[0])
        if name in self.env:
            return self.env[name]
        raise NameError(f"Erro: Variável '{name}' não definida.")

    def print_stmt(self, tree):
        value = self.run(tree.children[0])
        print(f"[Pyrus Out] -> {value}")

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

    # Comparadores
    def eq(self, tree): return self.run(tree.children[0]) == self.run(tree.children[1])
    def ne(self, tree): return self.run(tree.children[0]) != self.run(tree.children[1])
    def gt(self, tree): return self.run(tree.children[0]) > self.run(tree.children[1])
    def lt(self, tree): return self.run(tree.children[0]) < self.run(tree.children[1])

    # Matemática
    def add(self, tree): return self.run(tree.children[0]) + self.run(tree.children[1])
    def sub(self, tree): return self.run(tree.children[0]) - self.run(tree.children[1])
    def mul(self, tree): return self.run(tree.children[0]) * self.run(tree.children[1])
    def div(self, tree): return self.run(tree.children[0]) / self.run(tree.children[1])

    # Tipos
    def number(self, tree):
        val = tree.children[0]
        return float(val) if '.' in val else int(val)

    def string(self, tree):
        return str(tree.children[0])[1:-1]

    def comment(self, tree): pass

# Setup do Parser
pyrus_parser = Lark(pyrus_grammar, start='program', parser='lalr')

def executar(codigo):
    try:
        ast = pyrus_parser.parse(codigo)
        interpreter = PyrusInterpreter()
        interpreter.run(ast)
    except Exception as e:
        print(f"❌ Erro Pyrus:\n{e}")

# --- TESTE DA LÓGICA ---
meu_codigo = """
var x = 10;
var limite = 5;

if (x > limite) {
    print("X e maior que o limite!");
    var calculo = (x + 2) * 10;
    print(calculo);
} else {
    print("X e menor.");
}
"""

executar(meu_codigo)
