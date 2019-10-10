__author__ = "Гончаров Всеволод Сергеевич"

import os
import shutil


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print("Каталог {}\\{} создан".format(os.getcwd(), dir_name))
    except FileExistsError:
        print("Каталог {}\\{} уже существует".format(os.getcwd(), dir_name))


def delete_dir(dir_name):
    if dir_exist(dir_name):
        os.rmdir(dir_name)
        print("Каталог {}\\{} удален".format(os.getcwd(), dir_name))
    else:
        print("Каталог {}\\{} не существует".format(os.getcwd(), dir_name))


def dir_exist(dir_name):
    return os.path.exists(os.path.join(os.getcwd(), dir_name))


def dir_list():
    print("Каталог {} содержит:".format(os.getcwd(), ))
    for item in os.listdir():
        print(item)


def copy_file(obj, target):
    shutil.copy(obj, target)


def main():
    while True:
        print("Введи номер задачи (1-3) или 0 для выхода")
        key = int(input())
        # Задача-1:
        # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
        # из которой запущен данный скрипт.
        # И второй скрипт, удаляющий эти папки.

        if key == 1:
            while True:
                print("Запустить скрипт на создание директорий - 1. Запустить скрипт на удаление директорий - 2. "
                      "Выход - 0")
                local_key = int(input())
                if local_key == 1:
                    for idx, _ in enumerate(range(9), start=1):
                        create_dir("dir_{}".format(idx))
                elif local_key == 2:
                    for idx, _ in enumerate(range(9), start=1):
                        delete_dir("dir_{}".format(idx))
                elif local_key == 0:
                    break
                else:
                    print("Ввёл что-то не то, попробуй ещё.")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

        elif key == 2:
            dir_list()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

        elif key == 3:
            copy_file(os.path.join(os.getcwd(), "hw05_easy.py"), os.path.join(os.getcwd(), "hw05_easy_copy.py"))

        elif key == 0:
            break

        else:
            print("Ввел что то не то, попробуй ещё раз")


if __name__ == "__main__":
    main()
