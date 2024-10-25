from maratona import *

if __name__ == "__main__":
    R1 = Corredor("Usain Bolt", 38, 86.2)
    print(R1)
    print(R1.aquecer())
    print(R1.correr())

    N1 = Nadador("Michael Phelps", 39, 88.2)
    print(N1)
    print(N1.aquecer())
    print(N1.nadar())

    C1 = Ciclista("Thiago Ferauche", 45, 97.2)
    print(C1)
    print(C1.aquecer())
    print(C1.pedalar())