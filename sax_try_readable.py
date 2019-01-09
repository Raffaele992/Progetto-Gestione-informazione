import xml.sax as S
import time
import os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.query import Every
from whoosh.writing import BufferedWriter
from whoosh.qparser import QueryParser
from whoosh.index import open_dir


class ArticleHandler(S.ContentHandler):

    def __init__(self):

        self._currentdata = ''
        self._title = ''
        self._author = ''
        self._year = ''
        self.dict = {'title': None, 'author': None, 'year': None}

        self.thisisphdthesis = 0
        self.thisismastersthesis = 0
        self.thisisarticle = 0
        self.thisisbook = 0
        self.thisisinproceedings = 0
        self.thisisincollection = 0
        self.thisisproceedings = 0

        self.whatis = 'useless'

    def startElement(self, name, attrs):

        self._currentdata = name

        if name == 'article':
            self.whatis = 'article'

        elif name == 'phdthesis':
            self.whatis = 'phdthesis'

        elif name == 'book':
            self.whatis = 'book'

        elif name == 'incollection':
            self.whatis = 'incollection'

        elif name == 'mastersthesis':
            self.whatis = 'mastersthesis'

        # TRY
        elif name == 'www':
            self.whatis = 'useless'

        # elif name == 'inproceedings':
        #     self.thisisinproceedings += 1
        # elif name == 'proceedings':
        #     self.thisisproceedings += 1

    def add_DBType(self, number):

        if number == 4:
            writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['year'],
                                typeb='article')

        elif number == 0:
            writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['year'],
                                typeb='phdthesis')

        elif number == 3:
            writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['year'],
                                typeb='incollection')
        elif number == 2:
            writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['year'],
                                typeb='book')


        elif number == 1:
            writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['year'],
                                typeb='mastersthesis')

        self.dict['author'] = None
        self.dict['title'] = None
        self.whatis = 'useless'

    def endElement(self, name):
        # TRY
        if self.whatis == 'useless':
            return None

        else:
            if self._currentdata == 'author':
                self.dict['author'] = self._author
            elif self._currentdata == 'title':
                self.dict['title'] = self._title
            elif self._currentdata == 'year':
                self.dict['year'] = self._year

                if self.whatis == 'article':
                    self.add_DBType(4)

                elif self.whatis == 'phdthesis':
                    self.add_DBType(0)

                elif self.whatis == 'book':
                    self.add_DBType(2)

                elif self.whatis == 'incollection':
                    self.add_DBType(3)

                elif self.whatis == 'mastersthesis':
                    self.add_DBType(1)

        if self.whatis is not 'useless':
            if self._currentdata == 'author':
                self._author = ''
            elif self._currentdata == 'title':
                self._title = ''

        self._currentdata = ''

    def characters(self, content):
        if self.whatis is not 'useless':
            if self._currentdata == 'author':
                self._author = self._author+content
            elif self._currentdata == 'title':
                self._title = self._title+content
            elif self._currentdata == 'year':
                self._year = content

    def endDocument(self):
        print('---------------------------------------------------------------')
        # print('Incollections :', self.thisisincollection)
        # print('Inproceed : ', self.thisisinproceedings)
        # print('Book : ', self.thisisbook)
        # print('Article : ', self.thisisarticle)
        # print('WWWW : ', self.thisiswww)
        # print('MasterT. : ', self.thisismastersthesis)
        # print('PhdT. : ', self.thisisphdthesis)
        # print('Proceed. : ', self.thisisproceedings)
        # print('\nTotal : ---->', self.thisisincollection+self.thisisinproceedings+self.thisisbook\
        #       +self.thisisarticle+self.thisismastersthesis+self.thisisphdthesis\
        #       +self.thisisproceedings)
        start_c = time.clock()
        writer.commit()
        end_c = time.clock()
        print("Commit time : ", end_c - start_c)


start = time.clock()
# just a try for now
schema = Schema(title=TEXT(stored=True),
                year=KEYWORD(stored=True),
                author=TEXT(stored=False),
                typeb=KEYWORD(stored=True))

###### parsing and indexing

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
writer = ix.writer()
parser = S.make_parser()
handler = ArticleHandler()
parser.setDTDHandler("dblp.dtd")
parser.setContentHandler(handler)
parser.parse("dblp.xml")

end = time.clock()
print("Total time : ", end-start)

###### search

ix = open_dir("indexdir")
print(ix.schema)
with ix.searcher() as searcher:
    # types of query
    # query = QueryParser("title", schema=ix.schema).parse(u"title:Design AND author:Baltasar")
    # query = QueryParser("title", schema=ix.schema).parse(u"title:Implementierung und typeb=mastersthesis")
    query2 = QueryParser("typeb", schema=ix.schema).parse(u"typeb:article")
    query = QueryParser("author", schema=ix.schema).parse(u"author:Robert")
    # query2 = QueryParser("author", schema=ix.schema).parse(u"author:Peter Hogenkamp")
    results = searcher.search(query, limit=None)
    results2 = searcher.search(query2, limit=5)
    for i in results:
        print(i)
    print('_______________________________________________________')
    for i in results2:
        print(i)

##### show all of doc (careful here)

#ix = open_dir('indexdir')
print(ix.doc_count())
#results = ix.searcher().search(Every('title'))
#print(ix.schema)
#for result in results:
#    print("Rank: %s Title: %s Author: %s" % (result.rank, result['title'], result['author']))


