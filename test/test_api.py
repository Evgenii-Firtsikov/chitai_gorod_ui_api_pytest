import requests
from config.settings import BASE_URL, BOOK_API_URL, CART_API_URL, VIEW_CART_URL
import pytest
import allure

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Получение токена доступа из cookies")
@allure.step("Получение токена доступа")
def test_get_token():
    with allure.step("Отправка запроса на главную страницу для получения cookies"):
        response = requests.get(BASE_URL)
    
    with allure.step("Извлечение токена из cookies"):
        cookies = response.cookies
        token = cookies.get('access-token')
        if token:
            return token[9:]  # Извлекаем токен, начиная с 9 символа
        else:
            raise ValueError("Не удалось получить токен доступа")

@pytest.fixture
def headers():
    """Фикстура для заголовков с токеном авторизации."""
    with allure.step("Получение заголовков с токеном авторизации"):
        token = test_get_token()
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': BASE_URL,
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        return headers

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Проверка доступности главной страницы (ожидается статус 200)")
def test_main_page_accessible():
    with allure.step("Отправка запроса на главную страницу"):
        response = requests.get(BASE_URL)
    
    with allure.step("Проверка, что статус код равен 200"):
        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Проверка получения информации о книге по её slug (ожидается статус 200)")
def test_book_info_api(headers):
    book_slug = "sem-smertnyh-grehov-tom-10-the-seven-deadly-sins-manga-3063236"
    
    with allure.step(f"Отправка запроса на получение информации о книге с slug {book_slug}"):
        response = requests.get(f"{BOOK_API_URL}{book_slug}", headers=headers)
    
    with allure.step("Проверка, что статус код равен 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"
    
    with allure.step("Проверка, что в ответе присутствует поле 'title'"):
        data = response.json().get("data", {})
        assert "title" in data, "Отсутствует поле 'title' в ответе"
        print(f"Информация о книге: {data}")

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Проверка добавления книги в корзину (ожидается статус 200)")
def test_add_book_to_cart(headers):
    book_id = 3063236
    payload = {"id": book_id}
    
    with allure.step("Отправка запроса на добавление книги в корзину"):
        response = requests.post(CART_API_URL, headers=headers, json=payload)
    
    with allure.step("Проверка, что статус код равен 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"
    
    with allure.step("Проверка, что ответ содержит подтверждение добавления книги"):
        if response.text.strip():
            try:
                response_data = response.json()
                assert "id" in response_data, "Отсутствует подтверждение добавления в корзину"
                print(f"Книга с ID {book_id} успешно добавлена в корзину.")
            except requests.exceptions.JSONDecodeError:
                print("Ответ сервера не в формате JSON, но операция прошла успешно.")
        else:
            print("Ответ сервера пустой, но операция прошла успешно.")

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Проверка доступа к корзине (ожидается статус 200)")
def test_view_cart(headers):
    with allure.step("Отправка запроса на получение содержимого корзины"):
        response = requests.get(VIEW_CART_URL, headers=headers)
    
    with allure.step("Проверка, что статус код равен 200"):
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, но получен {response.status_code}"
    
    with allure.step("Парсинг и вывод содержимого корзины"):
        if response.text.strip():
            try:
                cart_data = response.json()
                print(f"Содержимое корзины: {cart_data}")
            except requests.exceptions.JSONDecodeError:
                print("Ответ сервера не в формате JSON, но корзина доступна.")
        else:
            print("Ответ сервера пустой, но корзина доступна.")

@allure.severity("critical")
@allure.feature("API тесты")
@allure.title("Проверка очистки корзины (ожидается статус 204)")
def test_clear_cart(headers):
    with allure.step("Отправка запроса на очистку корзины"):
        response = requests.delete(VIEW_CART_URL, headers=headers)
    
    with allure.step("Проверка, что статус код равен 204"):
        assert response.status_code == 204, f"Ошибка: ожидался статус 204, но получен {response.status_code}"
    
    with allure.step("Проверка, что корзина была успешно очищена"):
        response = requests.get(VIEW_CART_URL, headers=headers)
        cart_data = response.json().get("products", [])
        assert len(cart_data) == 0, "Корзина не была очищена"
        print("Корзина успешно очищена.")
