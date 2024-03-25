import os
import random
from pathlib import Path

import pytest

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
faker_en = Faker("En")


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 100),
        salary=random.randint(15000, 400000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generate_file():
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../upload_data'))
    Path(current_dir).mkdir(parents=True, exist_ok=True)
    path = os.path.join(current_dir, f'filetest_{random.randint(1, 999)}.txt')
    temp_file_name = ''
    with open(path, "w+") as temp_file:
        temp_file.write(f'Hello World{random.randint(0, 999)}')
        temp_file_name = temp_file.name
    return temp_file_name, path
