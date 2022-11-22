"""
relembrando orientação a objetos:
    - criando properties
    - criando comportamentos encapsulados
    - adicionando atributos e métodos
"""

class Filme:
    def __init__(self, nome, ano, duracao) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
        self.__deslike = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

    def deslike(self):
        self.__deslike += 1


class Serie:
    def __init__(self, nome, ano, temporadas) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
        self.__deslike = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

    def deslike(self):
        self.__deslike += 1