from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def cadastro_web(dataframe):

    # realizando login no sistema
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('link')

    email = browser.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys('email')

    senha = browser.find_element(By.XPATH, '//*[@id="password"]')
    senha.send_keys('senha')

    time.sleep(1)

    botao_entrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
    botao_entrar.click()

    time.sleep(3)

    # iterando nas linhas do dataframe
    for _, linha in dataframe.iterrows(): # i iterrows() sempre tráz o índice e os dados da linha
        cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
        cliente.send_keys(linha['Nome'])

        email = browser.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(linha['E-mail'])

        telefone = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        telefone.send_keys(linha['Telefone'])

        cidade = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cidade.send_keys(linha['Cidade'])

        estado = browser.find_element(By.XPATH, '//*[@id="estado"]')
        estado.send_keys(linha['Estado'])

        time.sleep(3)

        botao_cadastrar = browser.find_element(By.XPATH, '//*[@id="submit"]')
        botao_cadastrar.click()

        time.sleep(3)

    browser.close()





