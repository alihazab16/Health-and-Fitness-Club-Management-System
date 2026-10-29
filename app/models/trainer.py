from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Trainer(Base):
    __tablename__ = "trainer"

    trainer_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    # Add the remaining Trainer columns
    # based on your team's ERD