from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pytest
import allure
from config.settings import BASE_URL

@pytest.fixture(scope="session")
def browser():
    """Инициализация браузера для сессии."""
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()  # Закрытие браузера после выполнения всех тестов

@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на доступность главной страницы")
def test_page_accessible(browser):
    with allure.step("Отправка запроса на главную страницу"):
        response = requests.get(BASE_URL)
        assert response.status_code == 200, "Страница не открылась, статус отличается от 200"
    
    with allure.step("Открытие главной страницы в браузере"):
        browser.get(BASE_URL)

    with allure.step("Закрытие всплывающего окна"):
        try:
            close_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "popmechanic-close"))
            )
            close_button.click()
            print("Всплывающее окно закрыто.")
        except Exception as e:
            print(f"Всплывающее окно не найдено или не было закрыто: {e}")

    with allure.step("Закрытие уведомления о куки"):
        try:
            cookie_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cookie-notice__button"))
            )
            cookie_button.click()
            print("Уведомление о куки закрыто.")
        except Exception as e:
            print(f"Уведомление о куки не найдено или не было закрыто: {e}")

@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на открытие страницы информации о книге")
def test_open_book_page(browser):
    with allure.step("Открытие главной страницы"):
        browser.get(BASE_URL)

    with allure.step("Переход на страницу информации о книге"):
        try:
            book_element = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-picture__img"))
            )
            book_element.click()
            print("Переход на страницу информации о книге выполнен.")

            # Ожидание загрузки элемента на странице книги
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-detail"))
            )
        except Exception as e:
            print(f"Не удалось найти элемент книги для перехода на страницу информации: {e}")

@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на добавление книги в корзину")
def test_add_book_to_cart(browser):
    with allure.step("Нажатие на кнопку 'Купить'"):
        try:
            buy_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'product-offer-button') and contains(@class, 'chg-app-button--primary')]"))
            )
            buy_button.click()
            print("Кнопка 'Купить' нажата, книга добавлена в корзину.")

            # Ожидание подтверждения добавления книги в корзину
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "added-to-cart-confirmation"))
            )
        except Exception as e:
            print(f"Не удалось найти кнопку 'Купить' на странице книги: {e}")

@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на переход в корзину после добавления книги")
def test_go_to_cart(browser):
    with allure.step("Нажатие на иконку корзины"):
        try:
            cart_icon = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'sticky-header__controls-title') and text()='Корзина']"))
            )
            cart_icon.click()
            print("Переход в корзину выполнен.")

            # Ожидание загрузки страницы корзины
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart-content"))
            )
        except Exception as e:
            print(f"Не удалось найти иконку корзины для перехода: {e}")

@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на очистку корзины")
def test_clear_cart(browser):
    with allure.step("Нажатие на кнопку 'Очистить корзину'"):
        try:
            clear_cart_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "delete-many"))
            )
            clear_cart_button.click()
            print("Кнопка 'Очистить корзину' нажата, корзина очищена.")

            # Ожидание подтверждения очистки корзины
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "empty-cart-message"))
            )
        except Exception as e:
            print(f"Не удалось найти кнопку 'Очистить корзину': {e}")
