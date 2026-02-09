# Проект автоматизации тестирования

## Описание проекта
Проект содержит автоматизированные тесты для:
- Калькулятора с задержкой выполнения операций
- Интернет-магазина (полный цикл покупки)

## Структура проекта
lesson_10/
├── pages/ # Page Object классы
├── tests/ # Тесты
├── allure-results/ # Результаты Allure (не коммитить)
├── allure-report/ # Отчеты Allure (не коммитить)
├── pytest.ini # Конфигурация pytest
├── requirements.txt # Зависимости
└── README.md # Документация


## Установка и запуск

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
2. Запуск тестов с генерацией Allure отчетов
# Запуск всех тестов
pytest tests/ --alluredir=allure-results

# Запуск конкретного теста
pytest tests/test_calculator.py --alluredir=allure-results
pytest tests/test_store.py --alluredir=allure-results

# Параллельный запуск тестов
pytest tests/ -n 2 --alluredir=allure-results
3. Просмотр отчета Allure
Способ 1: Генерация HTML отчета
# Установка Allure командной строки (требуется Java)
# Скачать с https://github.com/allure-framework/allure2/releases

# Генерация отчета
allure generate allure-results -o allure-report --clean

# Открытие отчета в браузере
allure open allure-report
Способ 2: Использование Allure сервера
# Запуск сервера для просмотра отчетов
allure serve allure-results
Особенности проекта
Документация кода
Все методы классов содержат документацию с типами параметров и возвращаемых значений
Использованы type hints для улучшения читаемости кода
Добавлены подробные docstrings
Allure отчеты
Разметка шагов тестов с помощью @allure.step
Группировка тестов по функциональностям (@allure.feature)
Приоритетность тестов (@allure.severity)
Подробные описания тестов (@allure.description)
Поддерживаемые браузеры
Chrome
Firefox
Примечания
Папки allure-results и allure-report добавлены в .gitignore
Для работы с Allure требуется установка Java
Тесты настроены для работы с удаленными сервисами

## Ключевые улучшения:

1. **Полная документация кода** - добавлены type hints и docstrings ко всем методам
2. **Интеграция Allure** - разметка шагов, проверок, названий и описаний тестов
3. **Структурированный код** - добавлен базовый класс BasePage для избежания дублирования
4. **Профессиональная документация** - подробный README с инструкциями по запуску
5. **Конфигурационные файлы** - pytest.ini и requirements.txt для удобства работы