from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# _______Алгоритм действий________
#    1. Зайти на главную страницу
#    3. Заполнить поле Username
#    4. Заполнить поле Password
#    5. Нажать на кнопку Login

# URL страницы, на которой надо проверить логин и пароль
URL = 'https://www.saucedemo.com/' 

# Валидные данные 
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


# Эта функция возвращает объект драйвера Selenium Chrome,
# настроенного для безголового режима (без открытия окна браузера).
# Он также устанавливает размер окна браузера в 1920x800 пикселей 
# и неявное ожидание в 10 секунд.
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.implicitly_wait(10)
    return driver

# Функция открывает указанный url в браузере
def open_page(driver, url):
    driver.get(url)


# Функция поиска элемента по указанному атрибуту id 
def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

# Функция, которая нажимает на найденный элемент 
def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

# Функция, которая отправляет указанный текст 
def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

# Функция, которая заполняет поля name, password и кликает на кнопку Login
def login(driver, name, password):
    element_send_keys(driver, 'user-name', name)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'login-button')


driver = get_driver()
open_page(driver, URL)
login(driver=driver, name=LOGIN, password=PASSWORD)

driver.quit()