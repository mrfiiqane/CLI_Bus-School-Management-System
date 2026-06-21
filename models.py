from dataclasses import dataclass


@dataclass
class Student:
    id: int
    fullname: str
    gender: str
    student_class: str
    parent_name: str
    parent_phone: str
    fee: float
    driver: str


@dataclass
class Driver:
    id: int
    fullname: str
    phone: str
    license_number: str
    salary: float


@dataclass
class Bus:
    id: int
    bus_number: str
    capacity: int
    driver: str