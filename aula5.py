"""
Utiliza os metodos duck typing do python para estabelecer comportamentos semelhantes a estruturas built-in
"""

from itertools import chain


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


class Playlist:
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    def __len__(self):
        contador = 0
        for _ in self._programas:
            contador += 1
        
        return contador

    # utilizado para criar um iteravel
    def __getitem__(self, item):
        return self._programas[item]

    # utilizado para setar os atributos dentro no iteravel caso necessário
    def __setitem__(self, indice, novo_item):
        self._programas[indice] = novo_item

    def __add__(self, iter):
        return chain.from_iterable([self._programas, iter])



bastardos_inglorios = Filme("Bastardos Inglórios", 1999, 120)
titanic = Filme("Titanic", 1990, 90)
peaky_blinders = Serie("Peaky Blinders", 2013, 5)
breaking_bad = Serie("Breaking Bad", 2013, 5)
two_and_a_half_men = Serie("Two and A Half Men", 2000, 10)

programas = [bastardos_inglorios, titanic, peaky_blinders, breaking_bad, two_and_a_half_men]

playlist = Playlist("Maratonar", programas)
opcional = Playlist("Opcional", programas)

for programa in playlist:
    print(f"programa atual: {programa}")

print(f"tamanho da playlist: {len(playlist)}")
playlist[0] = Serie("teste", 2015, 1)
for programa in playlist:
    print(f"programa atual apos atualizar: {programa}")

print(f"\n\n")
result = playlist + opcional
for r in result:
    print(f"r: {r}")