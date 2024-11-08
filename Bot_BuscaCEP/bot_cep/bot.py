# Importações necessárias
from botcity.web import WebBot, Browser, By
from botcity.plugins.googlesheets import BotGoogleSheetsPlugin
from botcity.plugins.captcha import BotAntiCaptchaPlugin
from botcity.web.parsers import table_to_dict
import pandas as pd
from botcity.maestro import BotMaestroSDK

# Desabilita erros se não estiver conectado ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Constantes de configuração
CAMINHO_ARQUIVO_CREDENCIAIS = r"camainho\credenciais.json"
ID_PLANILHA_ORIGEM = "id planilha origem dos dados (Onde estão os ceps)"
ID_PLANILHA_DESTINO = "id planilha destino dos dados (onde serão salvos os endereços)"
API_KEY = "API KEY (BotAntiCaptcha)"

def main():
    maestro = BotMaestroSDK.from_sys_args()
    bot = WebBot()
    
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = r"resources\chromedriver-win64\chromedriver.exe"

    # Instancia plugins para planilhas de origem e destino
    planilha_origem = BotGoogleSheetsPlugin(CAMINHO_ARQUIVO_CREDENCIAIS, ID_PLANILHA_ORIGEM)
    planilha_destino = BotGoogleSheetsPlugin(CAMINHO_ARQUIVO_CREDENCIAIS, ID_PLANILHA_DESTINO)

    # Pega os CEPs da planilha de origem
    lista_ceps = [linha[0] for linha in planilha_origem.as_list() if linha]
    dados_relatório = []

    # Processa cada CEP
    for cep in lista_ceps:
        print(f"Consultando CEP: {cep}")
        enderecos = consultar_ceps(cep, bot)
        print(f"Dados retornados da tabela: {enderecos}")
        if enderecos:
            endereco = enderecos[0]
            dados_relatório.append({
                'CEP': endereco.get('cep', 'N/A'),
                'Logradouro': endereco.get('logradouro', 'N/A'),
                'Bairro': endereco.get('bairro', 'N/A'),
                'Cidade': endereco.get('localidadeuf', 'N/A').split('/')[0],
                'Estado': endereco.get('localidadeuf', 'N/A').split('/')[1] if '/' in endereco.get('localidadeuf', 'N/A') else 'N/A'
            })
            planilha_destino.add_rows([[endereco['logradouro'], endereco['bairro'], endereco['localidadeuf'], endereco.get('cep', 'N/A')]])
        else:
            print(f"Nenhum dado encontrado para o CEP: {cep}")

    # Salva o relatório em Excel
    df = pd.DataFrame(dados_relatório)
    df.to_excel('relatorio_enderecos.xlsx', index=False)

    bot.stop_browser()

def consultar_ceps(cep, bot: WebBot):
    bot.browse("https://buscacepinter.correios.com.br/app/endereco/index.php")
    bot.find_element("endereco", By.ID).send_keys(cep)
    
    # Resolver captcha
    captcha_img = bot.find_element("captcha_image", By.ID)
    captcha_img.screenshot("captcha.png")
    resposta_captcha = BotAntiCaptchaPlugin(API_KEY).solve_text("captcha.png")
    bot.find_element("captcha", By.ID).send_keys(resposta_captcha)

    # Realiza a pesquisa
    bot.find_element("btn_pesquisar", By.ID).click()
    bot.wait(2000)

    # Captura o resultado
    try:
        tabela_endereco = table_to_dict(bot.find_element("resultado-DNEC", By.ID))
        if tabela_endereco:
            return [{
                'logradouro': tabela_endereco[0].get('logradouronome', 'N/A'),
                'bairro': tabela_endereco[0].get('bairrodistrito', 'N/A'),
                'localidadeuf': tabela_endereco[0].get('localidadeuf', 'N/A'),
                'cep': tabela_endereco[0].get('cep', 'N/A')
            }]
    except Exception as e:
        print(f"Erro ao buscar dados do CEP {cep}: {e}")
    return []

if __name__ == '__main__':
    main()
