import time
from models.produto import Produto
from models.pedido import Pedido
from models.gestor_de_pedidos import GestorDePedidos
from exceptions.valor_invalido_error import ValorInvalidoError
from exceptions.quantidade_invalida_error import QuantidadeInvalidaError
from bot.bot import PlanilhaBot

if __name__ == "__main__":
    try:
        print("\n🚀 Iniciando sistema de gestão de pedidos...")
        time.sleep(0.5)
        
        # Criar bot (que já verifica e cria a planilha se necessário)
        bot = PlanilhaBot()
        
        # Criar gestor para receber dados da planilha
        gestor = GestorDePedidos()
        print("\n📊 Gestor de pedidos inicializado")
        time.sleep(0.5)
        
        # Extrair dados da planilha pedidos.xlsx
        bot.extrair_dados_planilha(gestor)
        
        # Imprimir informações dos pedidos carregados
        print("\n📊 Resumo dos pedidos carregados:")
        time.sleep(0.5)
        
        for status in ["Novo", "Em Processamento", "Concluído"]:
            pedidos = gestor.listar_pedidos_por_status(status)
            print(f"\n📌 Status: {status}")
            time.sleep(0.5)
            for pedido in pedidos:
                print(f"   • {pedido}")
                time.sleep(0.5)
        
        print(f"\n💰 Total de vendas: R${gestor.total_vendas():.2f}")
        time.sleep(0.5)
        
        # Salvar dados
        print("\n💾 Salvando dados...")
        time.sleep(0.5)
        gestor.salvar_dados_json()
        gestor.salvar_dados_binario()
        print("✅ Processo finalizado com sucesso!")
        time.sleep(0.5)

    except (ValorInvalidoError, QuantidadeInvalidaError) as e:
        print(f"❌ Erro de validação: {e}")
        time.sleep(0.5)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        time.sleep(0.5)