

# 📚 Documentação do Sistema de Gestão de Pedidos

## 📋 Visão Geral
O sistema é uma aplicação Python para gestão de pedidos que integra funcionalidades de manipulação de dados com automação através de um bot para processamento de planilhas.

## 🏗️ Estrutura do Projeto
```
bot_argus/
├── bot/
│   ├── bot.py
│   └── build scripts
├── data/
│   ├── pedidos.xlsx
│   ├── pedidos.json
│   └── pedidos.pkl
├── decorators/
│   └── log_atividade.py
├── exceptions/
│   ├── quantidade_invalida_error.py
│   └── valor_invalido_error.py
├── logs/
│   └── log_atividades.txt
├── models/
│   ├── gestor_de_pedidos.py
│   ├── pedido.py
│   └── produto.py
├── utils/
│   └── arquivo_utils.py
└── main.py
```

## 🔧 Componentes Principais

### 1. Classe Produto
- Responsável pelo gerenciamento das informações dos produtos
- Armazena nome, preço e categoria do produto
- Implementa validações para garantir preços positivos
- Fornece métodos para acesso aos dados do produto

### 2. Classe Pedido
- Gerencia informações completas de um pedido
- Mantém lista de produtos e suas respectivas quantidades
- Calcula valor total do pedido
- Permite acompanhamento do status do pedido
- Fornece métodos para visualização detalhada do pedido

### 3. GestorDePedidos
- Gerencia a coleção completa de pedidos do sistema
- Funcionalidades principais:
  - Adição de novos pedidos
  - Filtragem de pedidos por status
  - Análise de pedidos por categoria
  - Cálculo de vendas totais
  - Persistência de dados em JSON e formato binário
- Implementa logging de atividades

### 4. PlanilhaBot
- Automatiza operações com planilhas Excel
- Funcionalidades principais:
  - Criação automática de planilhas com dados exemplo
  - Importação de dados de planilhas existentes
  - Exportação de dados do sistema para planilhas
  - Validação e processamento de dados
- Integração completa com o sistema de pedidos

## 🚀 Como Usar

1. **Instalação de Dependências**:
```bash
pip install -r requirements.txt
```

2. **Execução do Sistema**:
```bash
python main.py
```

## 🔄 Fluxo de Dados
1. O sistema inicia verificando/criando estrutura de arquivos
2. Carrega dados existentes ou cria exemplos
3. Processa pedidos através do gestor
4. Salva dados em múltiplos formatos (Excel, JSON, binário)

## 🛠️ Funcionalidades Principais

### Gestão de Pedidos
- Criação e monitoramento de pedidos
- Cálculo automático de totais
- Categorização por status

### Persistência de Dados
- Suporte a múltiplos formatos
- Backup automático
- Logs de atividades

### Automação
- Processamento automático de planilhas
- Geração de dados de exemplo
- Validações automáticas

## 📝 Logs e Monitoramento
- Sistema de logs automático via decorator
- Registro de todas operações importantes
- Rastreamento de erros e exceções

## ⚠️ Tratamento de Erros
- Validação de valores negativos
- Verificação de quantidades inválidas
- Tratamento de erros de arquivo

## 🔒 Requisitos do Sistema
- Python 3.x
- Dependências listadas em requirements.txt
- Acesso a sistema de arquivos