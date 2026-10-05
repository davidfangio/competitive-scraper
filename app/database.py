from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///competitive_scraper.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def salvar_produto(produto):
    from app.models import Product

    session = get_session()

    produto_existente = (
        session.query(Product)
        .filter_by(url=produto.url)
        .first()
    )

    if produto_existente:
        produto_id = produto_existente.id
        session.close()
        return produto_id

    session.add(produto)
    session.commit()

    produto_id = produto.id

    session.close()

    return produto_id

def salvar_historico(produto_id, preco):
    from app.models import PriceHistory

    session = get_session()

    historico = PriceHistory(
        product_id=produto_id,
        price=preco,
        collected_at=datetime.now()
    )

    session.add(historico)
    session.commit()

    session.close()


class Base(DeclarativeBase):
    pass

import app.models

Base.metadata.create_all(engine)

def buscar_ultimo_preco(produto_id):
    from app.models import PriceHistory

    session = get_session()

    historico = (
        session.query(PriceHistory)
        .filter_by(product_id=produto_id)
        .order_by(PriceHistory.collected_at.desc())
        .first()
    )

    session.close()

    return historico

def buscar_preco_anterior(produto_id):
    from app.models import PriceHistory

    session = get_session()

    historicos = (
        session.query(PriceHistory)
        .filter_by(product_id=produto_id)
        .order_by(PriceHistory.collected_at.desc())
        .offset(1)
        .first()
    )

    session.close()

    return historicos
