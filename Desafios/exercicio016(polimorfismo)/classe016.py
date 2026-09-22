class Porta():
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação solicitada")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separe as partes sobre uma figideira")

class Pedra:
    pass

#MÉTODO PYTHONICO POLIMORFICO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas a tentar abrir o objeto tipo {objeto.__class__.__name__}")

