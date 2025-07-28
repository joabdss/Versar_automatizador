# Versar_automatizador

Este projeto trata-se de um software de teste automatizado para a aplicação WEB Versar plataforma socioemocional.

## Tecnologias utilizadas

- Python 3.13
- Selenium
- Pytest
- Html/Css/JS

## Instalação 

1. Clone o repositório:
     git clone https://github.com/joabdss/Versar_automatizador

2. Instale as dependências:
     pip install -r requirements.txt

## Execução 

- Para rodar o teste:
    pytest

- Para abrir o relatorio html
    Clicar com o direito "Reveal in File Explorer" > Abrirá a pasta (Versar_Automatizador) > relatorio.html
		
OBSERVAÇÃO: Para gerar o relatório "html" foi utilizado o seguinte comando: 
   		 pytest testes/T_versar.py --html=relatorio.html --self-contained-html
