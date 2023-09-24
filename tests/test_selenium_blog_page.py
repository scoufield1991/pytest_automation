from page_objects.home_page import HomePage
import pytest


@pytest.mark.smoke
def test_open_post(create_driver):
    """
    open site -> go to blogs -> open post
    """
    driver = create_driver
    blog_page = HomePage(driver).click_on_blogs()
    blog_page.click_on_article_aikon()
    assert blog_page.article_title_display(), 'Not element is displaying'


@pytest.mark.regression
def test_sort_by_history_tag(create_driver):
    """
    open site -> go to blogs -> make sort by history tag
    """
    driver = create_driver
    blog_page = HomePage(driver).click_on_blogs()
    blog_page.click_on_button_sort_by_history_watches()
    assert blog_page.activated_history_sort(), 'Not element is displaying'


@pytest.mark.regression
def test_sort_by_exclusive_hashtag(create_driver):
    """
    open site -> go to blogs -> make sort by exclusive hashtag
    """
    driver = create_driver
    blog_page = HomePage(driver).click_on_blogs()
    blog_page.activate_sort_by_exclusive_hashtag()
    assert blog_page.article_title_murakami_display(), 'Not element is display'


@pytest.mark.regression
def test_activate_deactivate_sort(create_driver):
    """
    open site -> go to blogs -> make sort -> disable sort
    """
    driver = create_driver
    blog_page = HomePage(driver).click_on_blogs()
    blog_page.click_on_button_sort_by_history_watches().click_on_activating_without_sort()
    assert blog_page.no_sorting_activated(), 'Not element is display'


@pytest.mark.smoke
def test_movement_by_content(create_driver):
    """
    open site -> go to blogs -> open post -> make some movement by content
    """
    driver = create_driver
    blog_page = HomePage(driver).click_on_blogs()
    blog_page.click_on_article_own_brand()
    assert blog_page.click_on_start_the_article(), 'Not element is display'
    assert blog_page.click_on_second_point(), 'Not element is display'
    assert blog_page.click_on_end_article(), 'Not element is display'
