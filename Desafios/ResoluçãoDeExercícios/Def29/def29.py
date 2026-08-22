from rich import print

class Diario:

    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

  
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__Diario.segredos.append(msg.strip())


    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        else:
            print(f"Diário LIBERADO!")
            for segredo in self.__segredos:
                print(f" - {segredo}")

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver sem a senha")

    @senha.setter
    def senha(self, novasenha):
        pass