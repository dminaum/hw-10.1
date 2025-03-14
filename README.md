# Проект: Обработка банковских транзакций

## Описание
Данный проект представляет собой инструмент для загрузки, обработки и анализа банковских транзакций из различных источников (JSON, CSV, XLSX). Он позволяет фильтровать, сортировать и анализировать транзакции, а также производить их маскирование и конвертацию валют.

## Функциональность
- Загрузка транзакций из файлов JSON, CSV и XLSX
- Фильтрация по статусу (EXECUTED, CANCELED, PENDING)
- Сортировка по дате (по возрастанию или убыванию)
- Фильтрация по валюте (например, только рублевые транзакции)
- Фильтрация по ключевому слову в описании
- Подсчет количества операций по категориям
- Маскирование номеров карт и счетов
- Логирование выполнения операций
- Конвертация валют с использованием внешнего API

## Основные функции, зашитые в main.py
- Программа позволяет принимать данные о банковских операциях в форматах JSON, CSV и XLSX
- После загрузки данных, пользователь может отфильтровать операции по статусу, валюте платежа, времени и описанию
- После выбора параметров для фильтрации, программа отдает подходящие операции в виде строк.
- Эти строки содержат дату платежа, замаскированные счета прихода/ухода, а так же общее количество платежей по той или иной категории

## Установка и запуск
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/your-repository.git
   ```
2. Перейдите в директорию проекта:
   ```sh
   cd your-repository
   ```
3. Установите зависимости с помощью Poetry:
   ```sh
   poetry install
   ```
4. Запустите программу:
   ```sh
   python -m src.main
   ```

## Структура проекта
```
📂 project_root
├── 📂 data               # Директория с файлами JSON, CSV, XLSX
├── 📂 src                # Исходный код
│   ├── 📜 decorators.py        # Декораторы для логирования
│   ├── 📜 external_api         # Перевод валют по актуальному курсу с помощью API
│   ├── 📜 generators.py        # Генераторы. Фильтр транзакций по валюте или описанию
│   ├── 📜 main.py              # Точка входа в приложение
│   ├── 📜 masks.py             # Маскирование номеров карт и счетов
│   ├── 📜 processing.py        # Фильтр по статусу и дате транзакции
│   ├── 📜 read_dataframes.py   # Превращение датафрейма .XLSX/.CSV в список со словарями
│   ├── 📜 search_dataframes.py # Фильтр и счет словарей по описанию
│   ├── 📜 utils.py             # Загрузка файла формата .JSON, перевод валюты в рубли на основе external_api
│   ├── 📜 widget.py            # Функции схватывания и редактирования даты и времени транзакций
├── 📜 pyproject.toml     # Файл зависимостей Poetry
└── 📜 README.md          # Описание проекта
```

## Примеры работы
```sh
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
```
Пользователь: 1
```sh
Программа: Для обработки выбран JSON-файл.
```
```sh
Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
```
Пользователь: EXECUTED

Программа: Операции отфильтрованы по статусу "EXECUTED"

В случае, если пользователь ввел неверный статус, программа не падает в ошибку.

Пользователь: test
```sh
Программа: Статус операции "test" недоступен.
```
```sh
Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
```
После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:
```sh
Программа: Отсортировать операции по дате? Да/Нет
```
Пользователь: да
```sh
Программа: Отсортировать по возрастанию или по убыванию? 
```
Пользователь: по возрастанию/по убыванию
```sh
Программа: Выводить только рублевые тразакции? Да/Нет
```
Пользователь: да
```sh
Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет
```
Пользователь: да/нет
```sh
Программа: Распечатываю итоговый список транзакций...

Программа: 
Всего банковских операций в выборке: 4

08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR
```
```sh
Если выборка оказалась пустой, программа выводит сообщение:

Программа: Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации
```
## Контакты
Разработчик: Дмитрий Наумов

_README был написан с помощью Chat-GPT_

