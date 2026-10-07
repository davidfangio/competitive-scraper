from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.monitor import analisar_preco
from app.alerts import processar_alerta

from app.models import Product
from app.database import salvar_produto, salvar_historico, buscar_ultimo_preco, buscar_preco_anterior


def coletar_produtos():
    driver = webdriver.Chrome()

    driver.get("https://books.toscrape.com/")

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    produtos = soup.find_all("article", class_="product_pod")

    produtos_extraidos = []

    for produto in produtos:
        nome = produto.find("h3").find("a")["title"]
        preco = float(
            produto.find("p", class_="price_color")
            .get_text()
            .replace("£", "")
        )
        url = urljoin(
            "https://books.toscrape.com/",
            produto.find("h3").find("a")["href"]
        )

        dados = {
            "nome": nome,
            "preco": preco,
            "url": url
        }

        produto_db = Product(
            name=dados["nome"],
            url=dados["url"]
        )

        produto_id = salvar_produto(produto_db)
        preco_anterior = buscar_ultimo_preco(produto_id)

        if preco_anterior:
            resultado = analisar_preco(
                float(preco_anterior.price),
                dados["preco"]
            )

            alerta = processar_alerta(resultado, dados["nome"])

            if alerta:
                print(alerta)

        salvar_historico(produto_id, dados["preco"])

        produtos_extraidos.append(dados)

    driver.quit()

    return produtos_extraidos


if __name__ == "__main__":
    produtos_extraidos = coletar_produtos()