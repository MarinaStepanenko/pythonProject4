[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Лицензия](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Простой и эффективный Python-модуль для фильтрации и сортировки списка банковских операций. Предназначен для анализа и организации данных о финансовых транзакциях.

---

## 📖 Содержание

1. [Цель проекта](#-цель-проекта)
2. [Ключевые функции](#-ключевые-функции)
3. [Тестирование](#-тестирование)
4. [Установка и использование](#-установка-и-использование)
5. [Зависимости](#-зависимости)
6. [Лицензия](#-лицензия)

---

## 🎯 Цель проекта

Цель проекта — предоставить базовые утилиты для работы с данными о банковских операциях, представленными в виде списка словарей. Модуль позволяет легко фильтровать операции по статусу выполнения и сортировать их по дате, что является частой задачей при анализе выписок или построении отчетов.

---

## ✨ Ключевые функции

### Модуль `processing`
- **`filter_by_state`**: Фильтрует список операций по статусу (например, показывать только выполненные операции)
- **`sort_by_date`**: Сортирует список операций по дате в порядке убывания или возрастания

### Модуль `generators`
- **`filter_by_currency(transactions, currency)`**: Возвращает итератор, который выдает транзакции с заданной валютой (например, "USD")
- **`transaction_descriptions(transactions)`**: Генератор, который возвращает описание каждой операции по очереди
- **`card_number_generator(start, end)`**: Генерирует номера банковских карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне

### Модуль `utils`
- **`get_operations(directory: str) -> list[dict]`**: Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список

**Файл с данными:** `data/operations.json` в корне проекта

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
## 🧪 Тестирование

Написаны комплексные тесты для всех функций, включая тесты с использованием `Mock` и `patch` для функций `get_operations` и `get_convertation`.

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
from src.external_api import get_convertation
```
## 📦 Зависимости

Проект требует следующие внешние зависимости:

- `requests` - для HTTP-запросов к API конвертации валют
- `python-dotenv` - для работы с переменными окружения из файла `.env`

**Установка зависимостей:**

```bash
pip install requests python-dotenv
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