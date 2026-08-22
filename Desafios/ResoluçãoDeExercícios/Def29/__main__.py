from def29 import Diario
from rich import print
from rich import inspect

def main():
    d = Diario()
    d.escrever ="Consegui fazer o exercício"
    d.escrever ="Sigo estudando Python"
    
    try:
        d.ler('CeV!@')
    except Exception as e:
        print(f"ERRO: {e}")
    inspect(d, private=True)

    print(d._Diario__segredos)
if __name__ == '__main__':  
    main()  