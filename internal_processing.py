import re
#1 - Добавить нового сотрудника в справочник
def add_person(file_function):
    input_name = input('Укажите ФИО сотрудника -> ')
    input_phone = input('Укажите номер телефона -> ')
    input_position = input('Укажите должность -> ')
    input_salary = input('Укажите зарплату -> ')
    data_phone = uniq_numbers(input_phone)
    file_function(input_name,data_phone,input_position,input_salary)
    print('Данные успешно добавлены')
#2 - Поиск сотрудника по фамилии или номеру телефона
def find_persons(file_func,type):
    person_search = input('Введите данные для поиска -> ')
    if uniq_numbers(person_search).isdigit() and (len(person_search)==11 or len(person_search)==10):
        person_search = uniq_numbers(person_search)
    base = file_func()
    answer=[]
    for i in range(len(base)):
        if person_search in base[i]:
            answer.append(base[i])
    if type == 1:
        if len(answer)!=0:
            for i in range(len(answer)):
                answer[i] = answer[i].split(";")
                to_print = ""
                for j in range(1,len(answer[i])):
                    to_print += str(answer[i][j]) + " "
                print(to_print)
        else:
            print('Такой фамилии в справочнике нет')
    elif type == 2:
        return (answer,person_search)
#3 - Изменение данных по сотруднику
def change_personal_data(database_function,rewrite_function):
    all_base = database_function()
    (list,search) = find_persons(database_function,2)
    index_list =[]
    for i in range(len(all_base)):
        if search in all_base[i]:
            index_list.append(i)
    for i in range(len(list)):
        print(list[i])
    select = input("Введите номер сотрудника из справочника для изменения его данных\n ")
    attribute_change=int(input('''Введите номер пункта, который хотите поменять -> 
                    1. ФИО
                    2. Телефон
                    3. Должность
                    4. Зарплата     '''))
    data_change = input("   Введите новые данные -> ")
    if uniq_numbers(data_change).isdigit() and len(data_change) >= 10:
        data_change = uniq_numbers(data_change)
    if select == 0:
        for i in range(len(list)):
            change_attr = str(list[i]).split(";")
            change_attr[attribute_change] = data_change
            list[i] = ""
            for x in range(len(change_attr)):
                if x==len(change_attr)-1:
                    list[i]+=change_attr[x]
                else:
                    list[i]+=change_attr[x]+";"
            all_base[index_list[i]]= list[i]
            print(all_base[index_list[i]])
    else:
        for y in range(len(list)):
            list[y]=list[y].split(";")
            if select in list[y][0]:
                list[y][attribute_change]= data_change
                uniq_person = f'{list[y][0]};{list[y][1]};{list[y][2]};{list[y][3]};{list[y][4]}'
                list[y]=uniq_person
                all_base[index_list[y]]= list[y]
                print(all_base[index_list[y]])
                break
    rewrite_function(all_base)
#4 - Удаление данных на сотрудника
def delete_person(database_func, rewrite_func):
    catalog = database_func()
    (persons_list, search) = find_persons(database_func,2)
    index_list =[]
    for i in range(len(catalog)):
        if search in catalog[i]:
            index_list.append(i)
    for i in range(len(persons_list)):
        print(persons_list[i])
    select = input("Введите номер сотрудника из справочника для изменения его данных -> ")
    for y in range(len(persons_list)):
        check = persons_list[y].split(";")
        if select in check[0]:
            result = catalog.pop(index_list[y])
            print(f'{result} - Сотрудник удален из справочника')
    rewrite_func(catalog)






    


#Подгонка телефона под формат 84951356369
def uniq_numbers(number):
    number = number.replace(" ","")
    number = re.sub(r'\D',"",number)
    number = re.sub('^7',"8",number)
    return number
