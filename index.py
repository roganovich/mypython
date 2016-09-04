# пример создания строки
string = 'My first pynhon string'
print(string) #выводим на экран

# 0 элемент массива. строка это массив
first_e = string[0]
print(first_e) #выводим на экран

# c 3 по 7 элемент массива.
first_e = string[3:7]
print(first_e)

# выполняем сложение
a=1
b=6
print(a+b)

# выполняем разбор строки на элементы массива
spisok = list('spisok')
print(spisok)

#обновление элемента массива по его индексу
arr = [111, 222, '1', '2', 3, 4]
print(arr[5])
arr[5]=555
print(arr[5])

arr.sort()
arr.reverse()