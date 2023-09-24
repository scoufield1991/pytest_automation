from page_objects.home_page import HomePage
import pytest


@pytest.mark.smoke
def test_open_brands_page(create_driver):
    """
    open site->open brands page by footer menu
    """
    driver = create_driver
    brands_page = HomePage(driver).scroll_click_on_brands()
    assert brands_page.is_name_page_displayed(), 'Name page Brands is not displayed'


@pytest.mark.regression
def test_activating_sort_by_countries(create_driver):
    """
    open site->open brands page -> activate sort by countries
    """
    driver = create_driver
    brands_page = HomePage(driver).scroll_click_on_brands()
    brands_page.click_activate_sort_by_countries()
    assert brands_page.is_display_sort_by_countries(), 'Not display sorting'


@pytest.mark.regression
def test_activating_sort_by_swis_watches(create_driver):
    """
    open site->open brands page -> activate sorting by elite switzerland watches
    """
    driver = create_driver
    brands_page = HomePage(driver).scroll_click_on_brands()
    brands_page.click_activate_sort_by_switzerland_watches()
    assert brands_page.is_display_sort_by_switzerland_watches(), 'Not display sorting'


@pytest.mark.regression
def test_activating_sorting_by_japan_country(create_driver):
    """
    open site->open brands page -> activate sort by countries -> choose for example Japan
    """
    driver = create_driver
    brands_page = HomePage(driver).scroll_click_on_brands()
    brands_page.click_activate_sort_by_countries().click_on_japan_country()
    assert brands_page.is_name_japan_filter_displayed(), 'Not display sorting'


@pytest.mark.smoke
@pytest.mark.regression
def test_open_hide_all_collections(create_driver):
    """
    open site -> go to brand -> choose some brand, for example diesel -> open all collections -> hide all collections
    """
    driver = create_driver
    brands_page = HomePage(driver).scroll_click_on_brands()
    brands_page.click_on_diesel()
    assert brands_page.click_on_display_all_collections(), 'Not display'
    brands_page.click_on_hide_collections()
    assert brands_page.display_button_all_collection(), 'Not display'
