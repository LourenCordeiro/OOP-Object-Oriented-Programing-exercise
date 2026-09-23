from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float):
        if salario < 0:
            raise ValueError("Salário não pode ser negativo")
        self.nome = nome
        self._salario = salario

    @property
    def salario(self) -> float:
        return self._salario

    @abstractmethod
    def calcular_bonus(self):
        pass
    
    def __str__(self) -> str:
        cargo = type(self).__name__
        return (f"{self.nome} ganha R${self._salario:,.2f} e por ser {cargo} o bônus será de R${self.calcular_bonus():,.2f}")

class Gerente(Funcionario):
    PERCENTUAL_BONUS = 0.15

    def calcular_bonus(self):
        return self._salario * self.PERCENTUAL_BONUS


class Designer(Funcionario):
    PERCENTUAL_BONUS = 0.8

    def calcular_bonus(self):
        return self._salario * self.PERCENTUAL_BONUS

class Desenvolvedor(Funcionario):
    PERCENTUAL_BONUS = 0.10
    
    def calcular_bonus(self):
        return self._salario * self.PERCENTUAL_BONUS
    

##O CÓDIGO DA CORREÇÃO DO PROFESSOR TROUXE ALGUMAS ABORDAGENS DIFERENTE
#-usou o setter para validar o reajuste de redução ou aumento
#-usou "self.__class__.name" para trazer o nome do cargo
#-Não utilizou um atributo de classe para cálculo no bônus fez direto no método.

class Funcionaio(ABC):
    def __init__(self, nome:str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario

    @abstractmethod             #será calcilado nas filhas
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float = None):
        if valor is None:
            raise ValueError("Impossível reajustar o salário desse jeito")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Você não pode reduzir o salário de um funcionário.")

    def __str__(self):
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.name__} o bônus será de R${self.calcular_bonus():,.2f}"

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15
