class ValorInvalidoError(Exception):
    """Exceção lançada quando um valor de produto é inválido (não positivo)."""
    def __init__(self, message="Valor do produto deve ser positivo."):
        self.message = message
        super().__init__(self.message)
