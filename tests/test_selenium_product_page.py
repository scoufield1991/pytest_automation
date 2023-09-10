from page_objects.home_page import HomePage
import pytest


@pytest.mark.smoke
def test_open_product(create_driver):
    """
    open site -> go to watches_page -> open product -> check name
    """
    driver = create_driver
    product_page = HomePage(driver).move_to_watches_page().activate_filter_accutime().open_watch_police()
    assert product_page.is_display_title_watch(), 'Not display'
    actual_text = product_page.get_text_from_title().lower()
    assert actual_text.__contains__('police')


@pytest.mark.regression
def test_check_buy_one_click(create_driver):
    """
    open site -> go to watches_page -> open product -> click on buy one click -> enter number telephone
    """
    driver = create_driver
    product_page = HomePage(driver).move_to_watches_page().activate_filter_accutime().open_watch_police()
    product_page.click_buy_one_click().send_keys_your_phone()
    assert product_page.is_display_button_submit_buy(), 'Not display button, incorrect phone enter'


@pytest.mark.regression
def test_check_enter_comment(create_driver):
    """
    open page -> go to watches_page -> open product -> click on live a comment -> enter all fields
    """
    driver = create_driver
    product_page = HomePage(driver).move_to_watches_page().activate_filter_accutime() \
        .open_watch_police().click_offer_comments().send_keys_comment().send_keys_fio().send_keys_email_or_phone()
    assert product_page.is_display_button_public_comment(), 'Not display button'


@pytest.mark.smoke
def test_check_delivery_and_guarantees(create_driver):
    """
    open site -> go to watches_page -> open product -> click on delivery -> click on guarantees
    """
    driver = create_driver
    product_page = HomePage(driver).move_to_watches_page().activate_filter_accutime().open_watch_police()
    assert product_page.is_active_delivery(), 'Not active delivery'
    product_page.click_on_more_information()
    actual_text_delivery = product_page.get_text_from_title_delivery()
    assert actual_text_delivery == "СПОСОБИ ОПЛАТИ ТА ДОСТАВКИ ГОДИННИКІВ"
    product_page.click_on_close_information().click_on_guarantees()
    assert product_page.is_active_guarantees(), 'Not active guarantees'
    product_page.click_on_more_information()
    actual_text_guarantees = product_page.get_text_from_title_guarantees()
    assert actual_text_guarantees == "УМОВИ ГАРАНТІЙНОГО ОБСЛУГОВУВАННЯ."
    product_page.click_on_close_information()


@pytest.mark.smoke
@pytest.mark.regression
def test_add_product_to_basket(create_driver):
    """
    open site -> go to watches_page -> open product -> click on buy -> check the basket
    """
    driver = create_driver
    product_page = HomePage(driver).move_to_watches_page().activate_filter_accutime().open_watch_police() \
        .click_button_buy().click_button_continue_buy()
    assert product_page.get_text_from_icon_count_basket() == "1"
    product_page.open_basket()
    assert product_page.get_text_from_title_basket() == "КОШИК"
    assert product_page.get_text_from_title_product_in_basket() == "ACCUTIME"
