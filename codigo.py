#  Passo a passo do projeto: 
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 0.7

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever em texto
# pyautogui.press -> pressionar uma tecla do teclado

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=618, y=413)
pyautogui.write("bcrespo@python.com")

# escrever a senha
pyautogui.press("tab")
pyautogui.write("12345")

# clicar no botão de logar
pyautogui.click(x=681, y=562)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")


# Passo 4: Cadastrar 1 produto
for linha in tabela.index:

    # clicar no primeiro campo
    pyautogui.click(x=547, y=295)
    # Codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro até acabar