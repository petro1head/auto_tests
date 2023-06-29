
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element_by_id(self, locator):
        return self.driver.find_element(By.ID, locator)

    def element_click(self, locator):
        element = self.get_element_by_id(locator)
        element.click()

    def element_send_keys(self, locator, text):
        element = self.get_element_by_id(locator)
        element.send_keys(text)

    def login(self, name, password):
        self.element_send_keys('user-name', name)
        self.element_send_keys('password', password)
        self.element_click('login-button')

# URL страницы, на которой надо проверить логин и пароль
URL = 'https://www.saucedemo.com/'

# Валидные данные
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# Создаем объект драйвера
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,800")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=chrome_options)
driver.implicitly_wait(10)

# Создаем объект страницы входа
login_page = LoginPage(driver)

# Открываем страницу
login_page.open_page(URL)

# Выполняем вход
login_page.login(LOGIN, PASSWORD)

# Закрываем драйвер
driver.quit()