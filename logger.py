path = 'C:/Users/Bjorn Hatred/Desktop/THE MOST IMPORTANT FOLDER/GeekBrains/Python/Lesson08/database.txt'
catalog = ""

def read_from_file():
    global catalog
    with open(path,'r',encoding='utf-8') as file:
        catalog = file.read().split('\n')
    return catalog


def add_to_file(data_person,number,post,salary):
    with open(path,'a+',encoding='utf-8') as file:
        base = read_from_file()
        length = len(base)
        file.write(f'{length};{data_person};{number};{post};{salary};\n')


def rewrite_in_file(array):
    with open(path,'w',encoding='utf-8') as file:
        for i in range(len(array)):
            file.write(f'{array[i]}\n')