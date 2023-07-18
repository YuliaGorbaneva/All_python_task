# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def OpenFile(file): #открытие и чтение файла
    with open(file, 'r', encoding='utf-8') as phonebook:
        contact = phonebook.readlines()
        for line in contact:
            print(line)
    # print(contact, end=";")


def DirTelBook(file): #преобразование в список словорей
    with open(file, 'r', encoding='utf-8') as phonebook:
        contact = phonebook.readlines()
    names = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    tel = []
    for line in contact:
        line = line.strip().split(', ')
        tel.append(dict(zip(names, line)))
    for i in (tel):
        print(i, end='\n')
    print(type(tel))
    return tel

def NewContakt (): #ввод нового контакта пользователем
    print("Введите Фамилию")
    firsName = input()
    print("Введите Имя")
    secondName = input()
    print("Введите отчество")
    treeName = input()
    print("Введите номер телефона")
    phone = input()
    return firsName, secondName, treeName, phone

def AddingData(file): #добавление нового контакта в телефонную книгу
    newContact = ', '.join(NewContakt())
    with open(file, 'a+', encoding='utf-8') as phonebook:
        phonebook.writelines(newContact + '\n')

def SearchByCriteria(): #ввод криетериев поиск контактов 
    print("Введите параметр поика\n 1 - Фамилия\n 2 - Имя\n 3 - Отчество\n 4 - Номер телефона")
    serchBySet = input()
    setVariant = None
    if serchBySet == '1':
        print("Ведите Фамилию")
        setVariant = input()
    elif serchBySet == '2':
        print("Ведите Имя")
        setVariant = input()
    elif serchBySet == '3':
        print("Ведите Номер телефона")
        setVariant = input()
    return serchBySet, setVariant

def SearchContackt(tel, search): #поиск и печать контакта по выбраному параметру
    serchBySet, setVariant = SearchByCriteria()
    contakt = []
    for cont in tel:
        if cont[search[serchBySet]] == setVariant:
            contakt.append(cont)
    for i in contakt:
        print(i)
        print(type(i))
    print(contakt)
    print(type(contakt))

def СhangeСontact(file, tel, search): #замена выбраных параметров
    serchBySet, setVariant = SearchByCriteria()
    contakt = []
    contPhone = []
    for cont in tel:
        if cont[search[serchBySet]] == setVariant:
            contakt.append(cont)
    print(contakt)
    for i in contakt:
        if i.values() == setVariant:
            contPhone.append(contakt)
    print(contPhone)
    with open(file, 'r+', encoding='utf-8') as phonebook:
        for cont in phonebook:
            line = ' '.join(i) + '\n'
            phonebook.write(line)

def DelitContact(tel,file, search): #удаление контакта
    serchBySet, setVariant = SearchByCriteria()
    with open(file, 'w+', encoding='utf-8') as phonebook:
        for cont in tel:
            if cont[search[serchBySet]] == setVariant:  
                line = ' '.join(cont) + '\n'
            phonebook.write(line)


def ShowMenu():
    print("\nВыберите необходимое действие:\n"
        "1. Открытие и чтение файла\n"
        "2. Добавление нового контакта в телефонную книгу\n"
        "3. Поиск и печать контакта по выбраному параметру\n"
        "4. Замена выбраных параметров\n"
        "5. Удаление контакта\n"
        "6. Закончить работу")
    choice = int(input())
    return choice

def WorkWithPhonebook():
    choice = ShowMenu()
    file = 'telPhone.txt'
    tel = DirTelBook(file)
    search = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Номер телефона'}
    while (choice != 6):
        if choice == 1:
            OpenFile(file)
        elif choice == 2:
            AddingData(file)
        elif choice == 3:
            SearchContackt(tel, search) 
        elif choice == 4:
            СhangeСontact(file, tel, search)
        elif choice == 5:
            DelitContact(tel, file, search)
        choice = ShowMenu()

WorkWithPhonebook()   