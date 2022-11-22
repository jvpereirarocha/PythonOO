from abc import ABC, abstractmethod
import enum
from typing import Set, Type

class Produto(ABC):
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
        self._produtos = set()

    def _adicionar(self):
        novo_produto = self.adicionar()
        self._produtos.add(novo_produto)
    
    @abstractmethod
    def adicionar(self) -> Type["Produto"]:
        raise NotImplementedError

    def obter_produtos(self) -> Set[Type["Produto"]]:
        return self._produtos

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.nome} - Preço: R${self.preco}"


class MedidaDoProduto(enum.Enum):
    PESO = "peso"
    UNIDADE = "unidade"


class Alimento(Produto):
    def __init__(self, nome, preco, unidade_ou_peso) -> None:
        super().__init__(nome, preco)
        self.unidade_ou_peso = unidade_ou_peso

    def adicionar(self) -> Type["Produto"]:
        return self


class Roupa(Produto):
    def __init__(self, nome, preco, codigo_ean) -> None:
        super().__init__(nome, preco)
        self.codigo = codigo_ean

    def adicionar(self) -> Type["Produto"]:
        return self


arroz = Alimento("Arroz", preco=15.0, unidade_ou_peso=MedidaDoProduto.PESO.value)
camisa = Roupa("Camisa Polo", preco=199.90, codigo_ean="152365")

arroz.adicionar()
camisa.adicionar()

lista_de_produtos = list(arroz.obter_produtos()) + list(camisa.obter_produtos())

for produto in lista_de_produtos:
    print(produto)


from collections.abc import Sized

class MinhaLista(Sized):
    def __init__(self, descricao) -> None:
        self.descricao = descricao

    def __str__(self) -> str:
        return self.descricao


minha_lista = MinhaLista("Nova Lista")
print(minha_lista)