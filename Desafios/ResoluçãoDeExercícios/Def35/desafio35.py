from abc import ABC, abstractmethod

class Arquivo(ABC):

    def __init__(self, nome:str, ext:str, tam:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext

    @abstractmethod
    def abrir(Self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("O arquivo está em um formato não supotado")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1_000_000}MB)"


class PDF(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'pdf', tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")


class DOC(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Michosoft Word")

#DUCK TYPING
def abrir_arquivo(arquivo):
    arquivo.abrir()