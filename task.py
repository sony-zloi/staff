'''
Напишите информационную систему «Сотрудники».
Программа должна обеспечивать
ввод данных,
редактирование данных сотрудника,
удаление сотрудника,
поиск сотрудника по фамилии,
вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых начинается на указанную букву.
Организуйте возможность сохранения найденной информации в файл.
Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
программы — по команде пользователя).
При старте программы происходит загрузка списка сотрудников из указанного пользователем файла.
'''


def userEnter():
    try:
        _enter = int(input('There is a list of firm employee\n'
                           'Want do You want to do with that??\n'
                           'Press 1 if You wanna print this list\n'
                           'Press 2 if You wanna add an item to list\n'
                           'Press 3 if You wanna search employes by last name\n'
                           'Press 4 if You wanna print employes by age\n'
                           'Press 5 if You wanna print employes by first char of last name\n'
                           'Press 6 if You wanna delete an employee from the list\n'
                           'Press 7 if You wanna change data\n'
                           'Or press any key to quit\n'
                           '> '))
    except:
        _enter = 0

    return _enter


def printDict(_dict):
    print('-' * 100)
    for key, value in _dict.items():
        print(f'{key} - {value}')
    print()


def addItem(_dict):
    name = input('Enter a Last First and Middle name which you want to add: ')
    pNum = int(input('Enter a phone number: '))
    email = input('Enter an email: ')
    age = input('Enter a age: ')
    place = input('Enter a place: ')
    skype = input('Enter skype: ')
    # lst = []
    # lst.append(name)
    # lst.append(height)
    # _dict.update([lst])
    _dict.update({name: {'phone_number': pNum, 'email': email, 'age': age, 'place': place, 'skype': skype}})
    # _dict.update({name: [pNum, email, age, place, skype]})
    printDict(_dict)


def delItem(_dict):
    name = input('Enter the Last/First/Middile Name which you want to delete: ')
    if name in _dict:
        deletedItem = _dict.get(name)
        _dict.pop(name, None)
        print(f'{name} has been deleted')
        printDict(_dict)
    else:
        print('There is no this employee\n')


def searchLastName(_dict):
    last_names = list(_dict.keys())
    search = input('Enter the first char of Last Name searching for: ').lower()
    isTrue = True
    for item in last_names:
        if item.startswith(search):
            print(item)
            print(_dict.get(item))
            isTrue = False

    if isTrue:
        print('Not found!')


def searchByFirstChar(_dict):
    staff_lst = list(_dict.keys())
    search = input('Enter the first char of Last Name searching for: ').lower()
    isTrue = True
    for item in staff_lst:
        item.split()
        if search in item[0]:
            isTrue = False
            print(item)
    if isTrue:
        print('Not found!')


def searchByAge(_dict):
    search = int(input('Enter an age searching for: '))
    isTrue = True
    for key, value in _dict.items():
        if value.get('age') == search:
            print(key)
            isTrue = False
    if isTrue:
        print('Not found!')
    print()

def updateItem(_dict):
    name = input('Please enter the item which you wanna change??> ')
    if name in _dict:
        pNum = int(input('Enter a phone number: '))
        email = input('Enter an email: ')
        age = input('Enter a age: ')
        place = input('Enter a place: ')
        skype = input('Enter skype: ')
        dictNew = {name: {'phone_number': pNum, 'email': email, 'age': age, 'place': place, 'skype': skype}}
        _dict.update(dictNew)
        printDict(_dict)
    else:
        print('There is no this employee\n')


staff = {
    'ivanov ivan ivanovich': {
        'phone_number': 891293234923,
        'email': 'IvanovII@example.com',
        'position': 'lead engineer',
        'age': 23,
        'skype': 'ivI_23',
    },

    'petrov sergei grigorievich': {
        'phone_number': 891293156923,
        'email': 'PetrovSG@example.com',
        'position': 'engineer',
        'place': 20,
        'skype': 'Petruha',
    },

    'sidorov andrey dmitrievich': {
        'phone_number': 892813153923,
        'email': 'SidorovAD@example.com',
        'position': 'head of department',
        'age': 23,
        'skype': 'gromiko'
    },

    'kozlov timur kareevich': {
        'phone_number': 89181313423,
        'email': 'KozlovTK@example.com',
        'position': 'engineer',
        'age': 20,
        'skype': 'tri_palca_i_pupok'
    },

    'kuraev mikhail ivanovich': {
        'phone_number': 891113123423,
        'email': 'KuraevMI@example.com',
        'position': 'cleaner',
        'age': 23,
        'skype': 'not_cleaner'
    },
}
printDict(staff)
enter = userEnter()

while 0 < enter <= 7:
    if enter == 1:
        printDict(staff)
    elif enter == 2:
        addItem(staff)
    elif enter == 3:
        searchLastName(staff)
    elif enter == 4:
        searchByAge(staff)
    elif enter == 5:
        searchByFirstChar(staff)
    elif enter == 6:
        delItem(staff)
    elif enter == 7:
        updateItem(staff)
    enter = userEnter()

print('See Ya!!')