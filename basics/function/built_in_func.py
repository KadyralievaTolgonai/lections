# # # "======встроеннные функции====="
# # # # map,filter,reduce,zip,enumerate

# # # "zip"
# # # # соединяет несколько последовательностей (получаем генератор в котором элементы-tuple)(zip object)
# # # list_1=[1,2,3,4]
# # # list_2=["a","b","c"]
# # # list_3=[10.5,20.0,1.3,0.5]

# # # zipped=list(zip(list_1,list_2,list_3))
# # # # print(zipped) 

# # # print(tuple(zipped))
# # # # print(dict(zipped))  работает только с двумя листами так как первый лист ключ второе значние


# # # 'enumerate'
# # # #  нумерует последовательность (по дефолту с 0),(тоже возвращает генератор)
# # # enumerated=enumerate(("hello world",3,True),100)
# # # # print(enumerated)
# # # # print(list(enumerated))
# # # for elem in enumerated:
# # #     print(elem)



# # # "map"
# # # # принимает функцию и последоватедьность 
# # # # записывает в новую последовательность результат функции приминив  ее на каждый элемент последовательности 
# # # # map object 0 7d>

# # # list_=["1jghvhj","2","3"]
# # # # mapped=map(int,list_)  #map object 

# # # # print(list(mapped))

# # # mapped2=map(str.isdigit,list_)
# # # print(list(mapped2))


# # # list_=[1,5,78]
# # # def pow_(x):
# # #     return x**2
# # # print(list(map(pow_,list_)))

# # # print(list(map(lambda x:x**2,list_)))


# # # str_=["hello world"]
# # # mapped3=map(str.upper,str_)
# # # print("".join(list(mapped3)))

# # # print("".join(list(map(str.upper,str_))))





# # # "filter"
# # # # возвращает генератор с элементами  прошедшими фильтрацию (какое то условие ) принимает функцию и последовательность 



# # # list_=[12,-23,0]
# # # filtered=filter(lambda x:x>=0,list_)
# # # print(list(filtered))


# # # list_=[12,-23,0]
# # # filtered=map(lambda x:x>=0,list_)
# # # print(list(filtered))


# # # users=[{"name":"makers","age":20},{"name":"anonym","age":15},{"name":"sem","age":25}]

# # # filtered=filter(lambda x:x["age"]>18,users)
# # # print(list(filtered))
# # # filtered=filter(lambda x:x["name"].startswith("a"),users)
# # # print(list(filtered))
# # # "reduce"
# # # #  принимает функцию и последовательность  возвращает 1 элемент передаваемая функция должна принимать 2 аргумента 
# # # #  импортируется  из  funtools



# # # from functools import reduce
# # # list_=[1,5,8]
# # # res=reduce(lambda x,y:x*y,list_)
# # # print(res)

# # # list_=["3","3","6"]
# # # res=reduce(lambda x,y:x+y,list_)
# # # print(res)


# # # users=[{"name":"makers","age":20},{"name":"anonym","age":15},{"name":"sem","age":25}]
# # # from functools import reduce
# # # def func(x,y):
# # #     if x["age"]<y["age"]:
# # #         return x
# # #     else:
# # #         return y
# # # print(reduce(func,users))


# # # list_=[1,3,6,8]
# # # # res=reduce(lambda x,y:x if x<y else y,list_)
# # # # print(res)
# # # def func(x,y):
# # #     if x<y:
# # #        print(x)
# # #     else:
# # #        print(y)




    
    
     

# # # print(reduce(func,list_))







# # a=9.66
# # a=round(a,2)
# # print(a)



# # # # from functools import reduce
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]


# # # # print(list_)

# # def h(l):
# #     f=[]
# #     for i in l:
# #         if int(i)**2:
# #             f.append(i)

# #             print(round(i,3))
# # print(list(filter(h,list_)))


# # def h(l):
# #      return res
   
# #      res=[round(i**2,3) for i in l]
  
# # a=map(h,list_)
# # print(list(a))

   
   


  
# # #     # return res
# # # print(list(a))

# # z=[9,8,7]
# o=list(map(lambda x:round(x**2,3),list_))
# print(o)


# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list2=list(filter(lambda x:x>0,list_))
# list3=list(filter(lambda x:x<=0,list_))
# zipped=list(zip(list2,list3))
# print(zipped)


from functools import reduce
list_=[7,9,56,8]
res=reduce(lambda x,y:x if x<y else y,list_)
print(res)

res=["hbu" if i%3==0 else "jin" for i in range(1,50)]
print(res)



res=list(map(lambda x:"j" if x%3==0 else "k",range(1,51)))
print(res)






