from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from travel_agency.db.models.base import Base

class Tour(Base):
    __tablename__ = "tours"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    destination: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    duration_days: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
