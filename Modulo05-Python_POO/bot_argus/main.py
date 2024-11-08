from models.produto import Produto
from models.pedido import Pedido
from models.gestor_de_pedidos import GestorDePedidos
from exceptions.valor_invalido_error import ValorInvalidoError
from exceptions.quantidade_invalida_error import QuantidadeInvalidaError

if __name__ == "__main__":
    gestor = GestorDePedidos()

    try:
        produto1 = Produto("Notebook", 3000, "Eletrônicos")
        produto2 = Produto("Mouse", 50, "Eletrônicos")
        produto3 = Produto("Teclado", 120, "Eletrônicos")

        pedido = Pedido([produto1, produto2], {produto1: 1, produto2: 2}, "Cliente A")
        gestor.adicionar_pedido(pedido)

        # Agora, ao imprimir a lista de pedidos, ele exibirá uma descrição legível
        print(gestor.listar_pedidos_por_status("Novo"))
        gestor.salvar_dados_json()
        gestor.salvar_dados_binario()
    except ValorInvalidoError as e:
        print(e)
    except QuantidadeInvalidaError as e:
        print(e)
