import internal_processing
import logger


def user_input():
    request = 0
    try:
        while request < 1 or request > 4:
            request = int(input("Введите цифру, соответствующую пункту меню -> "))
    except ValueError:
        print('Неправильный ввод')
    return request

def choose_menu_point(number):
    if number == 1:
    #1 - Добавить нового сотрудника в справочник
        return internal_processing.add_person(logger.add_to_file)
    #2 - Поиск сотрудника по фамилии или номеру телефона
    elif number ==2:
        return internal_processing.find_persons(logger.read_from_file,1)
    #3 - Изменение данных по сотруднику
    elif number ==3:
        return internal_processing.change_personal_data(logger.read_from_file,logger.rewrite_in_file)
    #4 - Удаление данных на сотрудника
    elif number ==4:
        return internal_processing.delete_person(logger.read_from_file,logger.rewrite_in_file)
# Вывод ответа
def user_response(numb):
    choose_menu_point(numb)


