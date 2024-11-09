from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey
from app.db.models.base import Base

class Booking(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True)
    tour_id: Mapped[int] = mapped_column(ForeignKey("tours.id"))
    customer_name: Mapped[str] = mapped_column()
    customer_email: Mapped[str] = mapped_column()
    seats: Mapped[int] = mapped_column()
