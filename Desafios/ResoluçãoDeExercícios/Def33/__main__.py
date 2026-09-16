from classe033 import *

def main():
    a = Aluno("Marcia", 2010, "ADM")
    b = Aluno("Pedro", 2015, "ENG")

    a.add_curso("ADS")

    print(b.cursos_oficiais)
    print(a.__dict__)

if __name__ == "__main__":
    main()