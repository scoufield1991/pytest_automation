from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __article_aikon = (By.XPATH, '//a[starts-with(@href, "/ua/articles/noviy-godinnik-aikon-skeleton-urban")]'
                                 '/span[contains (text(), "AIKON Skeleton Urban Tribe")]')
    __article_title = (By.XPATH, '//h1[@class="blog-article-page__heading"]'
                                 '/span[contains (text(), "AIKON Skeleton Urban Tribe")]')
    __button_history = (By.XPATH, '//button[@class="blog-tag-button blog-tags-list__tag"]'
                                  '/span[contains (text(), "Історія годинників")]')
    __history_activated_sort = (By.XPATH,
                                '//button[@class="blog-tag-button blog-tags-list__tag blog-tag-button--active"]')
    __hashtag_exclusive = (By.XPATH, '//span[contains (text(), "ЕКСКЛЮЗИВ")]'
                                     '/ancestor::button[@class="blog-article__hashtag-button"]')
    __article_title_murakami = (By.XPATH, '//a[@class="blog-article__title"]'
                                          '/span[contains (text(), "MP-15 Takashi Murakami")]')
    __button_all_articles = (By.XPATH, '//button[@class="blog-tag-button blog-tags-list__tag"]'
                                       '/span[contains (text(), "Всі")]')
    __button_all_activated_no_sorting = \
        (By.XPATH, '//button[@class="blog-tag-button blog-tags-list__tag blog-tag-button--active"]'
                   '/span[contains (text(), "Всі")]')
    __article_title_own_brand = (By.XPATH, '//span[contains (text(), "Андре Мартінес")]'
                                           '/ancestor::a[@class="blog-article__title"]')
    __button_start_article = (By.XPATH, '//span[contains (text(), "1.Пролог")]/ancestor::button')
    __element_start_article = (By.XPATH, '//h2[@id="пролог"]')
    __button_second_point_article = (By.XPATH, '//span[contains (text(), "2.Мініатюрне мистецтво")]/ancestor::button')
    __element_second_point_article = (By.XPATH, '//h2[@id="мініатюрнемистецтво"]')
    __button_go_to_end_article = (By.XPATH, '//span[contains (text(), "3.Ключові дані")]/ancestor::button')
    __element_end_article = (By.XPATH, '//h2[@id="ключовіданітаціна"]')

    def click_on_article_aikon(self):
        self.click(self.__article_aikon)
        return self

    def article_title_display(self):
        return self.is_element_displayed(self.__article_title)

    def click_on_button_sort_by_history_watches(self):
        self.click(self.__button_history)
        return self

    def activated_history_sort(self):
        return self.is_element_displayed(self.__history_activated_sort)

    def activate_sort_by_exclusive_hashtag(self):
        self.click(self.__hashtag_exclusive)
        return self

    def article_title_murakami_display(self):
        self.scroll(self.__article_title_murakami)
        return self.is_element_displayed(self.__article_title_murakami)

    def click_on_activating_without_sort(self):
        self.click(self.__button_all_articles)
        return self

    def no_sorting_activated(self):
        return self.is_element_displayed(self.__history_activated_sort)

    def click_on_article_own_brand(self):
        self.click(self.__article_title_own_brand)
        return self

    def click_on_start_the_article(self):
        self.click(self.__button_start_article)
        return self.is_element_displayed(self.__element_start_article)

    def click_on_second_point(self):
        self.click(self.__button_second_point_article)
        return self.is_element_displayed(self.__element_second_point_article)

    def click_on_end_article(self):
        self.click(self.__button_go_to_end_article)
        return self.is_element_displayed(self.__element_end_article)
