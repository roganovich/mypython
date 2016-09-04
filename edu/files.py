#работа с файлами
import os
folder = 'c:/test/'
filename = 'test.txt'

f = open(folder+filename,'w')
f.write('Roganovich ')
f.seek(5) #перейти на нужную нам позицию и продолжить работу
f.write('-')
f.write('Roman\n')
f.close()

strings = ['first\n','secont\n','third\n']
f = open(folder+filename,'w')
f.writelines(strings)
f.close()

f.close()
f = open(folder+filename,'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)
f.close()