"=======lamda====="
#  lamda-анонимная функция которая записывается в одну строку :


# def sum_(x,y):
#     return x+y

# sum_(10,6)




# sum_2=lambda x,y:x+y
# print(sum_2(6,9))


def sum_(y):
    return y**2
    

print(sum_(2))







sum_2=lambda y:y+y+y*y//y
print(sum_2(6))



a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
def lower_7():
    for i in a:
        if i<7:
            a=[]
            a.append(i)
        print(a)
lower_7()


