# # import functools 
# # list_ = [1, 2, 3, 4] 


# # list_1=functools.reduce(lambda x,y:x+y,list_)
# # print(list_1)


# # # list_ = [1, 5, -9, 6, -4] 
# # # result=all(list_.isdigit for i in list_ if i>3)
# # # print(list(result))


# # list_ = [1, 5, -9, 6, -4] 
# # result=filter(lambda x:x>3,list_)
# # print(list(result))


# # list_ = [1, 5, -9, 6, -4] 
# # result=filter(lambda x: "True"if x>3 else "False",list_)
# # print(list(result))


# # from functools import reduce
# # list_=[1,5,8]
# # res=reduce(lambda x,y:x if x>3 else y,list_)
# # print(res)


# # list_ = [1, 5, -9, 6, -4] 
# # result=all(i for i in list_ if i>3)
# # print(result)



# # list_=[1,2,3,4,5]
# # list2=len(list(filter(lambda x:x%2==0,list_)))
# # list3=len(list(filter(lambda x:x%2!=0,list_)))
# # print(list2,list3)
# # listi=filter(lambda even,odd:if int(i)%2==0)



# # list_=[1,2,3,4,5]
# # for i in list_:
# #     if i%2==0:
#  #   p=list_.count(i)

   
   

# # print(p)


# # l=[]

# # # list2=filter(lambda x: )
# # for i in list_:
# #     if i%2==0:
      
       
# #      print(i)

# # list_=[1,2,3,4,5]
# # i=0
# # k=0
# # u=1
# # l=lambda i:[i+u if i%2==0 else k+u for i in list_ ]
# # print(list(l))

# # for i in list_:
# #     if int(i)%2==0:
       
# #         ev+=1
       
# #     else :
      
# #         odd+=1
        
# # # print(ev,odd)

# # from functools import reduce


# # list_ = ['a', 'n', 'n', 'a',"p"]

# # def x(p,o):
# #     reduce
# #     if p==o:
# #         print("yes")
# #     else:
# # #         print("nno")
# # # print(reduce(x,list_))

# # # # list_="".join(list_)
# # # # print(list_)
# # # p="".join(list_)
# # # o=p[::-1]
# # print(o)


# # def f(x):
# #     return x%9
# # a=[555,876,944,786]
# # a.sort(key=f)
# # print(a)


# # a=[555,876,944,786]
# # # a.sort(key=lambda x:x//10%10)
# # # print(a)

# # def linear(k,b):
# #     return lambda x:x**2+k*b
# # graf1=linear(2,5)
# # print(graf1(3))

# # graf2=linear(-6,5)
# # print(graf1(7))

# # string = 'hello'
# # string=list(string)

# # for i in enumerate(string,1):
   
# #  print(tuple(string))


# # print(string)
# # 'enumerate'
# # #  нумерует последовательность (по дефолту с 0),(тоже возвращает генератор)
# # enumerated=enumerate(("hello world",3,True),100)
# # print(enumerated)
# # print(list(enumerated))
# # for elem in enumerated:
# #     print(elem)

# # string="hello"
# # e=enumerate(string,1)
# # print(tuple(e))
# # for i in tuple(enumerate(string,1)):
  

# #  print(i)


# # res=tuple(enumerate(string,1)) 
# # print(res)

# # list_ = ['123hello@gmail.com', '123', 'hello']
# # a=list(map(lambda x:x if "@gmail.com" in x[0] else "'Not valid email'",list_))
# # print(a)/////////
# # def s(x):
# #     if "@gmail.com" in x[0]:
# #      print("byun")
# #     elif a=map
  





# # if "@gmail.com" in list_[0]:
# #     print("byun")
# # else:
# #     ("bijn")


    








# # names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']

# # res=list(map(lambda x:x if len(x)>5 else "JavaScript",names))
# # print(res)

# # names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']

# # res=list(map(lambda x:f'{x}Python'if len(x)>5 else f'{x}JavaScript ',names))
# # print(res)


# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# a=list(map(lambda x:abs(x),list_))
# print(a)


# list_ = [1, 2, 3, 4] 
# result=list(filter(lambda x: x%2==0,list_))
# print(result)

# from functools import reduce
# list_1= ['a', 'n', 'n', 'a',]
# list_=list_1[::-1]
# print(list_)
# # a=list(reduce(lambda x,y:True if x+y else False,list_1))
# # print(a)



# from functools import reduce
# list_= ['a', 'n', 'n', 'a']
# res=reduce(lambda x,y:x+y,list_)
# p=res[::-1]
# if p==res:
#     print("YES")
# else:
#     print("NO")


# with open('text.txt', 'w+') as file: 
#     file.writelines(['0','*2','*3','*4','*5','*6','*7','*8','*9']) 
#     file.seek(0)

#     print(file.read())

# with open('task3.txt', 'a+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0) 
#     print(file.read())


# a=[6,8,9]
# y=max(a)
# p=min(a)
# print(y,p)


