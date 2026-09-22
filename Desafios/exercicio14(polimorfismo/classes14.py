from functools import singledispatchmethod          #Com essa função interna só consegue verificar um parâmetro por vcs
#Para acessar mais de um parâmetro por vocês o comando é multipledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possível analisar o valor {valor}")

    @analisar.register
    def _(self, valor:int):
        print(f"{valor} é um número Inteiro")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um número com ponto flutuantes (Real)")

    @analisar.register
    def _(self, valor: str):
        print(f"'{valor}' é uma cadeia de caracteres")

    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} é uma coleção de dados")
