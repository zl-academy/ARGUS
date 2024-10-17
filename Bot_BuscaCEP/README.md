# Bot de Busca de CEPs e Geração de Relatório

Este projeto é um bot de automação que utiliza a biblioteca **BotCity** para buscar informações de endereços a partir de uma lista de CEPs em uma planilha do Google Sheets. O bot resolve captchas automaticamente e gera um relatório em Excel com os dados coletados.

## Funcionalidades

- Coleta de CEPs a partir de uma planilha Google Sheets.
- Consulta automática de endereços no site dos Correios.
- Resolução de captchas usando o plugin **BotAntiCaptcha**.
- Geração de relatório em formato Excel com os resultados das consultas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **BotCity**: Automação da web e integração com Google Sheets e Captcha.
- **Pandas**: Manipulação de dados e geração de arquivos Excel.
- **Google Sheets API**: Integração para ler e escrever dados em planilhas.
- **BotAntiCaptcha**: Plugin para resolver captchas automaticamente.
- **Ambiente Virtual (venv)**: Gerenciamento de dependências isoladas.

## Pré-requisitos

- Python 3.10 para o bot.
- Google Sheets API habilitada e credenciais configuradas.
- Conta no **AntiCaptcha** para resolver captchas.
- Driver do **Chrome** para automação de navegador.

## Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/Millenas/ARGUS.git
   ```
   
2. Crie e ative o ambiente virtual:
   ```bash
   # No Windows
   python -m venv venv
   venv\Scripts\activate

   # No Linux ou macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as credenciais da API do Google Sheets:
   - Coloque o arquivo `credenciais.json` no caminho especificado no código.

5. Atualize as variáveis de configuração no arquivo principal:
   - `CAMINHO_ARQUIVO_CREDENCIAIS`
   - `ID_PLANILHA_ORIGEM`
   - `ID_PLANILHA_DESTINO`
   - `API_KEY` do AntiCaptcha

6. Baixe o driver do Chrome (Chromedriver) e coloque no diretório `resources`.

## Execução

Para executar o bot, siga os passos abaixo:

1. Ative o ambiente virtual (caso não esteja ativado):
   ```bash
   # No Windows
   venv\Scripts\activate

   # No Linux ou macOS
   source venv/bin/activate
   ```

2. Execute o bot:
   ```bash
   python boy.py
   ```

O bot irá:
- Ler os CEPs da planilha de origem.
- Realizar a consulta nos Correios.
- Resolver o captcha.
- Escrever os resultados em uma planilha de destino e gerar um relatório Excel.

## Estrutura do Projeto

```bash
Bot_BuscaCEP/
  ├── bot_cep/ 
    └─── resources/        # Diretório com o Chromedriver
    └─── bot.py                # Arquivo principal do bot
    └─── requirements.txt       # Dependências do projeto
    └── relatorio_enderecos.xlsx # Relatório gerado pelo bot
  ├── venv/                  # Ambiente virtual
  ├── credenciais.json       # Credenciais do Google Sheets (não incluído)

```


## Links Úteis

- [Documentação BotCity](https://documentation.botcity.dev/) - Guia oficial para automação com BotCity.
- [Google Sheets API](https://documentation.botcity.dev/plugins/google/credentials/) - Como usar a API do Google Sheets.
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Referência para manipulação de dados com Pandas.
- [AntiCaptcha](https://documentation.botcity.dev/plugins/captcha/) - API para resolver captchas automaticamente.
- [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/#stable) - Baixe o driver para automação no Chrome.
- [Vídeo Demo](https://youtu.be/UpRES2uQrhc?si=eesT80Bqys5qhOZo) - Assista o vídeo do projeto em execução 

Esses links ajudam a configurar e entender melhor as ferramentas usadas no projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

