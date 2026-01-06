from enum import Enum

class DayOfWeeks(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(DayOfWeeks.MONDAY.value)
print(DayOfWeeks.MONDAY.name)
print(DayOfWeeks(3))
print(DayOfWeeks(3).name)