from page_objects.home_page import HomePage
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_activate_filter_smartwatch(create_driver):
    """
    open site -> go to watches page -> activate filter smartwatch
    """
    driver = create_driver
    watches_page = HomePage(driver).move_to_watches_page()
    watches_page.activate_filter_smart()
    assert watches_page.is_display_activating_filter_smart(), 'Not display'


@pytest.mark.regression
def test_disable_filter_smartwatch(create_driver):
    """
    open site -> go to watches page -> activate smart watch -> disable filter
    """
    driver = create_driver
    watches_page = HomePage(driver).move_to_watches_page()
    watches_page.activate_filter_smart()
    watches_page.deactivate_filter_smart()
    assert watches_page.is_name_page_watches_displayed(), 'Not display name page'


@pytest.mark.regression
def test_disable_all_filters(create_driver):
    """
    open site -> go to watches page -> activate two filters -> press disable all
    """
    driver = create_driver
    watches_page = HomePage(driver).move_to_watches_page()
    watches_page.activate_filter_smart()
    assert watches_page.is_display_activating_filter_smart(), 'Not display'
    watches_page.activate_filter_woman()
    assert watches_page.is_display_activating_filter_smart_woman_filters(), 'Not display'
    watches_page.deactivate_all_filters()
    assert watches_page.is_name_page_watches_displayed(), 'Not display name page'


@pytest.mark.smoke
def test_open_page_through_hover_menu(create_driver):
    """
    open site -> go to watches page through the hover menu and choose one category
    """
    driver = create_driver
    watches_page = HomePage(driver).move_cursor_to_header_watches_page().click_on_watches_for_man()
    assert watches_page.is_display_activating_filter_man(), 'Not display'


@pytest.mark.regression
def test_disable_japan_country_filter(create_driver):
    """
    open site -> go to brands -> activate japan filter -> disable filter on watches page
    """
    driver = create_driver
    watches_page = HomePage(driver).scroll_click_on_brands().click_activate_sort_by_countries(). \
        click_on_japan_country().click_to_close_japan_filter()
    assert watches_page.is_name_page_watches_displayed(), 'Not display closing chosen filter'
