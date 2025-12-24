from enum import StrEnum


class ROLE(StrEnum):
    TEACHER = "teacher"
    STUDENT = "student"


class REQUEST_STATUS(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
