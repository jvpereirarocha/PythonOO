"""
Criação de uma lista de programas de TV usando o conceito de polimorfismo
"""
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0
        self._deslikes = 0

    @property
    def nome(self):
        return self._nome.title()

    @property
    def likes(self):
        return self._likes

    @property
    def deslikes(self):
        return self._deslikes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def gostei(self):
        self._likes += 1

    def nao_gostei(self):
        self._deslikes += 1

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Deslikes: {self.deslikes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{super().__str__()} - duracao: {self.duracao} minutos"


class Serie(Programa):
    def __init__(self, nome, ano, quantidade_de_temporadas):
        super().__init__(nome, ano)
        self.quantidade_de_temporadas = quantidade_de_temporadas

    def __str__(self):
        return f"{super().__str__()} - temporadas: {self.quantidade_de_temporadas}"


filme = Filme("Bastardos Inglórios", 1999, 120)
serie = Serie("Peaky Blinders", 2013, 5)

programas = [filme, serie]

for programa in programas:
    print(programa)