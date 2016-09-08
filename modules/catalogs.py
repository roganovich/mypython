from bd import myDB

class Catalogs(myDB):
    catalogs = None

    def getCatalog(self,name,subname):
        return name

    def setCatalog(self,name,subname=''):
        cur = myDB.conn.cursor()
        select_cat={}
        select_subcat={}

        select_cat = cur.execute("SELECT * FROM `catalog` where name='"+name+"'")
        select_subcat = cur.execute("SELECT * FROM `catalog` where name='" + subname + "'")

        if len(select_cat)>0:
            return True
        else:
            select_subcat = cur.execute("SELECT id FROM `catalog` where parent_id=" + select_cat[0]['id'])
            if len(select_cat)>0:
                selectsub = cur.execute("SELECT id FROM `catalog` where subname='" + subname + "'")
                if len(selectsub)>0:
                    self.insertCatalog()
            cur.query("INSERT INTO `catalog`(`parent_id`, `name`) VALUES ("+p_id+",'"+name+"')")

    def getAllCatalogs(self):
        if self.catalogs is not None:
            cur = myDB.conn.cursor()
            self.catalogs= cur.execute('SELECT * FROM `catalog`;')
