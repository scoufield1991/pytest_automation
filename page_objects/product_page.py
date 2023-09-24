from utilities.ui_utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __title_police_watch = (By.XPATH, '//h1[@class="section-title mb-5"]')
    __buy_one_click = (By.XPATH, '//a[contains(text(),"придбати в один кл")]')
    __phone_input = (By.XPATH, '//input[@class="author-input"]')
    __button_submit_buy = (By.XPATH, '//button[@class="comparison-product__button main-button comparison-buy"]')
    __button_offer_comments = (By.XPATH, '//a[@class="main-button trends-button feedback-button"]')
    __input_comment = (By.XPATH, '//textarea[@class="author-input"]')
    __input_fio = (By.XPATH, '//label[contains(text(),"П.І.Б.")]/following-sibling::input[@class="author-input"]')
    __input_phone_or_email = (By.XPATH, '//label[contains(text(),"тел./email")]'
                                        '/following-sibling::input[@class="author-input"]')
    __button_public_comment = (By.XPATH, '//button[@class="comparison-product__button main-button comparison-buy"]')
    __non_active_guarantees = (By.XPATH, '//a[@class="feedback-link watch-link watch-tabs__right"]')
    __active_delivery = (By.XPATH, '//a[@class="feedback-link watch-link watch-tabs__left active"]')
    __button_more_information = (By.XPATH, '//a[@class="feedback-link watch-link"]')
    __title_section_delivery = (By.XPATH, '//h1[@class="article-title section-title"]')
    __close_more_information = (By.XPATH, '//div[@class="close"]')
    __title_section_guarantees = (By.XPATH, '//div[@class="modal-inner right"]/div'
                                            '/h4[@class="section-title trends-title mb-5"]')
    __active_guarantees = (By.XPATH, '//a[@class="feedback-link watch-link watch-tabs__right active"]')
    __non_active_delivery = (By.XPATH, '//a[@class="feedback-link watch-link watch-tabs__left"]')
    __button_buy = (By.XPATH, '//div[@class="watch-desc d-flex justify-content-between mb-4"]'
                              '/following-sibling::div/button[@class="comparison-product__button main-button '
                              'comparison-buy p-0"]')
    __button_continue_buy = (By.XPATH, '//a/following-sibling::span[@class="feedback-link watch-link"]')
    __basket_button = (By.XPATH, '//a[contains(@href, "checkout/cart")]')
    __title_basket = (By.XPATH, '//h4[@class="article-title section-title basket-title"]')
    __icon_basket_count = (By.XPATH, '//span[@class="cart-icon__count"]')
    __title_product_in_basket = (By.XPATH, '//div[@class="basket-left__text"]/a[@class="basket-left__title"]')

    def is_display_title_watch(self):
        return self.is_element_displayed(self.__title_police_watch)

    def get_text_from_title(self):
        return self.get_text_element(self.__title_police_watch)

    def click_buy_one_click(self):
        self.click(self.__buy_one_click)
        return self

    def send_keys_your_phone(self):
        self.send_keys(self.__phone_input, '0936345824')

    def is_display_button_submit_buy(self):
        return self.get_text_element(self.__button_submit_buy)

    def click_offer_comments(self):
        self.click(self.__button_offer_comments)
        return self

    def send_keys_comment(self):
        self.send_keys(self.__input_comment, 'Hello_world')
        return self

    def send_keys_fio(self):
        self.send_keys(self.__input_comment, 'Kondrashev Yurii Oleksiyovich')
        return self

    def send_keys_email_or_phone(self):
        self.send_keys(self.__input_comment, 'scoufield@i.ua')
        return self

    def is_display_button_public_comment(self):
        return self.get_text_element(self.__button_public_comment)

    def click_on_more_information(self):
        self.click(self.__button_more_information)
        return self

    def get_text_from_title_delivery(self):
        return self.get_text_element(self.__title_section_delivery)

    def click_on_close_information(self):
        self.click(self.__close_more_information)
        return self

    def click_on_guarantees(self):
        self.click(self.__non_active_guarantees)
        return self

    def get_text_from_title_guarantees(self):
        return self.get_text_element(self.__title_section_guarantees)

    def is_active_delivery(self):
        return self.get_text_element(self.__active_delivery)

    def is_active_guarantees(self):
        return self.get_text_element(self.__active_guarantees)

    def click_button_buy(self):
        self.click(self.__button_buy)
        return self

    def click_button_continue_buy(self):
        self.click(self.__button_continue_buy)
        return self

    def open_basket(self):
        self.click(self.__basket_button)
        return self

    def get_text_from_title_basket(self):
        return self.get_text_element(self.__title_basket)

    def get_text_from_icon_count_basket(self):
        return self.get_text_element(self.__icon_basket_count)

    def get_text_from_title_product_in_basket(self):
        return self.get_text_element(self.__title_product_in_basket)
