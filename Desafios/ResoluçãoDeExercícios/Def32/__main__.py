from classe032 import *


def main():
    cc = ContaBancaria (111, "Josenildo", 10_000, "Guanabara")

    print("Vou tentar sacar...")
    cc.sacar(500)

    print("Tentando mudar o nome...")
    cc.nome = "Maricota"

    print(cc)
    

if __name__ == "__main__":
    main()