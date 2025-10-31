from src.processing import filter_by_state, sort_by_date
from src.read_csv import read_csv_trans
from src.read_excel_trans import read_excel_trans
from src.utils import filter_data_file, get_operations, process_bank_search
from src.widget import get_date, mask_account_card


def main() -> None:
    my_dict: list[dict] | str = []
    while True:
        result = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Пользователь: """)
        if result == "1":
            print("Для обработки выбран JSON-файл.")
            my_dict = get_operations("data/operations.json")
            break
        elif result == "2":
            print("Для обработки выбран CSV-файл.")
            my_dict = read_csv_trans("transactions.csv")
            break
        else:
            print("Для обработки выбран XLSX-файл.")
            my_dict = read_excel_trans("transactions_excel.xlsx")
            break
    print(my_dict)
    filtered_trans = []
    while True:
        result_2 = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Пользователь: """)
        if result_2.lower() == "executed":
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            filtered_trans = filter_by_state(my_dict, state="EXECUTED")
            break
        elif result_2.lower() == "canceled":
            print("Операции отфильтрованы по статусу 'CANCELED'")
            filtered_trans = filter_by_state(my_dict, "CANCELED")
            break
        elif result_2.lower() == "pending":
            print("Операции отфильтрованы по статусу 'PENDING'")
            filtered_trans = filter_by_state(my_dict, "PENDING")
            break
        else:
            print(f"Статус операции {result_2} недоступен.")
    filt_by_date = filtered_trans
    print(filt_by_date)
    while True:
        result_3 = input(
            """Отсортировать операции по дате? Да/Нет

Пользователь: """
        )
        if result_3.lower() == "да":
            while True:
                result_4 = input("Отсортировать по возрастанию или по убыванию? ")
                if result_4.lower() == "по возрастанию":
                    filt_by_date = sort_by_date(filtered_trans, reverse=False)
                    print(filt_by_date)
                    break

                elif result_4.lower() == "по убыванию":
                    filt_by_date = sort_by_date(filtered_trans, reverse=True)
                    break
            break
        elif result_3.lower() == "нет":
            break
    rub_trans = filter_data_file(filt_by_date)
    print(rub_trans)
    rub_trans_new = []
    while True:
        result_5 = input(
            """Выводить только рублевые транзакции? Да/Нет

Пользователь: """
        )
        if result_5.lower() == "да":
            for transaction in rub_trans:
                if transaction.get("currency_code") == "RUB" or transaction.get("currency_name") == "Ruble":
                    rub_trans_new.append(transaction)
            print(rub_trans_new)
            break
        elif result_5.lower() == "нет":
            rub_trans_new = rub_trans
            break
    final_trans = rub_trans_new
    while True:
        result_6 = input(
            """Отфильтровать список транзакций по определенному слову в описании? Да/Нет

Пользователь: """
        )
        if result_6.lower() == "да":
            search_string = input("Введите слово: ")
            final = process_bank_search(final_trans, search_string)
            print(final)
            break
        elif result_6.lower() == "нет":
            final = final_trans
            break
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(final)}")
    for trans in final:
        date = trans.get("date")
        to = trans.get("to")
        description = trans.get("description")
        currency = trans.get("currency_name")
        amount = trans.get("amount")
        print(f"{get_date(date)} {description}\n" f"{mask_account_card(to)}\n" f"Сумма: {amount} {currency}.\n")
