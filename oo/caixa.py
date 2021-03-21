"""
>>> caixa = Caixa(saldo=1000)
>>> caixa.consultar_saldo()
1000
>>> caixa_2 = Caixa()
>>> caixa_2.consultar_saldo()
0
>>> caixa.pagar_em_dinheiro(valor_pago=100, valor_produto=40)
60
>>> caixa.consultar_saldo()
1040
>>> caixa.consultar_fita()
['Pagamento em dinheiro no valor de R$ 100, troco retornado de R$ 60']
>>> # adicionando mais um pagamento
>>> caixa.pagar_em_dinheiro(valor_pago=200, valor_produto=10)
190
>>> caixa.consultar_saldo()
1050
>>> caixa.consultar_fita()
['Pagamento em dinheiro no valor de R$ 100, troco retornado de R$ 60', 'Pagamento em dinheiro no valor de R$ 200, troco retornado de R$ 190']
>>> caixa.pagar_em_cc(valor_produto=30, numero_cartao='1234')
0
>>> caixa.consultar_fita()
['Pagamento em dinheiro no valor de R$ 100, troco retornado de R$ 60', 'Pagamento em dinheiro no valor de R$ 200, troco retornado de R$ 190', 'Pagamento em cc no valor de R$ 30, numero cc; 1234']
"""


class Pagamento:
    """
    Responsabilidade de manter os dados de um pagamento específico
    """

    def __init__(self, valor_produto):
        self.valor_produto = valor_produto

    def calcular_troco(self):
        return 0


class PagamentoEmDinheiro(Pagamento):
    def __init__(self, valor_pago, valor_produto):
        super().__init__(valor_produto)
        self.valor_pago = valor_pago

    def calcular_troco(self):
        return self.valor_pago - self.valor_produto

    def __str__(self):
        return f'Pagamento em dinheiro no valor de R$ {self.valor_pago}, troco retornado de R$ {self.calcular_troco()}'


class PagamentoEmCartaoDeCredito(Pagamento):

    def __init__(self, valor_produto, numero_cartao):
        super().__init__(valor_produto)
        self.numero_cartao = numero_cartao

    def __str__(self):
        return f'Pagamento em cc no valor de R$ {self.valor_produto}, numero cc; {self.numero_cartao}'


class Caixa:
    """
    Responsabilidade de manter resgistros de pagamentos
    """

    def __init__(self, saldo=0):
        self.saldo = saldo
        self._pagamentos = []  # O dunder "_" protege a variavel

    def consultar_saldo(self):
        return self.saldo

    def pagar_em_dinheiro(self, valor_pago, valor_produto):
        pgto = PagamentoEmDinheiro(valor_pago, valor_produto)
        return self._registrar_pagamento(pgto)

    def consultar_fita(self):
        return [str(pgto) for pgto in self._pagamentos]

    def pagar_em_cc(self, valor_produto, numero_cartao):
        pgto = PagamentoEmCartaoDeCredito(valor_produto, numero_cartao)
        return self._registrar_pagamento(pgto)

    def _registrar_pagamento(self, pgto: Pagamento):
        self._pagamentos.append(pgto)
        self.saldo += pgto.valor_produto
        return pgto.calcular_troco()
