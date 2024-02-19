# "====функция высшего порядка===="
# # функция высшего порядка-это функция которая принимает в аргументы другую функцию создает внутри себя другую функцию вызывает функцию и возвращает
# def func1():
#     return "hi"
# def func2(func_):
#    print(func_())

# func2(func1)


# "====декораторы====="
# # декаратор это функция высшего порядка которая нужна для расширения функкционала другой функции не изменяя ее (функция оберток)


# def decarator_glush(func):
#     def wrapper(*args,**kwargs):
#         text=func(*args,**kwargs)
#         res="тихо "+text
#         print(res)
#     return wrapper

# def gun():
#     return "стрелять"
# decarator_glush(gun)()


# "--------------------------------"

# def decarator_glush(func):
#     def wrapper(*args,**kwargs):
#         text=func(*args,**kwargs)
#         res="тихо "+text
#         print(res)
#     return wrapper

# @decarator_glush
# def gun():
#     return "стрелять"
# gun()
# # способ использовать декаторат при помощи синтаксического сахара





# "---------------"
# from datetime import datetime

# def decarator(func):
#     def wrapper():
#         print("start: ",datetime.now())
#         func()
#         print("finish: ",datetime.now())
#     return wrapper
# def hello():
#     print("hello world")
# wrapper=decarator(hello)
# wrapper()







# "-----------------------"
def call_function(func):
    def wrapper(*args, **kwargs):
        print('Вызываю функцию', func.__name__)
        func(*args, **kwargs)
        print('Вызов функции', func.__name__, 'прошёл успешно')
    return wrapper

@call_function
def first():
    print("hello world")
    return "hello world"

first()
# задача номер 1



from datetime import datetime

# def decarator(func):
#     def wrapper():
#         print("start: ",datetime.now())
#         func()
#         print("finish: ",datetime.now())
#     return wrapper

# @decarator
# def hello():
#     print("hello world")
# hello()


def func_start_time(func):
    def wrapper(*args,**kwargs):
        print("start: ", datetime.now())
        func(*args,**kwargs)
    return wrapper

@func_start_time
def sum_(a,b):
    print(a+b)
sum_(20,10)

def decarator(num):
    def inner_decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(num):
                func(*args,**kwargs)
        return wrapper
    return inner_decorator


@decarator(10)
def hello():
    print("hello world")

hello()

from datetime import datetime
def func_start_time(func):

    def wrapper(*args,**kwargs):
        print("Функция запущена 26.02.2021", datetime.now())
        func(*args,**kwargs)
    return wrapper

@func_start_time
def func():
    print('Hello world')
func()




# def make_bold(func):
#     def wrapper():
       
#       return   f"<b>{func()}</b>"
#       return wrapper


# def make_italic(func):
#      def wrapper():
       
#       return f"<u>{func()}</u>"
#       return wrapper



# def make_underline(func):
#       def wrapper():
       
#        return  f"<i>{func()}</i>"
#        return wrapper


# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())




# from datetime import datetime

# def benchmark(func):
#     def wrapper(*args,**kwargs):
#         print("Время выполнения: 0.05 секунд.", datetime.now())
#         func(*args,**kwargs)
#     return wrapper

# @benchmark 
# def fetch_webpage(): 
  
#   webpage = requests.get('https://google.com')  
# fetch_webpage()


# def validate_password(func):
#     def login(username, password):
#         users={"mark":7698,"tsar":6547}
#         print(f'Welcome, {username}')
#         func(username,password)
#     return login

# @validate_password
# def validate_password():
#     for username,password in a.items():
#         if username in users.keys():
#             print("Username is not defined")
#         elif password!=username.values() :
#             print("Password is invalid")  

# validate_password(username,password)




def validate_password(func):
    def wrapper(username,password):
        users={"wgv":678,"gyuw":790}
        if users.keys not in users:
            print("Username is not defined ")
        elif users.values!=password:
            print("Password is invalid ")
        else:
            return func(username,password)
    return wrapper

@validate_password

def login(username, password):
        print(f'Welcome, {username}')
login()