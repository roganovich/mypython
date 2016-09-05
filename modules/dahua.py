# coding:utf8
import urllib.request
from bs4 import BeautifulSoup

class dahua:
    attr = {}
    pageObj = None

    def setAttr(self,name,value):
        self.attr[name]=value

    def getAttr(self, name):
        return self.attr[name]

    def startParser(self):
        page =  urllib.request.urlopen(self.attr['url']).read()
        self.pageObj = BeautifulSoup(page)

    def getPageObj(self):
        return self.pageObj