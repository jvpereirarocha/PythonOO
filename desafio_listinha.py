class Listinha:
    def __init__(self, itens) -> None:
        self.itens = itens

    def __iter__(self):
        return self.itens.__iter__()


meu_objeto = Listinha([1, 2, 4])

contador = 0

for item in meu_objeto:
    contador += 1

# acontecerá um erro de execução pois a classe Listinha não possui o magic method __len__
print(contador == len(meu_objeto))