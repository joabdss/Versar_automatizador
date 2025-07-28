import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)


try:
        driver.get("https://playful-torrone-162c28.netlify.app")
        sleep(2)
#----------------------------------------------LOGIN---------------------------------------------------------------------------
        driver.find_element(By.XPATH, '//span[text()="Login"]').click()
        driver.find_element(By.NAME, "email").send_keys("qualityassurance@bertoni.com.br")
        driver.find_element(By.NAME, "password").send_keys("versar123")
        driver.find_element(By.TAG_NAME, "form").submit()
#-----------------------------------------------MODULO---------------------------------------------------------------------------
        criar_modulo_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.MuiButton-containedPrimary')))
        criar_modulo_btn.click()

        titulo_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Título do Módulo"]')))
        titulo_input.send_keys("Módulo Automatizado QA")

        dropdown_btn = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-grade_id")))
        dropdown_btn.click()
        opcao_serie = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//ul[@role="listbox"]//li[contains(translate(text(),"º°", ""), "3 ANO")]')
        ))
        opcao_serie.click()

        descricao_input = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Descrição do Módulo"]')))
        descricao_input.send_keys("Este é um módulo criado automaticamente via Selenium.")

        botao_estrela = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '(//li[@class="MuiGridListTile-root"]//button[@type="button"])[1]')
        ))
        botao_estrela.click()

        botao_salvar = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[.//span[contains(text(),"Salvar")]]')
        ))
        botao_salvar.click()
#---------------------------------------------------CRIAR TEMA PÓS MÓDULO-----------------------------------------------------------------
        wait = WebDriverWait(driver, 10)
        botao_criar_tema_modulo = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Criar tema')]]")))
        botao_criar_tema_modulo.click()

        titulo_input_titulotemamod = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Título do Tema"]')))
        titulo_input_titulotemamod.send_keys("Módulo Automatizado QA - Tema")

        campo_segmento = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-segment_id")))
        campo_segmento.click()
        opcao_segmento = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Ensino Médio')]")))
        opcao_segmento.click()

        habilidades_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#skill_ids .css-1hwfws3")))
        actions = ActionChains(driver)
        actions.double_click(habilidades_dropdown).perform()
        menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-26l3qy-menu")))
        opcao_habilidade = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-26l3qy-menu')]//div[text()='Autopercepção']")))
        opcao_habilidade.click()
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(2)  

        driver.execute_script("window.scrollBy(0, 1000);") 
        time.sleep(1)  

        botao_capa = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "MuiGridListTileBar-actionIcon")]//button[contains(@class, "MuiIconButton-root")]')))
        driver.execute_script("arguments[0].click();", botao_capa)

        botao_salvar = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[.//span[contains(text(), "Salvar")]]')))
        botao_salvar.click()
        time.sleep(5) 
#-----------------------------------------------------CRIAR CONTEÚDO PÓS-TEMA-MODULO--------------------------------------------
        wait = WebDriverWait(driver, 10)
        botao_criar_conteudo_modulo = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Criar conteúdo')]]")))
        botao_criar_conteudo_modulo.click()
    
        titulo_input_titulocontmod = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Título do Conteúdo"]')))
        titulo_input_titulocontmod.send_keys("Módulo Automatizado QA - Conteúdo")
        
        segmento_conteudo = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Infantil')]]")))
        segmento_conteudo.click()

        driver.execute_script("window.scrollBy(0, 1000);") 
        time.sleep(1)  

        campo_foco_cont = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-occupation_id")))
        campo_foco_cont.click()
        opcao_foco = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Estudante')]")))
        opcao_foco.click()
        
        categoria_btn = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-category_id")))
        actions.double_click(categoria_btn).perform()
        opcao_categoria = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Conhecer')]")))
        opcao_categoria.click()
        time.sleep(1)  

        botao_avançar = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[.//span[contains(text(), "Avançar")]]')))
        botao_avançar.click()
        time.sleep(5)
#------------------------------------------------ PÁGINA COMPONENTES CONTEUDO-MODULO
        wait = WebDriverWait(driver, 10)
        def test_editor_nao_editavel(driver):
            # Verifica se o editor está read-only
            is_readonly = driver.execute_script("return tinymce.activeEditor.getMode() === 'readonly';")
            if is_readonly:
                pytest.fail("Erro: O campo de texto está em modo somente leitura (read-only)")

            # Tenta inserir texto
            driver.execute_script("tinymce.activeEditor.setContent('Teste automático');")
            conteudo = driver.execute_script("return tinymce.activeEditor.getContent();")
            assert "Teste automático" in conteudo, "Erro: Não conseguiu escrever no editor."
        time.sleep(1)  
        

        url_input_video = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="URL"]')))
        url_input_video.send_keys("https://www.youtube.com/watch?v=2PuFyjAs7JA")
        
        driver.execute_script("window.scrollBy(0, 1000);") 
        time.sleep(1)  

        def test_avancar_sem_redirecionamento(driver):
            # Clica no botão
            botao = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[.//span[contains(text(), "Avançar")]]'))
            )
            driver.execute_script("arguments[0].click();", botao)
            
            # Verifica se houve mudança de URL ou página
            try:
                WebDriverWait(driver, 5).until(
                    EC.url_changes(driver.current_url)
                )
                assert False, "Redirecionamento inesperado ocorreu — mas esperado era falhar"
            except:
                print("✅ Clicou em 'Avançar', mas não houve redirecionamento — comportamento incorreto confirmado.")


except Exception as e:
        assert False, f"Erro no teste: {e}"

finally:
        driver.quit()