import sys
import os
from core import executar_codigo

def main():
    print("🔥 Pyrus v0.0.0.0 | Pyrus-Labor Systems")
    
    if len(sys.argv) < 2:
        print("Utilize: python pyrus.py run <arquivo.pyu>")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "run":
        if len(sys.argv) < 3:
            print("Erro: Caminho do arquivo .pyu não especificado.")
            sys.exit(1)
            
        file_path = sys.argv[2]
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                executar_codigo(f.read())
        else:
            print(f"Erro: O arquivo '{file_path}' não existe.")
            
    elif cmd == "version":
        print("Pyrus Core v0.0.0.0-alpha")
    else:
        print(f"Comando '{cmd}' desconhecido.")

if __name__ == "__main__":
    main()
