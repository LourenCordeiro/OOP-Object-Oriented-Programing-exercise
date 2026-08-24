from def29 import Diario
from rich import print
from rich import inspect

def main():
    d = Diario()
    d.escrever("Consegui fazer o exercício")
    d.escrever("Sigo estudando Python")
    
    try:
        d.ler('CeV!@')
    except PermissionError as e:
        print(f"ERRO: {e}")
    #inspect(d, private=True)
    #print(d._Diario__segredos)
    d.trocar_senha('CeV!@', 'NovaSenhaForte')  # troca usando a senha atual
    d.ler('NovaSenhaForte')                    # funciona com a nova
    d.ler('CeV!@')                              # agora a antiga dá PermissionError


if __name__ == '__main__':  
    main()  