from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String, unique=True)


class PriceHistory(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    collected_at: Mapped[datetime] = mapped_column(DateTime)