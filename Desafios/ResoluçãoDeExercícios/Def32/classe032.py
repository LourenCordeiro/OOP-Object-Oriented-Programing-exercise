from hashlib import sha256


class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, ID:int, nome:str = None, saldo:float =0, chave:str = None):
        self._ID = ID            #protegido (#)
        self._titular = nome       #protected (#)
        self.__saldo = saldo        #private (-)
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._ID} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")


    def pede_senha(self) -> str:
        from pwinput import pwinput   #importa apenas para uso nessa função

        while True:
            senha = str(pwinput("Senha: ")).strip()     #função interna pwinput "esconde" com * o que está sendo digitado
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True

        else:
            return False


    def __str__(self):
        return f"A conta {self._ID} de {self._titular} tem R${self.__saldo:.2f} de saldo."
     #   return f"Estado atual da conta: {self.__dict__}"

    def depositar (self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta {self._ID} ")


    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._ID}: SALDO INSUFICIENTE")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} autorizado na conta {self._ID} ")
        else:
            print("Senha não confere. Saque não autorizado!")

    
    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
        else:
            print("Senha nã confere. Não posso alterar o nome")
