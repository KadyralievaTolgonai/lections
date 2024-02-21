"=====json===="
# javascript object notation-универсальный формат в котором мы можем хранить данные в типах данных понятных почти для всех языков программирования


import json 
# jason_list="[1,2,3,4]"
# python_list=json.loads(jason_list)
# print(python_list)

# jason_data="true"
# python_data=json.loads(jason_data)
# print(python_data)

# jason_data="null"
# python_data=json.loads(jason_data)
# print(python_data)

# десериализация -перевод с json  строки в python обьекты
# loads-метод для десериализации с json  строки
# load - метод для десериализации с json файла
# сериализация- перевод   python обьектов в  json строку
# dumps-метод для сериализации в  json строку
# dump - метод для сериализации в json файл


with open('test.json', 'r') as file:
    python_data=json.load(file)
    # print(file.readlines())
print(python_data)
