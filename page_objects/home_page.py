from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_objects.blog_page import BlogPage
from page_objects.brands_page import BrandPage
from page_objects.watches_page import WatchesPage
from utilities.ui_utilities.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # __lang = (By.XPATH, '//*/header/div/div/div/div/div[@class="shop-info__dopdown-wrapper row"]/' \
    #                     'div[@class="shop-info__dopdown d-flex align-items-center lang-switch"]')
    __lang = (By.CSS_SELECTOR, 'div.shop-info__dopdown-wrapper.row > '
                               'div.shop-info__dopdown.d-flex.align-items-center.lang-switch')
    __name_brand_ru = (By.XPATH,
                       '//div[@class="menu-links__item menu-links__item-title"]/a[contains (text(), "Бренды")]')
    __ru_lang = (By.XPATH, '//div/a[@class="lang__list-link btn"]')
    __favorites_element = (By.XPATH, '//div[@class="favorite-icon"]')
    __favorites_name = (By.XPATH, '//h4[@class="article-title section-title"]')
    __favorites_status = (By.XPATH, '//section[@class="filter comparison favorite"]/'
                                    'div/div[@class="row"]/following-sibling::div/div[@class="col-12"]')
    __brands_element = (By.XPATH, '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]'
                                  '/a[starts-with(@href, "/ua/b")]')
    __profile_element = (By.XPATH, '//div[@class="header__tooltip-wrapper"]/a[starts-with(@href,"/ua/authorization/")]')
    __phone_input = (By.XPATH, '//input[@placeholder="Телефон"]')
    __password_input = (By.XPATH, '//input[@placeholder="Пароль"]')
    __button_submit = (By.XPATH, '//button[@type="submit"]')
    __button_registration = (By.XPATH, '//a[contains (text(), "Зареєструватися")]')
    __button_forgot_password = (By.XPATH, '//a[contains (text(), "Забув пароль")]')
    __element_to_back = (By.XPATH, '//a[@class="nuxt-link-exact-active nuxt-link-active"]')
    __home_page_trends = (By.XPATH, '//div[contains (text(), "Зараз в тренді")]')
    __finder_element = (By.XPATH, '//input[@class="header-nav__input"]')
    __result_of_find_title = (By.XPATH, '//h1[@class="search-title"]')
    __blog_element = (By.XPATH, '//div[@class="footer-links__list-wrapper"]/a[starts-with(@href, "/ua/artic")]')
    __watches_page_element = (By.XPATH, '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]'
                                        '/a[contains(text(),"Годинники")]')
    __header_move_to_watches_page = (By.XPATH,
                                     '//div[@class="menu-links__item menu-links__item-title"]'
                                     '/a[contains(@href, "/ua/naruchnyy-godynnyk/")]')
    __watches_for_man = (By.XPATH, '//a[contains(@href, "cholovichi")]')

    def move(self):
        self.move_to_element(self.__lang)
        return self

    def click_on_language(self):
        self.click(self.__ru_lang)

    def get_text_from_brand(self):
        return self.get_text_element(self.__name_brand_ru)

    def click_on_favorites(self):
        self.click(self.__favorites_element)
        return self

    def get_text_from_favorites_name(self):
        return self.get_text_element(self.__favorites_name)

    def get_text_from_favorites_status(self):
        return self.get_text_element(self.__favorites_status)

    def scroll_click_on_brands(self):
        self.scroll(self.__brands_element)
        self.click(self.__brands_element)
        return BrandPage(self._driver)

    def click_on_profile(self):
        self.click(self.__profile_element)
        return self

    def phone_field_display(self):
        return self.is_element_displayed(self.__phone_input)

    def password_field_display(self):
        return self.is_element_displayed(self.__password_input)

    def button_submit_display(self):
        return self.is_element_displayed(self.__button_submit)

    def button_registration_display(self):
        return self.is_element_displayed(self.__button_registration)

    def button_forgot_password_display(self):
        return self.is_element_displayed(self.__button_forgot_password)

    def click_on_element_to_back(self):
        self.click(self.__element_to_back)
        return self

    def get_current_url(self):
        return self.get_url()

    def check_trends_on_home_page(self):
        self.scroll(self.__home_page_trends)
        return self.is_element_displayed(self.__home_page_trends)

    def set_value_for_find(self):
        self.click(self.__finder_element)
        self.send_keys(self.__finder_element, 'casio')
        self.send_keys(self.__finder_element, Keys.ENTER)
        return self

    def clear_value_for_find(self):
        self.clear(self.__finder_element)
        return self

    def get_text_finder_title(self):
        return self.get_text_element(self.__result_of_find_title)

    def is_display_finder_title(self):
        return self.is_element_displayed(self.__result_of_find_title)

    def click_on_blogs(self):
        self.scroll(self.__blog_element)
        self.click(self.__blog_element)
        return BlogPage(self._driver)

    def move_to_watches_page(self):
        self.scroll(self.__watches_page_element)
        self.click(self.__watches_page_element)
        return WatchesPage(self._driver)

    def move_cursor_to_header_watches_page(self):
        self.move_to_element(self.__header_move_to_watches_page)
        return self

    def click_on_watches_for_man(self):
        self.click(self.__watches_for_man)
        return WatchesPage(self._driver)
