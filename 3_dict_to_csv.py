"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    my_list = [{'name': "Konstantin", 'age': 39, 'job': 'Programmer'},
        {'name': "Egor", 'age': 34, 'job': 'Project manager'},
        {'name': "Ivan", 'age': 35, 'job': 'Programmer'},
        {'name': "Oleg", 'age': 52, 'job': 'Programmer'}
    ]

    with open('coworkers.csv', 'w', encoding='utf-8') as my_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(my_file, fields, delimiter=';')
        writer.writeheader()
        for coworker in my_list:
            writer.writerow(coworker)  

if __name__ == "__main__":
    main()
