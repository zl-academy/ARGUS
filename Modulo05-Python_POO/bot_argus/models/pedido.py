from functools import reduce

class Pedido:
    def __init__(self, produtos, quantidade, cliente, status="Novo"):
        self._produtos = produtos
        self._quantidade = quantidade
        self._cliente = cliente
        self._status = status

    def get_produtos(self):
        return self._produtos

    def get_quantidade(self):
        return self._quantidade

    def get_cliente(self):
        return self._cliente

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def total_pedido(self):
        # Corrige a ausência do import do reduce
        return reduce(lambda total, produto: total + produto.get_preco() * self._quantidade[produto], self._produtos, 0)

    def detalhes_pedido(self):
        detalhes = f"Cliente: {self._cliente}, Status: {self._status}\n"
        for produto in self._produtos:
            detalhes += f"{produto.detalhes()} - Quantidade: {self._quantidade[produto]}\n"
        detalhes += f"Total: R${self.total_pedido():.2f}"
        return detalhes

    def __repr__(self):
        """Retorna uma descrição legível do pedido para facilitar a impressão"""
        return f"Pedido(cliente='{self._cliente}', status='{self._status}', total={self.total_pedido():.2f})"
