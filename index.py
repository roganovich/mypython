# coding:utf8
import sys
#Добавляем путь к собственным модулям
sys.path.append('modules')
import baseclass #несмотря на предупреждение модуль подключился
import dahua #несмотря на предупреждение модуль подключился

baseclass.testFunc('check add new module') #вызываем метод из модуля

dahuaparser = dahua.dahua()
dahuaparser.setAttr('ulr','dahua.com')
url = dahuaparser.getAttr('ulr')
print(url)
