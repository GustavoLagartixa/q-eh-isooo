from q_eh_isso import *

if __name__ == "__main__":
    R1 = Corredor("Usain Bolt", 38, 86.2)
    print(R1)
    print(R1.aquecer())
    print(R1.correr())

    N1 = Nadador("Michael Phelps", 39, 88.2)
    print(N1)
    print(N1.aquecer())
    print(N1.nadar())

    C1 = Ciclista("Thiago Ferrauch", 45, 97.2)
    print(C1)
    print(C1.aquecer())
    print(C1.pedalar())

    T1 = Triatleta("Joaquim Malacarne", 19, 75)
    print(T1)
    print(T1.aquecer())
    print(T1.realizar_maratona())

