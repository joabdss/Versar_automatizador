from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

#Abrir Navegador e Site
driver.get("https://playful-torrone-162c28.netlify.app")
sleep(2)

#Clicar em Login
login_button = driver.find_element(By.XPATH, '//span[tect()="Login]')
login_button.click()

# Preenche os campos de login
driver.find_element(By.NAME, 
                    "email").send_keys("qualityassurance@bertoni.com.br")
driver.find_element(By.NAME, "password").send_keys("versar123")

#Efetua o login e entra na página
driver.find_element(By.TAG_NAME, "form").submit()

#Clicar em '+ Criar Módulo'
criar_modulo_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-containedPrimary'))
)
criar_modulo_btn.click()

# Aguarda o campo "Titulo do módulo" e preenche
titulo_input = wait.until(EC.presence_of_element_located((By.XPATH,
                      '//input[@placeholder="Título do Módulo"]')))
titulo_input.send_keys("Módulo Automatizado QA")

#Clica na setinha de "Série"
dropdown_btn = wait.until(EC.element_to_be_clickable((By.ID,
                "mui-component-select-grade_id")))
dropdown_btn.click()

# Aguarda e clica na opção "3 Ano"
opcao_serie = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//ul[@role="listbox"]//li[contains(translate(text(),"º°",""), "3 ANO")]')
))
opcao_serie.click()

# Preenche a descrição
descricao_input = wait.until(EC.presence_of_element_located((By.XPATH,                                       
                        '//textarea[@placeholder="Descrição do Módulo"]')))
descricao_input.send_keys("Este é um módulo criado automaticamente via Selenium.")

# Seleciona a capa (clicando no botao de estrela da primeira opção)
botao_estrela = wait.until(EC.element_to_be_clickable((By.XPATH,
            '(//li[@class="MuiGridListTile-root"]//button[@type="button"])[1]')))
botao_estrela.click()

# Aguarda o botao 'Salvar' final e clica (1)
botao_salvar_final = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//button[.//span[contains(text(), "Salvar")]]')
))
botao_salvar_final.click()

# Aguarda o botao 'Salvar' final e clica (2)
botao_salvar_final = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//button[.//span[contains(text(), "Salvar")]]')
))
botao_salvar_final.click()

# Aguarda o botao 'Salvar Modulo' final e clica
botao_salvar_final_modulo = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//button[.//span[contains(text(), "Salvar Módulo")]]')
))
botao_salvar_final_modulo.click()


sleep(10)
driver.quit()