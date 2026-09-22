from rich import print

class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome


    def fazer_pudim(self):
        print(f"{self.nome} faz [blue]pudim[/] com leite condensado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita [red]coxinha[/] no óleo de soja")


class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz [blue]pudim[/] com leite ninho e nutella")


class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} fritar [red]coxinha[/] na air freyer")