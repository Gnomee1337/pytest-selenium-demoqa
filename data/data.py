from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str
    current_address: str
    permanent_address: str
    phone_number: str

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield value
