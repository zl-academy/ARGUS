from functools import reduce  # Importando o reduce novamente
from decorators.log_atividade import log_atividade
from utils.arquivo_utils import salvar_dados_json, carregar_dados_json, salvar_dados_binario, carregar_dados_binario

class GestorDePedidos:
    def __init__(self):
        self._pedidos = []

    @log_atividade
    def adicionar_pedido(self, pedido):
        self._pedidos.append(pedido)

    @log_atividade
    def listar_pedidos_por_status(self, status):
        return list(filter(lambda pedido: pedido.get_status() == status, self._pedidos))

    def pedidos_por_categoria(self, categoria):
        produtos_por_categoria = map(lambda pedido: sum(1 for produto in pedido.get_produtos() if produto.get_categoria() == categoria), self._pedidos)
        return sum(produtos_por_categoria)

    def total_vendas(self):
        """Calcula o total de todas as vendas, somando o total de cada pedido usando 'reduce'"""
        return reduce(lambda total, pedido: total + pedido.total_pedido(), self._pedidos, 0)

    def salvar_dados_json(self, caminho="data/pedidos.json"):
        try:
            # Chama a função de utilitário para salvar os dados
            salvar_dados_json([pedido.detalhes_pedido() for pedido in self._pedidos], caminho)
        except Exception as e:
            print(f"Erro ao salvar dados em JSON: {e}")

    def carregar_dados_json(self, caminho="data/pedidos.json"):
        try:
            # Chama a função de utilitário para carregar os dados
            pedidos_data = carregar_dados_json(caminho)
            if pedidos_data:
                self._pedidos = pedidos_data
            print("Dados carregados de JSON com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar dados de JSON: {e}")

    def salvar_dados_binario(self, caminho="data/pedidos.pkl"):
        try:
            # Chama a função de utilitário para salvar os dados binários
            salvar_dados_binario(self._pedidos, caminho)
        except Exception as e:
            print(f"Erro ao salvar dados em binário: {e}")

    def carregar_dados_binario(self, caminho="data/pedidos.pkl"):
        try:
            # Chama a função de utilitário para carregar os dados binários
            pedidos_data = carregar_dados_binario(caminho)
            if pedidos_data:
                self._pedidos = pedidos_data
            print("Dados carregados de binário com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar dados de binário: {e}")
