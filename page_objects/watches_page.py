from page_objects.product_page import ProductPage
from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class WatchesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __name_page_watches = (By.XPATH, '//h1[@class="section-title mb-0" and contains(text(),"Годинники наручні")]')
    __filter_smart = (By.XPATH, '//div[@class="filter-checkbox"]/a[contains(@href,"smart-godynnyky")]')
    __filter_active_smart = (By.XPATH, '//h1[contains(text(),"Смарт годинники")]')
    __filter_deactivate_smart = (By.XPATH, '//li[@class="filter-sort__item"]/a[contains(text(),"Smart-годинники")]')
    __filter_woman = (By.XPATH, '//div[@class="filter-checkbox"]/a[contains(@href,"zhinochi")]')
    __active_smart_woman_filters = (By.XPATH, '//h1[contains(text(),"Смарт годинники жіночі")]')
    __button_deactivate_filters = (By.XPATH, '//a[contains(text(),"Очистити фільтри")]')
    __active_man_filter = (By.XPATH, '//h1[contains(text(),"Чоловічі годинники")]')
    __filter_by_accutime = (By.XPATH, '//div[@class="filter-checkbox"]/a[contains(@href,"accutime")]')
    __active_accutime_filter = (By.XPATH, '//h1[contains(text(),"Годинники Accutime")]')
    __watch_police = (By.XPATH,
                      '//a[contains(@href,"police-12896bs-02m-1.html") and @class="comparison-product__link"]')

    def is_name_page_watches_displayed(self):
        return self.is_element_displayed(self.__name_page_watches)

    def activate_filter_smart(self):
        self.click(self.__filter_smart)
        return self

    def is_display_activating_filter_smart(self):
        return self.is_element_displayed(self.__filter_active_smart)

    def deactivate_filter_smart(self):
        self.click(self.__filter_deactivate_smart)
        return self

    def activate_filter_woman(self):
        self.click(self.__filter_woman)
        return self

    def is_display_activating_filter_smart_woman_filters(self):
        return self.is_element_displayed(self.__active_smart_woman_filters)

    def deactivate_all_filters(self):
        self.click(self.__button_deactivate_filters)

    def is_display_activating_filter_man(self):
        return self.is_element_displayed(self.__active_man_filter)

    def activate_filter_accutime(self):
        self.click(self.__filter_by_accutime)
        return self

    def is_display_activating_filter_accutime(self):
        return self.is_element_displayed(self.__active_accutime_filter)

    def open_watch_police(self):
        self.click(self.__watch_police)
        return ProductPage(self._driver)








