from lark import Lark

# Gramática base para inicializar apenas o Lexer
from core import pyrus_grammar

# Inicializamos o parser configurado para expor a geração léxica
lex_engine = Lark(pyrus_grammar, start='program', parser='lalr', lexer='basic')

def analisar_tokens(codigo):
    """
    Transforma o código fonte bruto em uma fita de Tokens.
    Essa é a verdadeira Análise Léxica.
    """
    try:
        tokens = lex_engine.lex(codigo)
        print("🔍 [Análise Léxica] Fita de Tokens gerada:\n")
        print(f"{'TIPO':<20} | {'VALOR':<20} | {'LINHA, COLUNA'}")
        print("-" * 60)
        
        for token in tokens:
            print(f"{token.type:<20} | {repr(token.value):<20} | L:{token.line}, C:{token.column}")
            
        print("-" * 60)
        print("✅ Lexing concluído com sucesso.")
    except Exception as e:
        print(f"❌ Erro Léxico:\n{e}")
      
