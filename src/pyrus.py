import sys
import os
from core import executar
from lexer import analisar_tokens

BANNER = "🔥 Pyrus Engine | v0.1.2 (Hybrid Lexer Update)"

def show_help():
    print(f"""{BANNER}
Uso: pyu [comando] <argumentos>

Comandos:
  run <arquivo.pyu>    Executa um script Pyrus.
  lex <arquivo.pyu>    Executa a Análise Léxica e exibe os Tokens.
  repl                 Inicia o console interativo Pyrus.
  version              Exibe a versão atual do motor.
  help                 Mostra esta mensagem de ajuda.
    """)

def start_repl():
    print(f"{BANNER}\nDigite 'exit' para sair.")
    while True:
        try:
            codigo = input("pyu> ")
            if codigo.strip().lower() == 'exit':
                break
            if codigo.strip():
                executar(codigo)
        except (KeyboardInterrupt, EOFError):
            print("\nSaindo...")
            break

def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "run":
        if len(sys.argv) < 3:
            print("❌ Erro: Especifique o caminho do arquivo .pyu")
            sys.exit(1)
        
        file_path = sys.argv[2]
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                executar(f.read())
        else:
            print(f"❌ Erro: O arquivo '{file_path}' não foi encontrado.")

    elif cmd == "lex":
        if len(sys.argv) < 3:
            print("❌ Erro: Especifique o caminho do arquivo .pyu")
            sys.exit(1)
            
        file_path = sys.argv[2]
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                analisar_tokens(f.read())
        else:
            print(f"❌ Erro: Arquivo não encontrado.")

    elif cmd == "repl":
        start_repl()

    elif cmd == "version":
        print(BANNER)
        print("Arquitetura: Híbrida (Python/Lua) | Parser: LALR com Lexer exposto")

    elif cmd == "help":
        show_help()

    else:
        print(f"❓ Comando '{cmd}' desconhecido. Use 'python pyrus.py help'.")

if __name__ == "__main__":
    main()
    
