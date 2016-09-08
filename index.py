# coding:utf8

#подключаем все необходимые библиотеки
import sys
sys.path.append('modules')#Добавляем путь к собственным модулям
from dahua import Dahua #подключаем класс Dahua из модуля dahua
from timer import Timer #подключаем модуль работы со временем

t = Timer() #создаем обьект таймера
t.startTime() #запускаем таймер

dp= Dahua() #создаем обьект класса модели
dp.setAttr('url','http://dahua-russia.ru')
dp.setAttr('purl','http://dahua-russia.ru/catalog')
dp.setAttr('export',True)
#dp.setAttr('export_format','csv')
#dp.setAttr('export_file','dahua.csv')
dp.setAttr('export_format','mysql')


dp.startParser()
allpage = dp.returnAllObj()

t.endTimer() #считаем разницу во времени