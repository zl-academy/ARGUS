import time
from botcity.web import WebBot, Browser, By
from models.gestor_de_pedidos import GestorDePedidos
from models.produto import Produto
from models.pedido import Pedido
import pandas as pd
import os

class PlanilhaBot:
    def __init__(self):
        self.caminho_planilha = "data/pedidos.xlsx"
        print("\n🤖 Bot inicializado com sucesso!")
        time.sleep(0.5)
        
        # Verifica se o diretório data existe
        if not os.path.exists("data"):
            print("📁 Criando diretório data...")
            time.sleep(0.5)
            os.makedirs("data")
            
        # Verifica se a planilha existe
        if not os.path.exists(self.caminho_planilha):
            print("📝 Planilha não encontrada. Criando nova planilha com dados de exemplo...")
            time.sleep(0.5)
            self.criar_planilha_inicial()
        
    def criar_planilha_inicial(self):
        """Cria planilha inicial com dados de exemplo"""
        gestor = self.criar_pedidos_exemplo()
        self.preencher_planilha(gestor)
        
    def criar_pedidos_exemplo(self):
        """Cria 10 pedidos de exemplo com 5 clientes diferentes"""
        print("\n🤖 Iniciando criação de pedidos de exemplo...")
        time.sleep(0.5)
        
        clientes = ["Hercules Freitas", "Arlana Braga", "Brena Cidade", "Millena Sângela", "Emmerson da Silva"]
        produtos_disponiveis = [
            ("Notebook Dell", 4500, "Eletrônicos"),
            ("MacBook Pro", 12000, "Eletrônicos"),
            ("Mouse Gamer", 250, "Eletrônicos"),
            ("Teclado Mecânico", 450, "Eletrônicos"),
            ("Monitor 27\"", 2200, "Eletrônicos"),
            ("Headset", 180, "Eletrônicos"),
            ("Impressora", 1200, "Eletrônicos"),
            ("Smartphone", 3500, "Eletrônicos"),
            ("Tablet", 2800, "Eletrônicos"),
            ("Webcam HD", 300, "Eletrônicos")
        ]
        
        gestor = GestorDePedidos()
        status_opcoes = ["Novo", "Em Processamento", "Concluído"]
        
        pedidos_criados = 0
        for i, cliente in enumerate(clientes * 2):
            import random
            num_produtos = random.randint(2, 3)
            produtos_pedido = random.sample(produtos_disponiveis, num_produtos)
            
            produtos = []
            quantidades = {}
            
            print(f"\n📦 Criando pedido {pedidos_criados + 1} para {cliente}...")
            time.sleep(0.5)
            
            for prod_nome, prod_preco, prod_categoria in produtos_pedido:
                produto = Produto(prod_nome, prod_preco, prod_categoria)
                produtos.append(produto)
                quantidade = random.randint(1, 3)
                quantidades[produto] = quantidade
                print(f"   ➕ Adicionado: {prod_nome} (Quantidade: {quantidade})")
                time.sleep(0.5)
            
            status = random.choice(status_opcoes)
            pedido = Pedido(produtos, quantidades, cliente, status)
            gestor.adicionar_pedido(pedido)
            pedidos_criados += 1
            print(f"   ✅ Pedido finalizado com status: {status}")
            time.sleep(0.5)
            
        print(f"\n🎉 Total de {pedidos_criados} pedidos criados com sucesso!")
        time.sleep(0.5)
        return gestor

    def preencher_planilha(self, gestor):
        """Preenche planilha Excel com dados dos pedidos."""
        try:
            print(f"\n📝 Iniciando exportação para planilha {self.caminho_planilha}...")
            time.sleep(0.5)
            
            dados = []
            total_produtos = 0
            
            for pedido in gestor._pedidos:
                for produto in pedido.get_produtos():
                    dados.append({
                        'Cliente': pedido.get_cliente(),
                        'Status': pedido.get_status(),
                        'Produto': produto.get_nome(),
                        'Preço': produto.get_preco(),
                        'Categoria': produto.get_categoria(),
                        'Quantidade': pedido.get_quantidade()[produto],
                        'Total': produto.get_preco() * pedido.get_quantidade()[produto]
                    })
                    total_produtos += 1
            
            df = pd.DataFrame(dados)
            df.to_excel(self.caminho_planilha, index=False)
            print(f"✅ {total_produtos} produtos exportados com sucesso para {self.caminho_planilha}")
            time.sleep(0.5)
            
        except Exception as e:
            print(f"❌ Erro ao preencher planilha: {e}")
            time.sleep(0.5)
            
    def extrair_dados_planilha(self, gestor):
        """Extrai dados da planilha Excel e cria pedidos."""
        try:
            print(f"\n📊 Iniciando extração de dados da planilha {self.caminho_planilha}...")
            time.sleep(0.5)
            
            if not os.path.exists(self.caminho_planilha):
                print("❌ Planilha não encontrada! Criando nova planilha...")
                time.sleep(0.5)
                self.criar_planilha_inicial()
                
            df = pd.read_excel(self.caminho_planilha)
            clientes_unicos = df['Cliente'].unique()
            print(f"📋 Encontrados {len(clientes_unicos)} clientes diferentes")
            time.sleep(0.5)
            
            pedidos_criados = 0
            for cliente in clientes_unicos:
                print(f"\n👤 Processando pedidos do cliente: {cliente}")
                time.sleep(0.5)
                
                pedidos_cliente = df[df['Cliente'] == cliente]
                produtos = []
                quantidades = {}
                
                for _, row in pedidos_cliente.iterrows():
                    produto = Produto(
                        nome=row['Produto'],
                        preco=float(row['Preço']),
                        categoria=row['Categoria']
                    )
                    produtos.append(produto)
                    quantidades[produto] = int(row['Quantidade'])
                    print(f"   ➕ Produto adicionado: {produto.get_nome()}")
                    time.sleep(0.5)
                
                status = pedidos_cliente.iloc[0]['Status']
                pedido = Pedido(produtos, quantidades, cliente, status)
                gestor.adicionar_pedido(pedido)
                pedidos_criados += 1
                print(f"   ✅ Pedido criado com status: {status}")
                time.sleep(0.5)
            
            print(f"\n🎉 Total de {pedidos_criados} pedidos importados com sucesso!")
            time.sleep(0.5)
            
        except Exception as e:
            print(f"❌ Erro ao extrair dados da planilha: {e}")
            time.sleep(0.5)