from datetime import datetime

from sqlalchemy import select

from app.database import SessionLocal
from app.models.trainer_availability import TrainerAvailability
from app.models.PTSession import PTSession

def set_availability(
    trainer_id: int,
    start_time: datetime,
    end_time: datetime
) -> str:

    #Validate time range
    if start_time >= end_time:
        return "Error: start time must be before end time"

    with SessionLocal() as db:

        #Check for overlapping slot
        conflict = db.scalar(
            select(TrainerAvailability.availability_id).where(
                TrainerAvailability.trainer_id == trainer_id,
                TrainerAvailability.start_time < end_time,
                TrainerAvailability.end_time > start_time
            ).limit(1)
        )

        if conflict is not None:
            return "Error: this availability overlaps an existing slot"

        #Create new availability record
        availablility = TrainerAvailability(
            trainer_id = trainer_id,
            start_time= start_time,
            end_time=end_time
        )

        db.add(availablility)

        # Save the record in PostgreSQL
        db.commit()

        return "Availability saved successfully."

def view_schedule(trainer_id: int) -> list[PTSession]:

    with SessionLocal() as db:

        # Find all sessions belonging to this trainer
        sessions = db.scalars(
            select(PTSession)
            .where(PTSession.trainer_id == trainer_id)
            .order_by(PTSession.start_time)
        ).all()

        return list(sessions)


def Member_lookUp():
    pass