# # with open('task5.txt', 'r') as f:
# #      numbers = [int(line.strip()) 
# #      for line in f.readlines()]
# #      with open('task6.txt', 'w') as f: 
# #         f.write(f"{min(numbers)}-{max(numbers)}")

# # def read_last(lines, filename):
# #      with open(filename, 'r') as file_: 
# #          lines_list = file_.readlines() 
# #          lines_list.reverse() 
# #          if lines>= len(lines_list): 
# #              for line in lines_list:
# #                print(line.strip('\n'))
# #          else: 
# #              for i in range(lines): 
# #                print(lines_list[i].strip('\n'))


# # a=[7,9,87]
# # a=a[::-1]
# # print(a)
# # o="cghvjh"

# # for i in range(1,9):
# #     print(o[i])


# # inlist = open("input.txt", "w").read().split()
# # wm = ""
# # lm = 0
# # for w in inlist:
# #     l = len(w)
# #     if l > lm:
# #        wm = w
# #        lm = l
# # open("output.txt","w").write(wm)


# # o="hvgy hbjn\ngvyuhb"
# # p=o.replace('\n','')


# # print(p)
# string="678896"
# p=" ".join(string)
# s=p.split()
# i=[]
# p=i[0:1]
# print(p)

# for o in s:
#     i.append(int(o))
#     p=i[0:3]
#     z=i[3:]
# if sum(p)==sum(z):
#         print("fcg")
# else:
#         print("u")

    


# # for i in s:
    
    
# #     r.append(int(i))
# #     print(r,end='')
# # string1=string[:2]
# # string2=string[2:]
# # print(sum(string1))

# # print(int(z))

# # for i in string:
# #     if sum(string1)==sum(string2):
# #         print('да')
# #     else:
# #         print('нет')


# # a=int(input())
# # b=int(input())
# # c=int(input())


# # r=min(a,b,c)

# # d=max(a,b,c)
# # e=a+b+c-d-r

# # print(r,r,d)
# # # a=[]
# # for i in a:
# #     a=[]
# #     a.append(i)
# # print(a)


# # print(a,b,c)


# # a=range(int(input()))
# # o=[]
# # for i in a:
# #     o.append(i)
# # print(o)

# # print(sorted([int(input()) for _ in '' ]))

# # a=1
# # b=5
# # c=7
# # if a <= b and a <= c and b <= c:
# #  print(a,b,c)

# # a=int(input())
# # if a<=18:
# #     print('Доступ запрещен')
# # else:
# #     print('Добро пожаловать')

# # a=int(input(range(1,13)))
# # print(a)

# # a=int(input())
# # if 1<=a<=2:
# #     print("зима")
# # elif 3<=a<=5:
# #     print("весна")
# # elif 6<=a<=8:
# #     print("лето")
# # elif 9<=a<12:
# #     print("осень")
# # else:
# #     print("yv")
  
# # print("tyv")


# # a=int(input())
# # if 1<=a<=2:
# #     print("зима")
# # elif 3<=a<=5:
# #     print("весна")
# # elif 6<=a<=8:
# #     print("лето")
# # elif 9<=a<12:
# #     print("осень")
# # else:
# #     print("Такого месяца нет")

# # a=int(input())
# # if a>12:
# #     print("Такого месяца нет")
# # elif a==12 or 1<=a<=2:
# #     print("зима")
# # elif 3<=a<=5:
# #     print("весна")
# # elif 6<=a<=8:
# #     print("лето")
# # elif 9<=a<=11:
# #     print("осень")

# # a=int(input())
# # b=int(input())
# # c=int(input())
# # if a+b+c==90:
# #     print("rectangular")
# # i
# # elif a+b+c<90:
# #     print("acute")
# # elif a+b+c>90 or a+b+c<=180:
# #     print("obtuse")
# # else:
# #     print("impossible")

# # a=int(input())
# # b=int(input())

# # if a+b>c and a+c>b and b+c>a:
 
# # elif c**2>a**2+b**2:
# #     print("obtuse")
# # else:
# #     print("impossible")
# # elif c**2<a**2+b**2:
# #     print("acute")

# # a=int(input())
# # b=int(input())
# # c=int(input())
# # if a+b>c and a+c>b and b+c>a:
# #     if a**2+b**2==c**2:
# #       print("rectangular")
# #     elif c**2<a**2+b**2:
# #       print("acute")
# #     elif c**2>a**2+b**2:
# #       print("obtuse")
# #     else:
# #      print("impossible")

# # a1, b1, c1 = int(input()), int(input()), int(input())
# # c = max(a1, b1, c1)
# # b = min(a1, b1, c1)
# # a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1)
# # print(a,b,c)


# # a=int(input())

# # if a%10==0 and a:


# # num=int(input())

# # if chr(num).isalpha():
# #     print('''Это буква "буква" ''')
# # else:
# #     print('''Это не буква, а символ "символ"''')


# # num=int(input())

# # if chr(num).isalpha():
# #     print(f'''Это буква "{chr(num)}" ''')
# # else:
# #     print(f'''Это не буква, а символ "{chr(num)}" ''')

