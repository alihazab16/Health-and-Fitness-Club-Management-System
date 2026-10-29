
from datetime import datetime

from app.trainer import set_availability


# First slot
print(set_availability(
    1,
    datetime(2026, 11, 2, 9, 0),
    datetime(2026, 11, 2, 11, 0)
))

# Overlapping slot
print(set_availability(
    1,
    datetime(2026, 11, 2, 10, 0),
    datetime(2026, 11, 2, 12, 0)
))

# Invalid slot
print(set_availability(
    1,
    datetime(2026, 11, 2, 14, 0),
    datetime(2026, 11, 2, 13, 0)
))
