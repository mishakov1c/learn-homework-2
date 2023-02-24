"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as temp_file:
        content = temp_file.read()
        string_length = len(content)
        print(f'Длина получившейся строки: {string_length}.')
        print(f'Количество слов в тексте: {len(content.split())}.')
        new_content = content.replace('.', '!')
        
        with open('referat2.txt', 'w', encoding='utf-8') as new_file:
            new_file.write(new_content)
            new_file.close()

if __name__ == "__main__":
    main()
