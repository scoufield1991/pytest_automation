url = 'https://deka.ua/'

# footer_of_the_site
catalog_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]/div[@class="title"]'
catalog_css = '.footer-links__wrapper.footer-links__wrapper_catalog .title'
brands_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]/a[starts-with(@href, "/ua/b")]'
brands_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href^="/ua/b"]'
watches_xpath ='//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]/a[contains(text(),"Годинники")]'
watches_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href$="naruchnyy-godynnyk/"]'
top_watches_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]' \
                    '/a[contains(@href,":elitni-godynnyky/")]'
top_watches_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href$=":elitni-godynnyky/"]'
jewerly_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]' \
                '/a[contains(@href,"yuvelirni-vyroby")]'
jewerly_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href*="yuvelirni-vyroby"]'
accessories_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]/a[contains(@href,"aksesuary")]'
accessories_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href*="aksesuary"]'
discounts_xpath = '//div[@class="footer-links__wrapper footer-links__wrapper_catalog"]/a[contains(@href,"discounts")]'
discounts_css = '.footer-links__wrapper.footer-links__wrapper_catalog a[href*="discounts"]'
for_clients_xpath = '//div[@class="footer-links__wrapper footer-links_client"]/div[@class="title"]'
for_clients_css = '.footer-links__wrapper.footer-links_client .title'
payment_delivery_xpath = '//div[@class="footer-links__list-wrapper"]/a[contains(@href,"paymentanddelivery")]'
payment_delivery_css = '.footer-links__wrapper.footer-links_client a[href*="paymentanddelivery"]'
information_logo_xpath = '//div[@class="information__logo"]/img[@alt="logo"]'
information_logo_css = '.information__logo > img'

# brands_page
sort_by_brand = '//div[@class="brands__btn active"]'
sort_by_country = '//div[@class="brands__btn"]'
name_page = '//h1[@class="text-center" and contains(text(),"Бренди годинників")]'
go_to_main_page = '//div/a[@class="breadcrumbs__item nuxt-link-active"]'
brand_list = '//div[@class="brands-list"]'
select_all_brands = '//div[@class="brands__switch-country active-country"]'
select_switzerland_watches = '//div[@class="brands__switch-country"]'

# watches_page
name_watches_page = '//h1[@class="section-title mb-0" and contains(text(),"Годинники наручні")]'
count_of_watches = '//h1/following-sibling::span[@class="filter-title__number"]'
sorting_by_top_sales = '//a[contains(@href,"sort:lidery-prodazhu")]'
sort_by_discounts = '//a[contains(@href,"sort:znyzhki")]'
sort_by_rate = '//a[contains(@href,"sort:reytynhu") and contains(text(), "по рейтингу")]'
sort_by_new_comes = '//a[contains(@href,"sort:novynky") and contains(text(), "новинки")]'
sort_by_low_price = '//a[contains(@href,"sort:deshevshe")]'
sort_by_high_price = '//li/a[contains(@href,"sort:dorozhche")]'
filter_by_category = '//span[@class="filter-box__name" and contains (text(), "Категорія")]'
open_close_check_box_category = '//span[contains (text(), "Категорія")]/following-sibling::span'
filter_by_sex = '//span[@class="filter-box__name" and contains (text(), "Стать")]'
open_close_check_box_sex = '//span[contains (text(), "Стать")]/following-sibling::span'
checkbox_by_female = '//*[@id="sex0"]'
checkbox_by_male = '//*[@id="sex2"]'
check_box_by_unisex = '//*[@id="sex1"]'


