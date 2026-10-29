from datetime import datetime
from sqlalchemy import(
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
)

from sqlalchemy.orm import Mapped,mapped_column

from database import Base


class TrainerAvailability(Base):
    __tablename__ = "trainer_availability"
    availability_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    trainer_id: Mapped[int] = mapped_column(
        ForeignKey("trainer.trainer_id"),
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    end_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            "start_time < end_time",
            name="check_valid_availability_times"
        ),
    )