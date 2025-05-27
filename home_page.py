from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_section_by_index(self, index):
        self.driver.find_element(By.XPATH, f"//ul[@class='grid grid--uniform']/li[{index}]").click()

    def assert_home_url(self):
        assert "madison-island" in self.driver.current_url

    def assert_home_title(self):
        assert "madison-island" in self.driver.title
