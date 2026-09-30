from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def coletar_produtos():
    driver = webdriver.Chrome()

    driver.get("https://books.toscrape.com/")

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    produtos = soup.find_all("article", class_="product_pod")

    produtos_extraidos = []

    for produto in produtos:
        nome = produto.find("h3").find("a")["title"]
        preco = float(produto.find("p", class_="price_color").get_text().replace("£", ""))
        url = urljoin("https://books.toscrape.com/", produto.find("h3").find("a")["href"])

        dados = {
            "nome": nome,
            "preco": preco,
            "url": url
        }

        produtos_extraidos.append(dados)

    driver.quit()
    
    return produtos_extraidos

produtos_extraidos = coletar_produtos()