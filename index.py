# coding:utf8
import sys
#Добавляем путь к собственным модулям
sys.path.append('modules')



import baseclass #несмотря на предупреждение модуль подключился
import dahua #несмотря на предупреждение модуль подключился

baseclass.testFunc('check add new module') #вызываем метод из модуля

dp= dahua.dahua()
dp.setAttr('url','http://dahua-russia.ru')
dp.startParser()
soup = dp.getPageObj()

print(soup.prettify())


