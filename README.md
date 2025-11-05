[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Лицензия](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Простой и эффективный Python-модуль для фильтрации и сортировки списка банковских операций. Предназначен для анализа и организации данных о финансовых транзакциях.

---

## 📖 Содержание

1. [Цель проекта](#-цель-проекта)
2. [Ключевые функции](#-ключевые-функции)
3. [Декораторы](#декораторы)
4. [Дополнительные модули](#модули)
5. [Тестирование](#-тестирование)
6. [Установка и использование](#-установка-и-использование)
7. [Зависимости](#-зависимости)
8. [Лицензия](#-лицензия)

---

## 🎯 Цель проекта

Цель проекта — предоставить базовые утилиты для работы с данными о банковских операциях, представленными в виде списка словарей. Модуль позволяет легко фильтровать операции по статусу выполнения и сортировать их по дате, что является частой задачей при анализе выписок или построении отчетов.

---

## ✨ Ключевые функции

### Модуль `main`
- **`main`**: Отвечает за основную логику проекта и связывает функциональности между собой.

### Модуль `processing`
- **`filter_by_state`**: Фильтрует список операций по статусу (например, показывать только выполненные операции)
- **`sort_by_date`**: Сортирует список операций по дате в порядке убывания или возрастания

### Модуль `generators`
- **`filter_by_currency(transactions, currency)`**: Возвращает итератор, который выдает транзакции с заданной валютой (например, "USD")
- **`transaction_descriptions(transactions)`**: Генератор, который возвращает описание каждой операции по очереди
- **`card_number_generator(start, end)`**: Генерирует номера банковских карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне

## 🔧 Декораторы
### Модуль decorators
log(filename=None): Декоратор для автоматического логирования выполнения функций.

### Особенности:

Логирует время вызова, имя функции, аргументы и результат выполнения

При ошибках записывает тип исключения и входные параметры

Поддерживает запись логов как в файл, так и в консоль

Пример использования:
```
python
from src.decorators import log

@log(filename="operations.log")
def process_transaction(amount, currency):
    return f"Processed {amount} {currency}"

@log()
def risky_operation(x, y):
    return x / y

# Успешное выполнение - запись в файл
process_transaction(100, "USD")

# Ошибка - вывод в консоль
risky_operation(10, 0)
Формат логов:

Успешное выполнение: имя_функции ok

Ошибка: имя_функции error: тип_ошибки. Inputs: (аргументы)
```
## Дополнительные модули
### Модуль `utils`
- **`get_operations(directory: str) -> list[dict]`**: Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список

**Файл с данными:** `data/operations.json` в корне проекта
- **`process_bank_search(data: list[dict], search_string: str) -> list[dict]:`** Принимает список словарей с данными о банковских операциях и строку поиска, возвращает список словарей,
    у которых в описании есть данная строка.
    в каждой категории. Категории операций хранятся в поле description
- **`process_bank_operations(data: list[dict], categories: list) -> dict:`** Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
- **`filter_data_file(data: list[dict]) -> list[dict]:`** Функция, которая приводит список словарей к единому виду
### Модуль `external_api`
- **`get_convertation(transaction: list[dict]) -> float`**: Принимает на вход транзакцию и возвращает сумму транзакции (`amount`) в рублях. Если транзакция была в `USD` или `EUR`, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли. Используется [Exchange Rates Data API](https://apilayer.com/exchangerates_data-api)

**Примеры использования:**

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.utils import get_operations
from src.external_api import get_convertation

# Загрузка операций из файла
operations = get_operations("data/operations.json")

# Конвертация сумм операций в рубли
total_in_rub = get_convertation(operations)

# Фильтрация по валюте
usd_transactions = filter_by_currency(operations, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Получение описаний операций
descriptions = transaction_descriptions(operations)
for _ in range(3):
    print(next(descriptions))

# Генерация номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)
```
### Модуль `read_csv.py`
- **`read_csv(filename: str) -> list[dict]`**  - функция для прочтения Csv файла, которая возвращает список словарей с транзакциями.Используется совместно с декоратором `find_file_decorator(func)`: находит путь к файлу.
**Файл с данными:** `transactions.csv` в папке `data` в корне проекта.
### Модуль `read_excel_trans.py`
- **`read_excel_trans(filename: str) -> list[dict])`** - функция для прочтения excel файла, возвращает список словарей с транзакциями. Используется совместно с декоратором `find_file_decorator(func)`.
**Файл с данными:** `transactions_excel.xlsx` в папке `data` в корне проекта.
## 🧪 Тестирование

Написаны комплексные тесты для всех функций, включая тесты с использованием `Mock` и `patch` для функций `get_operations` и `get_convertation`, `read_csv` и `read_excel_trans`.

**Запуск тестов:**
```
bash
pytest
```
**Запуск тестов с покрытием:**
```
bash
pytest --cov
```
**Тестирование декораторов:**
```
- Проверка логирования в консоль с использованием capsys

- Тестирование записи логов в файл

- Проверка обработки успешных выполнений и исключений
```
## ⚙️ Установка и использование

Склонируйте или скачайте проект и поместите директорию `src` в путь к вашему проекту.

Создайте файл `.env` на основе шаблона и добавьте ваш API-ключ:

```env
API_KEY=your_exchange_rates_api_key_here
```
Импортируйте функции из модулей в ваш скрипт:

```python
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.utils import get_operations
from src.decorators import log
from src.external_api import get_convertation
```
## 📦 Зависимости

Проект требует следующие внешние зависимости:

- `requests` - для HTTP-запросов к API конвертации валют
- `python-dotenv` - для работы с переменными окружения из файла `.env`
- `pandas` - для работы с файлами формата сsv и excel.

**Установка зависимостей:**

```bash
pip install requests python-dotenv
pip install pandas 
Python 3.7+
```
## 🔧 Конфигурация

Для работы функции конвертации валют необходимо:

1. Получить API-ключ на [apilayer.com](https://apilayer.com/marketplace/exchangerates_data-api)
2. Создать файл `.env` в корне проекта
3. Добавить в файл `.env` ваш API-ключ:

```text
API_KEY=ваш_ключ_здесь
```
**ВНИМАНИЕ:** Файл `.env` добавлен в `.gitignore` для защиты чувствительных данных. Не коммитьте реальные API-ключи в репозиторий.

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.