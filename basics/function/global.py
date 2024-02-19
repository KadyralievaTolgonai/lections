"====build-in====="
# встроенное пространство имен  (list,print,dict,len,input)     
"===Global=====" 

#  все переменные которые мы создали внутри файла 
# чтобы посмотреть все глобальные переменные можно использовать функцию globals

a=10
b="hello"
print(globals())






"=====local====="
# локальное пространство имен-это простраство которое находится внутри функции 
a=8
c="hello"
def func(a,b):
    res=a+b
    print(c)

    print(a+b)
    print(locals())
func(10,5)


a=10
def func():
    print(a)
func()


a=10
def func():
    global a
    print(a)
    a=60
    print(a)
func()
 

b=80
def func():
    global a
    b=90
   
    print(b)
print(b)
func()
print(a)



b=80
def func():
    
    b=90
   
    print(b)
print(b)
func()
print(a)



count=1
def count_():
    global count
    count+=1
    print(count)

count_()
count_()
count_()


# def count_():
#     global count
#     count+=1
#     print(count)
# while True:
#     count_




