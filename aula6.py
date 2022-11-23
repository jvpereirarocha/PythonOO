class Funcionario:
    def __init__(self, nome) -> None:
        self._nome = nome
    
    def registra_horas(self, horas):
        print(f"Funcionário: {self._nome} registrando {horas} horas")

class EmpresaTeste(Funcionario):
    
    def registra_horas(self, horas):
        print(f"Funcionario {self._nome} da Empresa Teste registra: {horas} horas")

    def resolver_bugs(self):
        print(f"Resolver bugs")


class EmpresaQualquer(Funcionario):
    
    def registra_horas(self, horas):
        print(f"Registrando {horas} horas para o funcionário {self._nome} da empresa qualquer")

    def consultar_apis_externas(self):
        print(f"Consultando APIs externas")


class Junior(EmpresaTeste):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def estudar_orientacao_a_objetos(self):
        print(f"Estudando OO...")


class Pleno(EmpresaQualquer, EmpresaTeste):

    def escrever_testes_unitarios(self):
        print(f"Escrevendo testes unitários")


class Senior(EmpresaTeste, EmpresaQualquer):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def otimizacoes_de_codigo(self):
        print(f"Otimizando código")

    def monitorar_infra(self):
        print(f"Monitorando infraestrutura")
    
    def ensinar_plenos_e_juniors(self):
        print(f"Mentorando Plenos e Juniors")


junior = Junior(nome="José")
junior.registra_horas(6)
pleno = Pleno(nome="João")
pleno.registra_horas(8)

"""
Ordem do MRO:
- Pleno
- Empresa Qualquer > Funcionario
- Empresa Teste > Funcionario
O MRO verifica se 'Funcionario' é uma "GoodHead". Como a 'Empresa Teste' está no mesmo nível de 'Empresa Qualquer' ele usa a 'Empresa Qualquer'
"""