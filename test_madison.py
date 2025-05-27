from home_page import HomePage
from category_page import CategoryPage
from item_page import ItemPage
from time import sleep
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys






class TestMadison:

    # PRE CONDICIONES
    @classmethod
    def setup_method(cls):
        cls.fake = Faker('es_CO')
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://madison-island.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.home = HomePage(cls.driver)
        cls.category = CategoryPage(cls.driver)
        cls.item = ItemPage(cls.driver)

    def test_positive_purchase(self):
        self.home.assert_home_url()
        self.home.assert_home_title()
        self.home.click_on_section_by_index("1")
        self.category.click_button_next_page()
        self.category.click_on_item_by_name("ELIZABETH KNIT TOP")
        self.item.select_size_by_index(3)
        self.item.select_color_by_index(2)
        self.item.click_on_add_to_cart_button()

    def test_sold_out_item(self):
        self.home.assert_home_url()
        self.home.assert_home_title()
        self.home.click_on_section_by_index("1")
        self.category.click_button_next_page()
        self.category.click_on_item_by_name("ELIZABETH KNIT TOP")
        self.item.select_size_by_index(1)
        self.item.select_color_by_index(2)
        self.item.assert_sold_out_button()

    # POST CONDICIONES
    @classmethod
    def teardown_method(cls):
        sleep(2)
        cls.driver.quit()



# select_size = driver.find_element(By.ID, "SingleOptionSelector-0")
# select = Select(select_size)
# select.select_by_index(3)
#
# select_color = driver.find_element(By.ID, "SingleOptionSelector-1")
# select = Select(select_color)
# select.select_by_index(2)
#
# driver.find_element(By.XPATH, "//button[@name='add']").click()
#
# quantity_input = driver.find_element(By.XPATH, "//input[@name='updates[]']")
# quantity_input.clear()
# quantity_input.send_keys("3")
# quantity_input.send_keys(Keys.RETURN)
# driver.find_element(By.XPATH, "//input[@name='checkout']").click()
#
# driver.find_element(By.NAME, "email").send_keys(fake.email())
# select_country = driver.find_element(By.NAME, "countryCode")
# select = Select(select_country)
# select.select_by_visible_text("Colombia")
# driver.find_element(By.NAME, "firstName").send_keys(fake.first_name())
# driver.find_element(By.NAME, "lastName").send_keys(fake.last_name())
# driver.find_element(By.NAME, "address1").send_keys(fake.address())
# # driver.find_element(By.NAME, "address2").send_keys(fake.address_detail())
# driver.find_element(By.NAME, "city").send_keys(fake.city())
# driver.find_element(By.NAME, "city").send_keys(fake.city())
# select_province = driver.find_element(By.NAME, "zone")
# select = Select(select_province)
# select.select_by_visible_text("Cundinamarca")
# driver.find_element(By.NAME, "postalCode").send_keys(fake.city())
#
#
#
# sleep(2)
# driver.quit()