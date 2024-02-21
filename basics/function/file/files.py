# "=========modul & package===="
# # .py- module
# # more modules-package

# "=======file======"
# # open()-функция которая открывает файл в определенном режиме
# # r-read(только для чтения)
# # w-write(только для записи каждый раз файл очищается)
# # a-append(только для дозаписи добавляется в конец)
# # x-создает файл но если он существует выйдет ошибка




# "======read======"
# # file=open("test1.txt","r")
# # # print(dir(file))
# # print(file.readable())#True
# # print(file.writable())
# # print(file.read()) # read file
# # print(file.read())
# # file.seek(15)
# # print(file.read())
# # print(file.read(10))
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())

# # print(file.tell())

# # print(file.readlines())
# # print(file.tell())
# # file.close()
# "read:str,readline:str,readlines:list[str]"



# "=====write======"
# # file=open("test1.txt","w")
# # # file.write("makers\nhello world\n")
# # file.writelines(["hellow\nmaker\n"])
# # file.close()
# # print(file.closed)
# "write(str),writelines(list[str,str])"

# "=====append===="
# #  append добавляет запись в конец


# file=open("test1.txt","a")
# file.write("py33\n")

# # file.seek(0)
# file.write("py32\n")
# file.close()


"=====контекстный менеджер ===="
# with
with open("test1.txt") as f:
    print(f.read())
print(f.closed)























