from rich import print

class Diario:

    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

  
    def escrever(self, msg):
        if not isinstance(msg, str) or len(msg.strip()) == 0:
            raise ValueError("[blue]A mensagem precisa ser um texto não vazio.[/]")
        self.__segredos.append(msg.strip())


    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError(f"[red]Senha inválida! Você não pode ler meu diário![/]")
        else:
            print(f"Diário LIBERADO!")
            for segredo in self.__segredos:
                print(f" - {segredo}")

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            raise PermissionError("Senha atual incorreta! Não é possível trocar a senha.")
        if not isinstance(nova_senha, str) or len(nova_senha.strip()) == 0:
            raise ValueError("A nova senha precisa ser um texto não vazio.")
        self.__senha = nova_senha.strip()


    @property
    def senha(self):
        raise PermissionError(f"[red]Ninguém tem permissão de ver sem a senha[/]")

    @senha.setter
    def senha(self, nova_senha):
            raise PermissionError("Use o método trocar_senha(senha_atual, nova_senha).")

