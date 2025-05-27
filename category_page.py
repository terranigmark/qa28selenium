from selenium.webdriver.common.by import By


class CategoryPage:

    def __init__(self, driver):
        self.driver = driver

    def click_button_next_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".pagination li:nth-of-type(3)").click()

    def click_button_previous_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".pagination li:nth-of-type(1)").click()

    def click_on_item_by_name(self, item_name):
        self.driver.find_element(By.LINK_TEXT, item_name).click()