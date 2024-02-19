# # l=[1,2,3,4,5,6,7,8,9,10]
# # p=[i**2 for i in l if i%2==0]
# # print(p)

# # def check_numbers(t):
# #     if t%2==0:
# #         print(bool(1))
# #     else:
# #         print(bool(0))

# # check_numbers(6)



# # def length_text(i):
# #       i=input()
      
      

      
      
# #       print(len(i))
        
# # length_text("fteduygfir")


# # p=int("vhbj")
# # print(p)



# string = input("enter text ")
# def length_text(string):
#       list_ = string.split(" ")
#       length_string = []
#       for i in list_:
#             length_string.append(len(i))
#       return length_string



# print(length_text(string))
       
# def foo():
#        var=" переменная foo"
#        def bar():
#             global var
#             var=" переменная bar"
            
#        bar()
#        print(var)
# foo()
# print(var)



# # def foo():
# #       var="переменная foo"
# #       def bar():
# #         global var
# #         var="переменная bar"
        
# #       bar()
# #       print(var)
     
# # foo()
# # print(var)


# def foo():
#     var = 'переменная foo'
#     def bar():
#         global var
#         'переменная bar'
        
#     bar()
#     print(var)
# foo()
# print(var)


def foo():
    var = 'переменная foo'
    def bar():
        global var
        var = 'переменная bar'
        
    bar()
    print('переменная в bar: ', var)
foo()
print('переменная в foo: ', var)


# # def foo():
# #  global var
# #  var = 'переменная foo'
# #  def bar():
# #    global var
# #    var='переменная bar'
   
        
# #  bar()

# # foo()
# # print('переменная в bar: ', var)
# # print('переменная в bar: ', var)


# # def foo():
# #  var = 'переменная foo'
# #  def bar():
# #    global var
# #    var='переменная bar'
        
# #  bar()
# #  print('переменная в foo: ', var)
# # foo()
# # print('переменная в bar: ', var)


# # x="Я глобальная переменная!"
# # print(x)
# # def my_func():
# #   global x
  
# #   x="Я могу изменяться."
  
  
# # my_func()
# # print(x)


# # x="Я глобальная переменная!"
# # def my_func():
# #     global x
# #     x="Я могу изменяться."
# # my_func()
# # print(x)


# # x="Я глобальная переменная!"  right
# # print(x)
# # def my_func():
# #     global x
# #     x="Я могу изменяться"
# # my_func()
# # print(x)


# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# # def lower_7():
# #     for i in a:
# #         if i<7:
# #             print(i)
# # lower_7()




# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# # m=[]
# # def lower_7():
# #     for i in a:
# #         if i<7:
            
# #             m.append(i)
# #             print(m)
# # lower_7()

# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# # def lower_7():
# #     for i in a:
# #         if i<7:
# #             n=[]
# #             n.append(i)
# #             print(n)
            
 
# # lower_7()



# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]  ri
# # s=[]
# # def lower_7():
# #     global s
# #     for i in a:
# #         if i<7:
# #           s.append(i)
            
        
            
 
# # lower_7()
# # print(s)


# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# # s=[]
# # def lower_7():
    
# #     for i in a:
# #         if i<7:
# #           s.append(i)
# #     return s
            
        
            
 
# # print(lower_7())


# # a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3] ri

# # def lower_7():
# #     s=[]
    
# #     for i in a:
# #         if i<7:
# #           s.append(i)
# #     return s
            
        
            
 
# # print(lower_7())

# # p="hvp"
# # if "h""v""p" in p:
# #   print("i")

# # a=['pipi', 'papa', 'mama']
# # d=' '.join(a)
# # o=d.title()
# # s=o.split(" ")
# # print(s)



# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# d=a.keys
# for i,k in a.items():
#     if k>17:
#         print(f"{i},Вы можете войти в клуб")

a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
d=a.keys
for i,k in a.items():
    if k>17:
        print(f"{i},Вы можете войти в клуб")
    else:
        print(f"{i},извините, Вы не проходите по age-control")


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# d=a.keys
# for i,k in a.items():
#     if k>=17:
#         print(f"{i},Вы можете войти в клуб \n")
#     else:
#         print(f"{i},извините, Вы не проходите по age-control\n")


# # result=0
# # result+=6**5
# # result=result%7
# # print(result)



# result = 0
# def pow_first(x,y):
#     global result
#     result=x**y
# pow_first(2,3) 
# def pow_second(z):
#         global result
#         result=result%z
# pow_second(3)
  
 
# print(result)


# string=input()
# def count_symbols(string):
  
#   count=0
#   count1=0
#   count2=0
   
#   v=set("бвгджзйклмнпрстфхцчшщ")
#   p=set("яуюоеёэиы")

#   for i in string:
#       if i.lower() in p:
#         count+=1
#       elif i.lower() in v:
#         count1+=1
#       else:
#         count2+=1

#   return count,count1,count2
# print(count)
# print(count1)

# count_symbols()





# def count_symbols(p):
   
  
#    glasnye = 0 
#    soglasnye = 0 
#    drugie = 0 
#    for letter in p: 
#       if letter.lower() in 'аяуюоеёэиы': 
#        glasnye += 1 
#       elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ':
#        soglasnye += 1 
#       else: 
#        drugie += 1 
#        return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}')
# print(count_symbols('Привет;'))


# def f():
#   a=[i for i in range(1,10)]
  
#   print(a)
# f()

# a=[]
# def f():
#   a=[i for i in range(1,10)]
#   return a
  
# print(f())




def func():
    global a
    a = []
    for i in range(0,11):
        a.append(i)
    return a
func()
print(a)

  
























  







    
    





   
