## Описание проекта: Chitai Gorod UI и API тесты

## Общее описание
Проект "Chitai Gorod" представляет собой набор автоматизированных тестов для проверки функциональности веб-приложения интернет-магазина книг, реализованных с использованием Selenium и pytest. Целью данного проекта является обеспечение качества программного обеспечения за счет выполнения как пользовательских интерфейсных (UI) тестов, так и тестов на уровне API. Для визуализации отчетов применяется Allure.

## [Тест план](https://fe-bug-report.atlassian.net/wiki/x/AQBwAg) 

## Шаги
1. Склонировать проект: 'git clone https://github.com/Evgenii-Firtsikov/chitai_gorod_ui_api_pytest.git'
2. Установить все зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report

## Структура проекта
```
chitai_gorod_ui_api_tests/
├── test/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ui.py
├── run_tests.py
├── requirements.txt
├──.gitignore
└── config/
    └── settings.py
```
- **test/**: Директория, содержащая тестовые файлы. Включает:
  - **test_api.py**: Тесты для проверки функциональности API, таких как получение информации о книгах, добавление книг в корзину и проверка состояния корзины.
  - **test_ui.py**: Тесты для проверки пользовательского интерфейса, включая проверку доступности страницы, взаимодействие с элементами на странице, добавление книг в корзину через UI и очистку корзины.
- **run_tests.py**: Скрипт для запуска тестов, поддерживающий три режима: выполнение только UI-тестов, только API-тестов или всех тестов одновременно.
- **requirements.txt**: Список зависимостей проекта
- **config/**: Директория для хранения конфигурационных файлов, в которой находится settings.py, содержащий настройки окружения (URL, пути к файлам, тестовые данные).

## Тесты API (test_api.py)
- **test_get_token**: Описание: Получение токена доступа из cookies.
- **headers (fixture)**: Описание: Фикстура для заголовков с токеном авторизации.
- **test_main_page_accessible**: Описание: Проверка доступности главной страницы (ожидается статус 200).
- **test_book_info_api**: Описание: Проверка получения информации о книге по её slug (ожидается статус 200).
- **test_add_book_to_cart**: Описание: Проверка добавления книги в корзину (ожидается статус 200).
- **test_view_cart**: Описание: Проверка доступа к корзине (ожидается статус 200).
- **test_clear_cart**: Описание: Проверка очистки корзины (ожидается статус 204).

## Тесты UI (test_ui.py)
- **browser (fixture)**: Описание: Инициализация браузера.
- **test_page_accessible**: Описание: Тест на доступность страницы, с проверкой закрытия всплывающего окна и уведомления о куки.
- **test_open_book_page**: Описание: Тест на открытие страницы информации о книге.
- **test_add_book_to_cart**: Описание: Тест на добавление книги в корзину с кнопкой 'Купить'.
- **test_go_to_cart**: Описание: Тест на переход в корзину после добавления книги.
- **test_increase_book_quantity**: Описание: Тест на увеличение количества копий книги в корзине.
- **test_clear_cart**: Описание: Тест на очистку корзины.

## Технические детали
- **Язык программирования**: Python
- **Библиотеки**:
  - **requests**: для выполнения HTTP-запросов к API.
  - **selenium**: для автоматизации взаимодействия с веб-приложением через браузер.
  - **webdriver-manager**: для автоматической загрузки и управления драйверами браузеров.
  - **pytest**: для организации и запуска тестов, а также для формирования отчетов.
  - **allure**: для генерации отчета.

## Запуск тестов
Для запуска тестов используется скрипт `run_tests.py`, который позволяет выбирать режим запуска:
- Только UI-тесты: `python run_tests.py ui`
- Только API-тесты: `python run_tests.py api`
- Все тесты: `python run_tests.py`

## Полезные ссылки
- [Подсказка по markdown](https://fe-bug-report.atlassian.net/wiki/x/AQBwAg) 
- [Генератор файлов .gitignore ](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)



