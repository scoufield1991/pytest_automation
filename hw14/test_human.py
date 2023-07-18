import pytest

from hw14.human import Human


def test_check_age(create_human):
    human = create_human
    human.grow()
    expected_age = human.age
    assert human.age == expected_age, 'Age did not change'


def test_check_difference_age_after_grow(create_human_with_custom_params):
    human = create_human_with_custom_params('Olga', 19, 'female')
    start_age = human.age
    human.grow()
    after_year_age = human.age
    expected_difference = 1
    assert expected_difference == after_year_age - start_age, 'Difference did not change'


def test_are_you_dead(create_human_with_custom_params):
    name = 'Malik'
    human = create_human_with_custom_params(name, 101, 'male')
    human.grow()
    with pytest.raises(Exception, match=f"{name} is already dead...") as exc:
        human.grow()
    assert str(exc.value) == f"{name} is already dead..."


def test_are_you_alive(create_human, human_age_limit):
    human = create_human
    human.grow()
    result = human.age < human_age_limit
    assert result is True, 'I am alive'


def test_human_change_gender_same_as_previous(create_human):
    human = create_human
    with pytest.raises(Exception, match="Yurii already has gender 'male'") as exc:
        human.change_gender("male")
    assert str(exc.value) == "Yurii already has gender 'male'"


def test_human_change_on_invalid_gender(create_human):
    human = create_human
    with pytest.raises(Exception, match="Not correct name of gender") as exc:
        human.change_gender("unknown")
    assert str(exc.value) == "Not correct name of gender"


def test_human_change_gender(create_human):
    human = create_human
    expected_gender = "female"
    human.change_gender(expected_gender)
    assert human.gender == expected_gender, 'Gender did not change'


def test_validate_gender(create_human_with_custom_params, valid_gender):
    human = create_human_with_custom_params('Malik', 88, 'other')
    assert human.gender not in valid_gender, 'Not valid gender did not works'


def test_validate_gender_method_is_private():
    method_name = '_Human__validate_gender'
    method = getattr(Human, method_name, None)
    assert method.__name__ == '__validate_gender'
    assert method.__class__.__name__ == 'function'


def test_validate_is_alive_method_is_private():
    method_name = '_Human__is_alive'
    method = getattr(Human, method_name, None)
    assert method.__name__ == '__is_alive'
    assert method.__class__.__name__ == 'function'
