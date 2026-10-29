from datetime import datetime

from sqlalchemy import select

from app.database import SessionLocal
from app.models.trainer_availability import TrainerAvailability

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

def Schedule_view():
    pass


def Member_lookUp():
    pass
