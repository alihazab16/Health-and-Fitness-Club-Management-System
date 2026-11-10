from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class PTSession(Base):

    __tablename__ = "PTSession"

    session_id : Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True
    )
        # Foreign key connecting to Member
    member_id: Mapped[int] = mapped_column(
        ForeignKey("member.member_id"),
        nullable=False
    )

        # Foreign key connecting to Trainer
    trainer_id: Mapped[int] = mapped_column(
        ForeignKey("trainer.trainer_id"),
        nullable=False
    )

        # Foreign key connecting to Room
    room_id: Mapped[int] = mapped_column(
        ForeignKey("room.room_id"),
        nullable=False
    )

    start_time : Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False
    )

    end_time : Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False
    )

    status : Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

        # Ensure the session ends after it starts
    __table_args__ = (
        CheckConstraint(
            "start_time < end_time",
            name="check_valid_session_times"
        ),
    )
