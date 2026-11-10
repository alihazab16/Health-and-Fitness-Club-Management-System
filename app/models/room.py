from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Room(Base):
    __tablename__ = "Room"

    room_id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    capacity : Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    room_name : Mapped[int] = mapped_column(
        String(100),
        nullable=False
    )