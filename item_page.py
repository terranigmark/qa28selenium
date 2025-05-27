from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ItemPage:

    def __init__(self, driver):
        self.driver = driver

    def select_size_by_index(self, index):
        select_size = self.driver.find_element(By.ID, "SingleOptionSelector-0")
        select = Select(select_size)
        select.select_by_index(index)

    def select_color_by_index(self, index):
        select_color = self.driver.find_element(By.ID, "SingleOptionSelector-1")
        select = Select(select_color)
        select.select_by_index(index)

    def click_on_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, "//button[@name='add']").click()

    def assert_sold_out_button(self):
        add_to_cart_button = self.driver.find_element(By.ID, "AddToCart-product-template")
        add_button_text = add_to_cart_button.text
        assert "SOLD OUT" in add_button_text, f"El boton de sold out contiene el texto: {add_button_text}"