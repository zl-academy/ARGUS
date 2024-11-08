import pandas as pd
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# Função para ler o Excel e retornar os dados dos funcionários
def ler_dados_excel(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo)
        # Filtrar apenas os funcionários que ainda não foram cadastrados
        df = df[df['Status'] != 'Cadastrado']
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo Excel não encontrado no caminho {caminho_arquivo}")
        return None

# Função para atualizar o status no Excel
def atualizar_status_excel(caminho_arquivo, df):
    try:
        df.to_excel(caminho_arquivo, index=False)
        print("Arquivo Excel atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar o Excel: {e}")
''
# Função principal de automação
def main():
    # Caminho do arquivo Excel 
    caminho_excel = "C:/Users/braga/OneDrive/Área de Trabalho/projetos/AutoRegister/cadastro/funcionarios.xlsx"

    #caminho_excel = r"C:\Users\Brena\Downloads\cadastro\funcionarios.xlsx"

    # Ler os dados dos funcionários
    df_funcionarios = ler_dados_excel(caminho_excel)
    if df_funcionarios is None or df_funcionarios.empty:
        print("Nenhum funcionário para cadastrar, funcionarios cadastrados.")
        return

    webbot = WebBot()

    # Configuração do navegador
    webbot.headless = False
    webbot.browser = Browser.CHROME
    webbot.driver_path = ChromeDriverManager().install()

    # Acessar o Google Forms
    #webbot.browse("https://forms.gle/RsScG4dLXhQwADbbA")
    webbot.browse("https://forms.gle/24kLtdEd7vb9Jwpg6")
    webbot.wait(5000)
    

    # Fazer login (apenas quando usarmos o forms fornecido, que permite apenas uma resposta por logins)
    """
    webbot.enter()
    webbot.wait(2000)
    email_field = webbot.find_element('//*[@id="identifierId"]', By.XPATH)
    #email_field.send_keys("brena.cidade@ifam.edu.br")
    email_field.send_keys("arlana.silva@ifam.edu.br")
    webbot.enter()
    webbot.wait(3000)

    password_field = webbot.find_element('//*[@id="password"]/div[1]/div/div[1]/input', By.XPATH)
    #password_field.send_keys("011.876.382-26")
    password_field.send_keys("703.813.102-80")
    webbot.enter()
    """
    webbot.wait(10000)
    #webbot = input()

    # Preenchimento do formulário com os dados de cada funcionário
    for index, funcionario in df_funcionarios.iterrows():
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['Nome'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['E-mail'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['Departamento'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', By.XPATH).send_keys(funcionario['Endereco'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea', By.XPATH).send_keys(funcionario['CPF'])
        webbot.wait(1000)
        webbot.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input', By.XPATH).send_keys(funcionario['RG'])
        webbot.wait(1000)


        # Selecionar o turno
        if funcionario['Turno'] == 'Primeiro':
            turno_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span' 
        elif funcionario['Turno'] == 'Segundo':
            turno_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
        else:
            turno_xpath = None

        if turno_xpath:
            webbot.find_element(turno_xpath, By.XPATH).click()
            webbot.wait(500)  # Espera um pouco entre os cliques
            webbot.find_element(turno_xpath, By.XPATH).click()

        
        # Selecionar o gênero
        if funcionario['Gênero'] == 'Masculino':
            genero_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
        elif funcionario['Gênero'] == 'Feminino':
            genero_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
        else:
            genero_xpath = None

        if genero_xpath:
            webbot.find_element(genero_xpath, By.XPATH).click()
            webbot.wait(500)  # Espera um pouco entre os cliques
            webbot.find_element(genero_xpath, By.XPATH).click()
        

        webbot.wait(2000)
        # Enviar o formulário
        enviar_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        enviar_button = webbot.find_element(enviar_button_xpath, By.XPATH)
        if enviar_button:
            enviar_button.click()  # Clique no botão de envio
        else:
            print("Erro: Botão de envio não encontrado.")
        webbot.wait(5000)  # Espera após envio

        # Atualizar o status para "Cadastrado"
        df_funcionarios.at[index, 'Status'] = 'Cadastrado'

    # Atualizar o Excel com os novos status
    atualizar_status_excel(caminho_excel, df_funcionarios)
    
    # Fechar o navegador
    webbot.stop_browser()

if __name__ == '__main__':
    main()

