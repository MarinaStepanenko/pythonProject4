# Приложение на Python для обработки банковских операций

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Лицензия](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Простой и эффективный Python-модуль для фильтрации и сортировки списка банковских операций. Предназначен для анализа и организации данных о финансовых транзакциях.

---

## 📖 Содержание

1.  [Цель проекта](#-цель-проекта)
2.  [Ключевые функции](#-ключевые-функции)
3.  [Тестирование](#-тестирование)
4.  [Установка и использование](#-установка-и-использование)
5.  [Зависимости](#-зависимости)
6.  [Лицензия](#-лицензия)

---

## 🎯 Цель проекта

Цель проекта — предоставить базовые утилиты для работы с данными о банковских операциях, представленными в виде списка словарей. Модуль позволяет легко фильтровать операции по статусу выполнения и сортировать их по дате, что является частой задачей при анализе выписок или построении отчетов.

---

## ✨ Ключевые функции

### Модуль `processing`
*   **`filter_by_state`**: Фильтрует список операций по статусу (например, показывать только выполненные операции).
*   **`sort_by_date`**: Сортирует список операций по дате в порядке убывания или возрастания.

### Модуль `generators`
*   **`filter_by_currency(transactions, currency)`**: Возвращает итератор, который выдает транзакции с заданной валютой (например, "USD").
*   **`transaction_descriptions(transactions)`**: Генератор, который возвращает описание каждой операции по очереди.
*   **`card_number_generator(start, end)`**: Генерирует номера банковских карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

**Примеры использования:**
```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация по валюте
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Получение описаний операций
descriptions = transaction_descriptions(transactions)
for _ in range(3):
    print(next(descriptions))

# Генерация номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)
```
## 🧪 Тестирование
**Запуск тестов**:

bash
pytest

### Запуск тестов с покрытием:
```
bash
pytest --cov
```

## ⚙️ Установка и использование

Склонируйте или скачайте проект и поместите директорию src в путь к вашему проекту.

Импортируйте функции из модулей в ваш скрипт:
```
python
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
```
## 📦 Зависимости
Проект написан на чистом Python и не требует внешних зависимостей, кроме стандартной библиотеки.

Python 3.7+

## 📄 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.