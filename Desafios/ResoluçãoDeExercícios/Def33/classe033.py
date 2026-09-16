from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None     
        self.nascimento = nasc      #atributo validavél

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento (self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade (self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")



class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]       #Atributo de classe

    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso


    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError (f"O curso {curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        ##Nesse exercício o prof fez o desafio de incluir uma condição caso o curso adicionado já estivesse na lista oficial, então adpatei o primeiro If para If not e depois o IF IN na lista oficial
        if not (3 <= len(curso) <= 5):
            raise ValueError(f"Nome {curso} está fora do padão para Cursos!")
        if curso in Aluno.cursos_oficiais:
            raise ValueError(f"O {curso} já está na lista oficial!")
        Aluno.curso_oficiais.append(curso)


