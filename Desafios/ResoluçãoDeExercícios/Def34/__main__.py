from desafio34 import *

def main():
    f = Desenvolvedor("Louren", 28_000)
    print(f)

    funcionarios = [
        Desenvolvedor("Pedro", 18_000), Designer("José", 25_000), Gerente("Mariana", 45_000)
    ]

    for f in funcionarios:
        print(f)


if __name__=="__main__":
    main()