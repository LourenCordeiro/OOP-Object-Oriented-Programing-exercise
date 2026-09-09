from Def30 import Credencial

def main():
    c = Credencial()
    c.enha = str(input('Digite a senha: '))
    print(c.senha)


    c.valida('CeV!@')

if __name__ == '__main__':
    main()