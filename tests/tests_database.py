from app.database import get_session
from app.models import Product
from app.models import Product, PriceHistory
from datetime import datetime

session = get_session()

produto = Product(
    name="Livro de Teste",
    url="https://exemplo.com/livro"
)

session.add(produto)
session.commit()

historico = PriceHistory(
    product_id=produto.id,
    price=12.99,
    collected_at=datetime.now()
)

session.add(historico)
session.commit()

historicos = session.query(PriceHistory).all()

for historico in historicos:
    print(
        historico.id,
        historico.product_id,
        historico.price,
        historico.collected_at
    )

produtos = session.query(Product).all()

for produto in produtos:
    print(produto.id, produto.name, produto.url)

session.close()

print("Produto salvo com sucesso!")