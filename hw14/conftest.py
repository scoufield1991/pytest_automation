import pytest

from hw14.human import Human


@pytest.fixture()
def create_human():
    human = Human('Yurii', 25, 'male')
    yield human


@pytest.fixture()
def human_age_limit():
    age_limit = 100
    return age_limit


@pytest.fixture()
def valid_gender():
    gender = ["male", "female"]
    return gender


@pytest.fixture()
def create_human_with_custom_params():
    def __create_human(name: str, age: int, gender: str):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human
