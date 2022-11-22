class Funcionario:
    def __init__(self, ctps):
        self.ctps = ctps

    def __str__(self):
        return f"Funcionario de registro: {self.ctps}"


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Idade: {self.idade}"



class FuncionarioEmpresa(Pessoa, Funcionario):
    def __init__(self, nome, idade, email) -> None:
        super().__init__(nome, idade)
        self.email = email

    def __str__(self) -> str:
        return super().__str__()


funcionario_empresa = FuncionarioEmpresa("Joao Victor", 25, "11111", email="jv@empresa.com.br")
print(funcionario_empresa)