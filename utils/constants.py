from enum import StrEnum


class ROLE(StrEnum):
    TEACHER = "teacher"
    STUDENT = "student"


class ATTENDANCE_STATUS(StrEnum):
    PRESENT = "present"
    ABSENT = "absent"
