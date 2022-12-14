# Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# Сделать замену информации по атрибуту (5 // Петров //+1113233// уборщик // 141515 -> зарплата: 33333 -> 5 // Петров //+1113233// уборщик // 33333)
# Если с таким критерием поиска несколько записей, нужно вызвать уточнение, чтобы получить запись конкретного сотрудника.

import interface
import os

clear = lambda: os.system('cls')

def menu():
    clear()
    print("""Справочник работников компании ООО "Прохиндей"\n
    
    1. Добавить нового сотрудника в справочник
    2. Поиск сотрудника по фамилии или номеру телефона
    3. Изменение данных по сотруднику
    4. Удаление данных на сотрудника\n""")
    num = interface.user_input()
    interface.user_response(num)

menu()