# # if chr(num):
# #     print(f'''Это буква "{num}" ''')
# # else:
# #     print(f'''Это не буква, а символ "{num}" ''')

# # mark=int(input())
# # if mark>=90:
# #     print("Отлично, Ваша оценка 5! ")
# # elif mark>=80:
# #     print("Здорово, Ваша оценка 4! ")
# # elif mark>=70:
# #     print("Хорошо, Ваша оценка 3! ")
# # elif mark>=60:
# #     print("Вам стоит подучить материал")
# # else:
# #     print("Вы не сдали экзамен")

# # x=102
# # y=36
# # z=90
# # if x<y and x<z:
# #     print(x)
# # elif y<x and y<z:
# #     print(y)
# # else:
# #     print(z)

# # x=32
# # y=32
# # z=100

# # if x==y and x==z:
# #     print("3")
# # elif x==y or x==z:
# #     print("2")
# # else:
# #     print("0")

# # x=int(input())
# # y=int(input())
# # z=x%y
# # f=x//y
# # if x%y==0:
# #     print(f'Частное:{f}')
# # else:
# #     print(f'Остаток:{z}')



# # print(f'Частное:{f}')
# # print(f'Остаток:{z}')

# # x=int(input())
# # y=int(input())

# # if x%y:
# #     print("Остаток: ",x%y)
# # elif x%y==0:
# #     print("Частное: ",x//y)
# # else:
# # o=list(map(int,input().split(",")))
# # for i in o:
# #     p="".join(i)
# # print(p)

# # i=int(input())
# # o=int(input())
# # print(i,end(","))
# # print(o,end(","))
# # i=input()
# # p=i.split(",")
# # p=sorted(p)
# # print(p)

# # list_ = [1,7,9,6,8]
# list_ = [20, 1, 100]
# if [0]>[1]>[2] or [0]>[2]>[1] in list_ :
#      print(list_[0]) 
# elif [0]<[1]<[2] or [1]<[0]<[2] : 
#     print(list_[1]) 
# elif [0]<[2]<[1] or [2]<[0]<[1] :
#      print(list_[2])
# print()

# # if list_[0]<list_[1] or list_[1]<list_[2] and list_[2]<list_[3] and list_[3]<list_[4]:
# #     print(list_[0])
# # elif list_[1]<list_[2] or list_[2]<list_[3] and list_[3]<list_[4]:
# #     print(list_[1])
# # elif list_[2]<list_[3] and list_[3]<list_[4]:
# #     print(list_[2])
# # elif list_[3]<list_[4]:
# #     print(list_[3])
# # else:
# #     print(list_[4])


# # lst = [1, 0, 3, 6, -5, 7]
 
# # mins = lst[0]
# # print(mins)
# # # for i in lst:
# # #     if i < mins:
# # #         mins = i
        
# # # print(mins)

# # num=1
# a=[]


# # while num<=5:
# #     print(num,input())
# #     num=num+1


# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x=8
# for i in list_:
#     if x in list_:
#         p=list_.count(x)
# print(p)


# # list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# # number=8

# # if number in list_:
# #   p=list_.count(number)
# # print(p)

# str_list = ['abc', 'xyz', 'aba', '1211']



# # if str_list[0][0]==str_list[0][2] or str_list[1][0]==str_list[1][2] :
# #     print(str_list)
# # elif  str_list[2][0]==str_list[2][2] or str_list[3][0]==str_list[3][3] :
# #     print(str_list)

# str_list = ['abc', 'xyz', 'aba', '1221']
# y=[]
# for i in str_list:
#     if i[0]==i[::-1]:
#      y.append(str_list.index(i))
# print(y)
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_lists=max(lists)
# min_lists=min(lists)
# print(f'max_list {max_lists}')
# print(f'min_lis {min_lists}')//////////




# def call_function(func):
#     def wrap(func):
#         print(f'Вызываю функцию {func.__name__}')
#         func()
 
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#         return wrap
#         wrap()
    

# @call_function
# def first():
#         print("hello world")
#         return "hello world"
#         first()



# def call_function(func): 
#     def wrapper(): 
#         print(f"Вызываю функцию {func.__name__}")
#         func() 
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#         return wrapper
 
# @call_function
# def first():
#   print("hello world") 
#   return 'hello world' 
#   first()

# def call_function(func): 
#     def wrapper(): 
#       print(f"Вызываю функцию {func.__name__}")
#       func() 
#       print(f"Вызов функции {func.__name__} прошёл успешно")
#       return wrapper


 
# @call_function
# def first():
#   print("hello world") 
#   return 'hello world' 


# first()

# def i():
#   p="ygvhub"
#   print(p)
#   return p
# i()


lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_list=lists[0]
min_list=lists[0]

for i in lists:
    if len(i)>len(max_list):
        max_list=i
    if len(i)<len(min_list):
        min_list=i

if min_list==max_list:
        min_list==None
        
        
print('max_list',max_list)
print('min_list',min_list)






    
    
   

    








    


















  

