#условия
pre = 111
if pre <100 :
    print('<100')
elif pre>100:
    print('>100')
else:
    print('=100')

if pre >100 and pre!=101:
    print('>101')

if pre <90 or pre !=101:
    print('90')

# циклы


# while
a=0
while a != pre:
    print(a, end=', ') #end условие разделитель!!!!!!!!!!!!!!!!!!!!!!
    a += 1
# for
a = ['1,', '2', '3']
for x in a:
    print(x)

for i in range(10): #range(10) создать список от 0 до 10 принимает 3 параметра range(старт, стоп, шаг)
    print(i, end=' ,')
# for по элементам строки
for i in 'string o string':
    if i == 'o': # условие пропустить элемент списка с таким значением
        continue
    print(i * 2, end=' ')
for i in 'string o string':
    if i == 'o': # условие остановить работу циклы после элемента списка с таким значением
        break
    print(i * 2, end=' ')


# Функциии начинаються со слова def
print('\n Функциии')
def myfunc(x):
    if x > 0:
        print('x > 0') #возможно указывать на return
    else:
        print('x <= 0')

myfunc(9)
myfunc(-9)

