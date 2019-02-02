import xml.sax as S
import time
import os
import os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.query import Every
from whoosh.index import open_dir
from whoosh.writing import BufferedWriter
from whoosh.qparser import QueryParser


class ArticleHandler(S.ContentHandler):

    def __init__(self):

        self._currentdata = ''
        self._title = ''
        self._author = ''
        self._date = ''
        self.dict = {'title': None, 'author': None, 'date': None}

        # parte del conto e controllo dei tag
        # contare i tag omonimi
        self.thisisphdthesis = 0
        self.thisismastersthesis = 0
        self.thisisarticle = 0
        self.thisisbook = 0
        self.thisiswww = 0
        self.thisisinproceedings = 0
        self.thisisincollection = 0
        self.thisisproceedings = 0

        self.whatis = None




    def startElement(self, name, attrs):
        self._currentdata = name

        if name == 'phdthesis':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisphdthesis += 1
            self.whatis = name
        elif name == 'mastersthesis':
            self.thisismastersthesis += 1
        elif name == 'article':
            self.thisisarticle += 1
        elif name == 'book':
            self.thisisbook += 1
        elif name == 'www':
            self.thisiswww += 1
        elif name == 'inproceedings':
            self.thisisinproceedings += 1
        elif name == 'incollection':
            self.thisisincollection += 1
        elif name == 'proceedings':
            self.thisisproceedings += 1


    def endElement(self, name):

        if self.whatis == 'phdthesis':
            if self._currentdata == 'author':
                self.dict['author'] = self._author
            elif self._currentdata == 'title':
                self.dict['title'] = self._title
            if name == 'phdthesis':
                if not self.dict['author']:
                    self.dict['author'] = 'unknown'
                writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'])
                self.dict['author'] = None
                self.dict['date'] = None
                self.dict['title'] = None
                self.whatis = None
        self._currentdata = ""


    def characters(self, content):
        if self._currentdata == 'author':
            self._author = content
        elif self._currentdata == 'title':
            self._title = content


    def endDocument(self):
        print('---------------------------------------------------------------')
        print('Incollections :', self.thisisincollection)
        print('Inproceed : ', self.thisisinproceedings)
        print('Book : ', self.thisisbook)
        print('Article : ', self.thisisarticle)
        print('WWWW : ', self.thisiswww)
        print('MasterT. : ', self.thisismastersthesis)
        print('PhdT. : ', self.thisisphdthesis)
        print('Proceed. : ', self.thisisproceedings)
        print('\nTotal : ---->', self.thisisincollection+self.thisisinproceedings+self.thisisbook\
              +self.thisisarticle+self.thisiswww+self.thisismastersthesis+self.thisisphdthesis\
              +self.thisisproceedings)
        writer.commit()


start = time.time()

schema = Schema(title=TEXT(stored=True),
                key=ID(stored=False),
                year=KEYWORD(stored=True),
                author=TEXT(stored=True),
                type=KEYWORD(stored=True))

####### parsing and indexing
 
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
writer = ix.writer()
parser = S.make_parser()
handler = ArticleHandler()
parser.setFeature(S.handler.feature_namespaces, 0)
parser.setFeature(S.handler.feature_external_ges, False)
parser.setContentHandler(handler)
parser.parse("dblp.xml")

####### search

#ix=open_dir("indexdir")
#print(ix.schema)
#with ix.searcher() as searcher:
#     query = QueryParser("title", schema=ix.schema).parse(u"title:Design AND author:Baltasar")
#     results = searcher.search(query,limit=None)
#     print(len(results))
#     for i in results:
#         print(i)

##### show all of doc (careful here)
#ix = open_dir('indexdir')
print(ix.doc_count())
#results = ix.searcher().search(Every('title'))
#print(ix.schema)
#for result in results:
#    print("Rank: %s Title: %s Author: %s" % (result.rank, result['title'], result['author']))

end = time.time()
exec_time = end-start
print(exec_time)
