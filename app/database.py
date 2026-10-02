from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///competitive_scraper.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def salvar_produto(produto):
    session = get_session()

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


