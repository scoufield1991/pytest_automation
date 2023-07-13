import pytest

from hw14.human import Human


@pytest.fixture()
def create_human():
    human = Human('Yurii', 25, 'male')
    yield human


@pytest.fixture()
def create_human_with_custom_params():
    def __create_human(name, age, gender):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human
