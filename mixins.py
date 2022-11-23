from typing import List


class NomeFormatadoMixin:
    def formatar_nome(self):
        return f"O {self.__class__.__name__.lower()} {self.nome}"

class NotasMixin:
    def _calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def media_das_notas_de_aluno(self):
        return f"média: {self._calcular_media()}"


class CalculoDeSalarioMixin:
    def calcular_salario_por_dia(self) -> float:
        return self.horas_trabalhadas_por_dia * self.valor_hora_trabalho

    def calcular_salario_mensal(self) -> float:
        return self.calcular_salario_por_dia() * self.dias_trabalhados

class Pessoa(NomeFormatadoMixin):
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def __str__(self) -> str:
        return f"{self.formatar_nome()}"


class Aluno(Pessoa, NotasMixin):
    def __init__(self, nome, notas) -> None:
        super().__init__(nome)
        self.notas = notas

    def __str__(self) -> str:
        return f"{super().__str__()} teve {self.media_das_notas_de_aluno()}"


class Funcionario(Pessoa, CalculoDeSalarioMixin):
    def __init__(self, nome, valor_hora_trabalho: float = 10.0, horas_trabalhadas_por_dia: float = 8.0, dias_trabalhados: int = 22) -> None:
        super().__init__(nome)
        self.valor_hora_trabalho = valor_hora_trabalho
        self.horas_trabalhadas_por_dia = horas_trabalhadas_por_dia
        self.dias_trabalhados = dias_trabalhados

    def __str__(self) -> str:
        return f"{super().__str__()} recebeu R$ {self.calcular_salario_mensal()}"


class Empresa:
    def __init__(self, nome, funcionarios: List[Funcionario]) -> None:
        self.nome = nome
        self.funcionarios = funcionarios

    def calcular_despesas_da_empresa_mensais(self):
        valor_mensal = 0.0
        for funcionario in self.funcionarios:
            valor_mensal_por_funcionario = funcionario.calcular_salario_mensal()
            print(funcionario, end="\n")
            valor_mensal += valor_mensal_por_funcionario
        
        return round(valor_mensal, 2)
        


aluno = Aluno(nome="Joao Victor", notas=[10, 9, 9, 8])
print(aluno)

funcionario1 = Funcionario(nome="Joao", valor_hora_trabalho=18.50)
funcionario2 = Funcionario(nome="Jose", valor_hora_trabalho=21.00)
funcionario3 = Funcionario(nome="Joaquin", valor_hora_trabalho=29.00)
funcionario3 = Funcionario(nome="Junior")

empresa = Empresa(nome="Teste", funcionarios=[funcionario1, funcionario2, funcionario3])
print(f"Despesa mensal da empresa com salarios: {empresa.calcular_despesas_da_empresa_mensais()}")
