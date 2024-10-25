from abc import ABC, abstractmethod, ABCMeta

class Atleta(ABC):
    nome : str
    idade : int
    peso : float

    def __init__(self, n: str, i: int, p: float):
        self.nome = n
        self.idade = i
        self.peso = p

    def aquecer(self):
        return "Aquecendo..."
    
    def __str__(self):
        info = f'nome: {self.nome}, '
        info += f'{self.idade} anos, '
        info += f'{self.peso} kg '
        return info
    
class Corredor(Atleta):
    def correr(self):
        return "correndo..."

class Nadador(Atleta):
    def nadar(self):
        return "nadando..."
    
class Ciclista(Atleta):
    def pedalar(self):
        return "pedalando..."
    
class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self):
        info = self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info