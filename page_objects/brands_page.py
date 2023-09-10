from selenium.webdriver.common.by import By
from page_objects.watches_page import WatchesPage
from utilities.ui_utilities.base_page import BasePage


class BrandPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __name_page = (By.XPATH, '//h1[@class="text-center" and contains(text(),"Бренди годинників")]')
    __by_countries_none_active = (By.XPATH, '//div[@class="brands__btn"]')
    __by_countries_active = (By.XPATH, '//div[@class="brands__btn active"]')
    __by_japan_country = (By.XPATH, '//div[2]/div[@class="country__column-wrapper search-anchor__J"]'
                                    '/a[@class="country__title"]/span')
    __name_by_japan_filter = (By.XPATH, '//h1[@class="section-title mb-0" and contains(text(),"Японські годинники")]')
    __close_japan_filter = (By.XPATH, '//span[@class="filter-sort__close"]')
    __sort_by_switzerland_watches_none_active = (By.XPATH, '//div[@class="brands__switch-country"]')
    __sort_by_switzerland_watches_active = (By.XPATH, '//div[@class="brands__switch-country active-country"]')
    __brand_diesel = (By.XPATH, '//a[contains(@href,"diesel")]')
    __display_all_collection = (By.XPATH,
                                '//input[@class="main-button trends-button" and @value="Показати всі колекції"]')
    __hide_all_collection = (By.XPATH, '//input[@class="main-button trends-button" and @value="Приховати"]')

    def is_name_page_displayed(self):
        return self.is_element_displayed(self.__name_page)

    def click_activate_sort_by_countries(self):
        self.click(self.__by_countries_none_active)
        return self

    def is_display_sort_by_countries(self):
        return self.is_element_displayed(self.__by_countries_active)

    def click_activate_sort_by_switzerland_watches(self):
        self.click(self.__sort_by_switzerland_watches_none_active)
        return self

    def is_display_sort_by_switzerland_watches(self):
        return self.is_element_displayed(self.__sort_by_switzerland_watches_active)

    def click_on_japan_country(self):
        self.click(self.__by_japan_country)
        return self

    def is_name_japan_filter_displayed(self):
        return self.is_element_displayed(self.__name_by_japan_filter)

    def click_to_close_japan_filter(self):
        self.click(self.__close_japan_filter)
        return WatchesPage(self._driver)

    def click_on_diesel(self):
        self.click(self.__brand_diesel)
        return self

    def click_on_display_all_collections(self):
        self.click(self.__display_all_collection)
        return self.is_element_displayed(self.__hide_all_collection)

    def click_on_hide_collections(self):
        self.click(self.__hide_all_collection)
        return self

    def display_button_all_collection(self):
        return self.is_element_displayed(self.__display_all_collection)
