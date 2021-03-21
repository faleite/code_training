"""
Utilizando o conceito de dicionários, faça uma ficha de cadastro
de 4 funcionários utilizando a seguinte estrutura:
Chave: Nome Dados: Idade, email, setor, salario
Inclua os funcionários:
Joao Pereira, 25, joao.pereira@hurb.com, marketing, 1950
Maria Silva, 23, maria.silva@hurb.com, comercial, 2300
Pedro Peixoto, 32 pedro.peixoto@hurb.com, operacao, 2625
Luiza Almeida, 28, luiza.almeida@hurb.com, atendimento, 2120
Faça um programa que retorne o nome, email e setor de todos
os funcioárioscom mais de 25 anos.

"""
import unittest


def filtrar_maiores_de_25(colaboradores):
    resultado = []
    for nome, (idade, email, setor, _) in colaboradores.items():
        if idade >= 25:
            resultado.append((nome, email, setor))
    return resultado


class TesteColaboradores(unittest.TestCase):
    def test_filtragem_colaboradores(self) -> None:
        colaboradores = {
            'Joao Pereira': [25, 'joao.pereira@hurb.com', 'marketing', 1950],
            'Maria Silva': [23, 'maria.silva@hurb.com', 'comercial', 2300],
            'Pedro Peixoto': [32, 'pedro.peixoto@hurb.com', 'operacao', 2625],
            'Luiza Almeida': [28, 'luiza.almeida@hurb.com', 'atendimento', 2120],
        }
        resultado = filtrar_maiores_de_25(colaboradores)

        self.assertEqual(
            resultado,
            [
                ('Joao Pereira', 'joao.pereira@hurb.com', 'marketing'),
                ('Pedro Peixoto', 'pedro.peixoto@hurb.com', 'operacao'),
                ('Luiza Almeida', 'luiza.almeida@hurb.com', 'atendimento'),
            ]
        )
