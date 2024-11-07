class QuantidadeInvalidaError(Exception):
    """Exceção lançada quando uma quantidade de pedido é inválida (não positiva)."""
    def __init__(self, message="Quantidade do pedido deve ser positiva."):
        self.message = message
        super().__init__(self.message)
