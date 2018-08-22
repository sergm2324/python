# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def createdir(name):  # функция создания директории в текущей папке
    import os
    dir_path = os.path.join(os.getcwd(), name)
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    except PermissionError:
        print('Вы не ввели имя папки')
    else:
        print('Успешно создано')

if __name__ == "__main__":
    i = 0
    while i < 9:
        i = i + 1
        my_dir = ('dir_' + str(i))
        createdir(my_dir)


def removedir(name):  # функция удаления директории в текущей папке
    import os
    dir_path = os.path.join(os.getcwd(), name)
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такой директории не существует')
    except PermissionError:
        print('Вы не ввели имя папки')
    else:
        print('Успешно удалено')

if __name__ == "__main__":
    i = 0
    while i < 9:
        i = i + 1
        my_dir = ('dir_' + str(i))
        removedir(my_dir)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def reflectdir():  # отображает только папки текущей директории
    import os
    for file in os.scandir(path=os.getcwd()):
        if file.is_dir():
            print(file)

if __name__ == "__main__":
    reflectdir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyfile():
    import shutil
    import os
    file = os.path.realpath(__file__)
    file1 = file + '.dupl'
    shutil.copy(file, file1)

if __name__ == "__main__":
    copyfile()
