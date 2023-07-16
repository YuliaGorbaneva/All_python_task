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

# def ShowMenu():
#     print("\nВыберите необходимое действие:\n"
#         "1. Отобразить весь справочник\n"
#         "2. Отобразить справочник с шапками\n"
#         "3. Добавить контакт\n"
#         "4. Изменить данные контакта\n"
#         "5. Удалить контакт\n"
#         "6. Сохранить справочник в текстовом формате\n"
#         "7. Закончить работу")
#     choice = int(input())
#     return choice

def OpenFile():
    with open('telPhone.txt', 'r', encoding='utf-8') as file:
        print(*file)
    # file = open('telPhone.txt', 'r', encoding='utf-8')
    # print(*file)
    # file.close()
OpenFile()

def OpenListGroup(filename):
    filename = 'telPhone.txt'
    with open(filename, 'r', encoding='utf-8') as file:
    # file = open('telPhone.txt', 'r', encoding='utf-8')
        worlds = file.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    telDirect = []
    for line in worlds:
        line = line.strip().split()
        telDirect.append(dict(zip(headers, line)))
    return telDirect
print(OpenListGroup('telPhone.txt'))
print()

def PrintForKey(telDirect: list):
    for contact in telDirect:
        for key, value in contact.items:
            print(f'{key}: {value}', end=";")
        # print()
# PrintForKey(OpenListGroup)

def ShowPhonebook(filename):
    contacts = sorted(OpenListGroup(filename), key=lambda x: x['Имя'])
    PrintForKey(contacts)
    return contacts
ShowPhonebook('telPhone.txt')
        






# def ReadFile(filename):
#     filename = 'telPhone.txt'
#     with open(filename, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
#     contactList = []
#     for line in lines:
#         line = line.strip().split()
#         contactList.append(dict(zip(headers, line)))
#     return contactList
# print(ReadFile('telPhone.txt'))

# def PrintContacts(contactList: list):
#     for contact in contactList:
#         for key, value in contact.items():
#             print(f'{key}: {value}', end='')
#         print()

# def ShowPhonebook(filename):
#     listOfContacts = sorted(ReadFile(filename), key=lambda x: x['Фамилия'])
#     PrintContacts(listOfContacts)
#     return listOfContacts

# def SearchParameters():
#     print('Поиск по полю')
#     searchField = input('1 - по фамилии\n2 - по имени\n3 - по отчеству\n4 - по номеру телефона\n')
#     print()
#     searchValue = None
#     if searchField == '1':
#         searchValue = input('Введите фамилию для поиска: ')
#         print()
#     elif searchField == '2':
#         searchValue = input('Введите имя для поиска: ')
#         print()
#     elif searchField == '3':
#         searchValue = input('Введите отчество для поиска: ')
#         print()
#     elif searchField == '4':
#         searchValue = input('Введите номер телефона для поиска: ')
#         print()
#     return searchField, searchValue

# def FindNumber(contactList):
#     searchField, searchValue = SearchParameters()
#     searchValueDict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Номер телефона'}
#     foundContacts = []
#     for contact in contactList:
#         if contact[searchValueDict[searchField]] == searchValue:
#             foundContacts.append(contact)
#     if len(foundContacts) == 0:
#         print('Контакт не найден!')
#     else:
#         PrintContacts(foundContacts)

# def GetNewNumber():
#     lastName = input('Введите фамилию: ')
#     firstName = input('Введите имя: ')
#     phoneNumber = input('Введите номер телефона: ')
#     return lastName, firstName, phoneNumber


# def AddPhoneNumber(filename):
#     info = ' '.join(GetNewNumber())
#     with open(filename, 'a', encoding='utf-8') as file:
#         file.write(f'{info}\n')

# def ChangePhoneNumber(filename):
#     contactList = ReadFile(filename)
#     numberToChange = SearchToModify(contactList)
#     contactList.remove(numberToChange)
#     print('Какое поле вы хотите изменить?')
#     field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
#     if field == '1':
#         numberToChange[0] = input('Введите фамилию: ')
#     elif field == '2':
#         numberToChange[1] = input('Введите имя: ')
#     elif field == '3':
#         numberToChange[2] = input('Введите номер телефона: ')
#     contactList.append(numberToChange)
#     with open(filename, 'w', encoding='utf-8') as file:
#         for contact in contactList:
#             line = ' '.join(contact) + '\n'
#             file.write(line)

# def SearchToModify(contactList: list):
#     searchField, searchValue = SearchParameters()
#     searchResult = []
#     for contact in contactList:
#         if contact[int(searchField) - 1] == searchValue:
#             searchResult.append(contact)
#     if len(searchResult) == 1:
#         return searchResult[0]
#     elif len(searchResult) > 1:
#         print('Найдено несколько контактов')
#         for i in range(len(searchResult)):
#             print(f'{i + 1} - {searchResult[i]}')
#         numberCount = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
#         return searchResult[numberCount - 1]
#     else:
#         print('Контакт не найден')
#     print()

# def DeleteContact(filename):
#     contactList = ReadFile(filename)
#     numberToChange = SearchToModify(contactList)
#     contactList.remove(numberToChange)
#     with open(filename, 'w', encoding='utf-8') as file:
#         for contact in contactList:
#             line = ' '.join(contact) + '\n'
#             file.write(line)

# def WorkWithPhonebook():
#     choice = ShowMenu()
#     phonebook = ReadFile('telPhone.txt')
#     while (choice != 7):
#         if choice == 1:
#             ShowPhonebook(phonebook)
#         elif choice == 2:
#             contact_list = ReadFile(phonebook)
#             FindNumber(contact_list)
#         elif choice == 3:
#             AddPhoneNumber(phonebook)
#         elif choice == 4:
#             ChangePhoneNumber(phonebook)
#         elif choice == 5:
#             DeleteContact(phonebook)
#         choice = ShowMenu()

# WorkWithPhonebook()    
