from page_objects.home_page import HomePage
import pytest


@pytest.mark.regression
def test_switch_language_site(create_driver):
    """
    open site -> change language to ru
    """
    driver = create_driver
    home_page = HomePage(driver).move()
    home_page.click_on_language()
    actual_text = home_page.get_text_from_brand()
    assert actual_text == "БРЕНДЫ"


@pytest.mark.smoke
def test_check_favorites(create_driver):
    """
    open site -> check favorites
    """
    driver = create_driver
    home_page = HomePage(driver).click_on_favorites()
    actual_text_name = home_page.get_text_from_favorites_name()
    actual_text_status = home_page.get_text_from_favorites_status()
    assert actual_text_name == "ОБРАНЕ"
    assert actual_text_status == "Обраного немає"


@pytest.mark.regression
@pytest.mark.smoke
def test_check_displaying_fields_authorization(create_driver):
    """
    open site -> go to profile -> check all elements is display on authorization form
    """
    driver = create_driver
    home_page = HomePage(driver).click_on_profile()
    assert home_page.phone_field_display(), 'Not element is displaying'
    assert home_page.password_field_display(), 'Not element is displaying'
    assert home_page.button_submit_display(), 'Not element is displaying'
    assert home_page.button_registration_display(), 'Not element is displaying'
    assert home_page.button_forgot_password_display(), 'Not element is displaying'


@pytest.mark.regression
@pytest.mark.smoke
def test_check_button_back(create_driver):
    """
    open site -> go to profile -> click on logo of the site -> check that you are on home page
    """
    driver = create_driver
    home_page = HomePage(driver).click_on_profile()
    home_page.click_on_element_to_back().check_trends_on_home_page()
    expected_url = 'https://deka.ua/'
    assert home_page.get_url() == expected_url, 'Actual URL  does not match the expected URL'


@pytest.mark.smoke
@pytest.mark.regression
def test_checking_finder(create_driver):
    """
    open site -> click find -> enter casio -> press enter
    """
    driver = create_driver
    home_page = HomePage(driver).set_value_for_find()
    assert home_page.is_display_finder_title(), 'Title does not display'
    actual_title_result = home_page.get_text_finder_title()
    assert actual_title_result.lower().__contains__('casio')
