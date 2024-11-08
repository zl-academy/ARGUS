from exceptions.valor_invalido_error import ValorInvalidoError

class Produto:
    def __init__(self, nome, preco, categoria):
        if preco <= 0:
            raise ValorInvalidoError("O preço do produto deve ser positivo.")
        self._nome = nome
        self._preco = preco
        self._categoria = categoria

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_categoria(self):
        return self._categoria

    def detalhes(self):
        return f"Produto: {self._nome}, Preço: R${self._preco}, Categoria: {self._categoria}"
