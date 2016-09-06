# coding:utf8
import urllib.request
from bs4 import BeautifulSoup
import csv

class Dahua:
    attr = {}
    pageObj = {}

    # функция добавляет параметра в загрузку
    def setAttr(self,name,value):
        self.attr[name]=value

    # функция возвращает занчение параметра в загрузку
    def getAttr(self, name):
        return self.attr[name]

    # функция собирает все данные каталогах и вложенностях
    def startParser(self):
        html =  urllib.request.urlopen(self.attr['purl']).read()
        soup = BeautifulSoup(html, "html.parser")
        mydivs = soup.findAll("li", {"class": "category category-level-1"})
        catalog = {}

        for main_div in mydivs:
            catalogname = main_div.findAll('a')[0].get_text().strip()
            catalogurl = self.attr['url'] + main_div.findAll('a')[0].get('href')
            subdivs = main_div.findAll("li", {"class": "category category-level-2"})
            if len(subdivs) > 0:
                for each_div in subdivs:
                    name = each_div.get_text().strip()
                    url = self.attr['url'] + each_div.findAll('a')[0].get('href')
                    catalog= {'catalogname':catalogname,'catalogurl':catalogurl,'subname':name,'pagesurl':url}
                    self.getArticlePager(catalog)
                    break
            else:
                catalog = {'catalogname':'','catalogurl':'','pagesurl': catalogname, 'subname': catalogurl}
                self.getArticlePager(catalog)
            break

    # функция собирает все данные о постраничной навигации и передает адрес страниц
    def getArticlePager(self,catalog):
        #ище пагинацию и вычисляем максимальное количество страниц в этой категории товаров
        html = urllib.request.urlopen(catalog['pagesurl']).read()
        soup = BeautifulSoup(html, "html.parser")
        pagers = soup.findAll("div", {"class": "paginator"})[0]
        ahref = pagers.findAll('a',{"class":"paginator-item"})[-1].get('href')

        pagecount = int(ahref[-2::]) #выбрать последние два символа в строке
        #? & page = 2
        p = 1
        while p<=pagecount:
            if p>1:
                catalog['pageurl'] = catalog['pagesurl']+'?&page='+str(p)
                self.getArticleList(catalog)
                break
            else:
                catalog['pageurl'] = catalog['pagesurl']
                self.getArticleList(catalog)
                break
            p +=1

    # функция собирает все артикулы на странице
    def getArticleList(self,article):
        #меняем catalog на article потому что дальше мы добавляем в обьект ортикула все данные о его категориях
        html = urllib.request.urlopen(article['pageurl']).read()
        soup = BeautifulSoup(html, "html.parser")
        page = soup.findAll("div", {"class": "products-list-wrapper"})[0]
        rows =  page.findAll("article", {"class": "tbl-row"})

        for row in rows:
            article['url'] = self.attr['url'] + row.findAll("a")[0].get('href')
            article['name'] = row.findAll("h2")[0].get_text().strip()
            self.getOneAticle(article)

    # функция собирает все данные об артикуле с его страницы
    def getOneAticle(self,article):
        html = urllib.request.urlopen(article['url']).read()
        soup = BeautifulSoup(html, "html.parser")

        article['desc'] = soup.findAll("div", {"class": "product-description product-info-section"})[0].get_text().strip()
        article['img'] = self.attr['url'] + soup.findAll("div", {"class": "product-image-wrapper"})[0].findAll("img")[0].get('src')

        article_spec={}
        specTable =  soup.findAll("table", {"class": "product-property-table"})[0]

        specTableTr = specTable.findAll("tr")
        # ищем характеристики артикула
        for tr in specTableTr:
            td = tr.findAll("td")
            if len(td)>1:
                attr = td[0].get_text().replace('  ','').strip()
                value = td[1].get_text().replace('  ','').strip()
                article_spec[attr]=value

        article['spec']=article_spec
        print(article)
        self.pageObj[article['url']]=article

    #функция возвращает весь список артикулов которые удалось собрать
    def returnAllObj(self):
        return self.pageObj

