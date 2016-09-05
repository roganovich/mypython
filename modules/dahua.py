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
        soup = BeautifulSoup(page, "html.parser")
        mydivs = soup.findAll("a", {"class": "product-offer"})
        catalog = {}
        for each_div in mydivs:
            name = each_div.get_text().strip()
            url = each_div.get('href')
            img = each_div.findAll('img')[0].get('src')
            catalog= {'name':name,'url':url,'img':img}

            print (catalog)


    def getPageObj(self):
        return self.pageObj