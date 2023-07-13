import pytest


def test_check_age(create_human):
    human = create_human
    human.grow()
    expected_age = 26
    assert human.age == expected_age, 'Age did not change'


def test_check_difference_age_after_grow(create_human_with_custom_params):
    human = create_human_with_custom_params('Olga', 19, 'female')
    start_age = human.age
    human.grow()
    after_year_age = human.age
    expected_difference = 1
    assert expected_difference == after_year_age - start_age, 'Difference did not change'


@pytest.mark.parametrize('age, status', [(98, 'alive'), (100, 'dead')])
def test_check_status(create_human, age, status):
    human = create_human
    human._Human__age = age
    human.grow()
    expected_status = status
    assert human._Human__status == expected_status, 'Status did not change'


def test_are_you_dead(create_human_with_custom_params):
    human = create_human_with_custom_params('Malik', 100, 'male')
    human.grow()
    with pytest.raises(Exception) as exc:
        human._Human__is_alive()
    assert str(exc.value) == f"{human._Human__name} is already dead..."


def test_are_you_alive(create_human_with_custom_params):
    human = create_human_with_custom_params('Malik', 88, 'male')
    human.grow()
    result = human._Human__is_alive()
    assert result is True, 'I am alive'


def test_human_change_gender_same_as_previous(create_human):
    human = create_human
    with pytest.raises(Exception) as exc:
        human.change_gender("male")
    assert str(exc.value) == "Yurii already has gender 'male'"


def test_human_change_on_invalid_gender(create_human):
    human = create_human
    with pytest.raises(Exception) as exc:
        human.change_gender("unknown")
    assert str(exc.value) == "Not correct name of gender"


def test_human_change_gender(create_human):
    human = create_human
    human.change_gender("female")
    expected_gender = "female"
    assert human.gender == expected_gender, 'Gender did not change'


def test_validate_gender(create_human_with_custom_params):
    human = create_human_with_custom_params('Malik', 88, 'other')
    with pytest.raises(Exception) as exc:
        human._Human__validate_gender(human.gender)
    assert str(exc.value) == "Not correct name of gender"


def test_custom_change_age(create_human_with_custom_params):
    human = create_human_with_custom_params('Malik', 88, 'male')
    human._Human__age = 33
    expected_age = human.age
    assert human.age == expected_age, 'Custom change for age works'
