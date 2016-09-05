# coding:utf8

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
arr = [111, 222, '333', '444', 555, 666]
print(arr[5])
arr[5]=777
print(arr[5])

#развернуть массив в обратном порядке
print(arr)
arr.reverse()
print(arr)

#сортировка массива.... только один тип в массиве!!!!!!
arr=[5,6,2,3,6,8,9]
print(arr)
arr.sort()
print(arr)

#сортировка массива.... только один тип в массиве!!!!!!
arr=['55','124','88','99','1']
print(arr)
arr.sort()
print(arr)

#найти индекс элемента массива по значению
a = arr.index('55')
print(a)

#очистить значение переменной
#a.clear()
#print(a)

#добавить элемент в список
arr=['55','124','88','99','1']
arr.append(99999999)
print(arr)

#добавить элемент из списка по значению
arr.remove('124')
print(arr)

#ассоциативные массивы
pre = {'name':'ira','lasetame':'pleshakova'}
print(pre)
#добавляем элементы по имени ключа
pre['age']=[1988]
pre['sex']='female'
print(pre)

#сравнить размер списка и массива
list=(1,2,3)
array=[1,2,3]
print(list.__sizeof__())
print(array.__sizeof__())

#полностью удалить из памяти переменную
del list