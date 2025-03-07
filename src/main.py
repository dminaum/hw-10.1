from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_dataframes import read_csv, read_xlsx
from src.search_dataframes import sort_dataframes_by_desc, count_operations_by_category
from src.utils import load_transactions
from src.widget import get_date, mask_account_card, format_date

JSON_PATH = 'data/operations.json'
CSV_PATH = 'data/transactions.csv'
XLSX_PATH = 'data/transactions_excel.xlsx'


def main():
    extensions = ['JSON', 'CSV', 'XLSX']
    file_extension = input('''
Привет! Добро пожаловать в программу работы с банковскими транзакциями. 

Выберите необходимый пункт меню:

1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')

    if file_extension in ['1', '2', '3']:
        print(f'Для обработки выбран {extensions[int(file_extension) - 1]}-файл.')
        if file_extension == '1':
            result = load_transactions(JSON_PATH)
        elif file_extension == '2':
            result = read_csv(CSV_PATH)
        elif file_extension == '3':
            result = read_xlsx(XLSX_PATH)

        if result == []:  # Проверяем, не пустой ли список
            print("Ошибка: список транзакций пуст. Проверьте файл или формат данных.")
            return []

        while True:
            state = input('''
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
''')
            state = state.upper()
            if state in ['EXECUTED', 'CANCELED', 'PENDING']:
                result = filter_by_state(result, state)
                print(f'Операции отфильтрованы по статусу "{state.upper()}".')
                break
            else:
                print(f'Статус операции {state.upper()} недоступен.')
                continue

        is_sorted_by_date = input('Отсортировать операции по дате? Да/Нет ')
        if is_sorted_by_date.lower() == 'да':
            is_reversed = input('Отсортировать по возрастанию или по убыванию? ')
            if is_reversed.lower() == 'по возрастанию':
                result = sort_by_date(result, False)
            else:
                result = sort_by_date(result)
        is_rubles_only = input('Выводить только рублевые транзакции? Да/Нет ')
        if is_rubles_only.lower() == 'да':
            result = list(filter_by_currency(result, 'RUB'))

        is_sorted_by_key_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
        if is_sorted_by_key_word.lower() == 'да':
            key_word = input('По какому слову отфильтровать? ')
            result = sort_dataframes_by_desc(result, key_word)

        if result == []:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
            return
        print('Распечатываю итоговый список транзакций...')
        total_transactions = count_operations_by_category(result)
        print(f'Всего банковских операций в выборке: {len(result)}')
        for operation, amount in total_transactions.items():
            print(f"{operation.title()}: {amount}")
        for transaction in result:
            if transaction['from'] == 'Не указано' or transaction['from'] == '':
                print(f"""
{format_date(get_date(transaction['date']))} {transaction['description']}
{mask_account_card(transaction['to'])}
Сумма: {transaction['amount']} {transaction['currency_name']} 
""")
            else:
                print(f"""
{format_date(get_date(transaction['date']))} {transaction['description']}
{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}
Сумма: {transaction['amount']} {transaction['currency_name']} 
""")
    else:
        print('Вы ввели неверный пункт меню. Попробуйте снова')


if __name__ == '__main__':
    main()
