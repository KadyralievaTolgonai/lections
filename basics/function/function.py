# '====функция===='
# # функция- это именнованный блок кода который может принимать аргументы и возвращать результат



# # def get_sum(x,y):  #x,y- параметры
# #     result=x+y
# #     return result

# # print(get_sum(10,20)) # 10,20 -аргументы



# """Функция соблюдают принцип DRY don't repeat yourself"""

# "====аргументы и параметры==="

# # парметры это переменные внутри функции задаются при создании функции
# # аргументы-это значения которые мы передаем при вызове функции


# "====виды параметров ====="
# # 1 обязательные
# # 2 необязательные
# # 2.1  с дпефолтом(со значением по умолчанию)
# # 2.2 args(все позиционные аргументы)
# # 2.3 kwargs(все лишние именнованные аргументы)


# # def func(a,b):
# #     a+b

# # print(func(10,20))

# # def func(a=5,b=4):
# #     return a+b
    
# # print(func(b=7))

# # def func(*args):
# #     print(*args)
# # print(func(1,2,3,"hi"))


# def func(*args,**kwargs):
#     print(*args)
#     print(kwargs)
# print(func(1,2,3,"hi",hello="hello world",p="hh"))

# def func_(a,b):
#     return a**b
# print(func_(10,2))


# def len_(a):
#     count=0
#     for i in a:
#         count=count+1
#     return count
# print(len_([6,5,12,678]))



# "===виды аргументов==="
# # 1 позиционные(по позиции)
# # 2 именованные (по названию(параметр=значение))

# def func_(a,b,c,d):
#     return func_
# print(func_(12,4,5,d=6))


# "-----------------------------------"
# # num:int="ygrueh"
# # name:str=10
# # num=10



# # def sum_(a:int,b:str):
# #     return a+b
# # print(sum_(2,3))


# def calc_():
#     try:
#         num1=float(input("enter number: "))
#         num2=int(input("enter number: "))
#         oper=input("enter oper: ")
#         if oper=="+":
#             print(num1+num2)
#         elif oper=="-":
#             print(num1-num2)
#         elif oper=="/":
#             print(num1/num2)
#         elif oper=="*":
#             print(num1*num2)
#         elif oper=="**":
#             print(num1**num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print(" вы вели не ту операцию")
#     except ValueError:
#         print("введите число а не символ")
#     except ZeroDivisionError:
#         print("делить на ноль нельзя")
        
# calc_()



        













# # db=[
# #     {"name":"Tima","password":hash("123456789")},
# #     {"name":"Nick","password":hash("205221000")}
# # ]


# # def in_database(name):
# #     for user in db:
# #         if name==user["name"]:
# #             return True
# #     return False

# # def register(name,password,password2):
# #     if in_database(name):
# #         raise Exception("юзер  с таким именем уже существует")
# #     if password !=password2:
# #         raise Exception("пароли не совпадают ")
# #     user={"name":name,"password":hash(password)}
# #     db.append(user)
# #     return " вы успешно зарегистрировались"


# # def login(name,password):
# #     if not in_database(name):
# #         raise Exception("пользователь не найден")
# #     for user in db:
# #         if user["name"]==name:
# #             if user["password"] !=hash(password):
# #                 raise Exception("пароль неверный")
# #     return "вы успешно залогинились"
 
# # print(register("katana","123123123","123123123"))
# # print(db)
# # print(login("katana","123123123"))








count=0
number=input()
if number.isdigit():
    count += int(number)
    print(count)
else:
    print("ghjk")















