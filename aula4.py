"""
Cria uma classe de playlist de programas para utilizar outras técnicas quando herança não é vantajoso
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


# não recomendado herdar de list
# class Playlist(list):
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

#     def tamanho(self):
#         return len(self.programas)

class Playlist:
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    @property
    def tamanho(self) -> int:
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


bastardos_inglorios = Filme("Bastardos Inglórios", 1999, 120)
titanic = Filme("Titanic", 1990, 90)
peaky_blinders = Serie("Peaky Blinders", 2013, 5)
breaking_bad = Serie("Breaking Bad", 2013, 5)


programas = [bastardos_inglorios, titanic, peaky_blinders, breaking_bad]

playlist = Playlist("Maratonar", programas)

# não é uma boa prática, precisa conhecer detalhes da classe playlist
for programa in playlist.listagem:
    print(programa)

# existe uma forma de obter através do len() utilizando um método duck_typing
print(f"tamanho: {playlist.tamanho}")