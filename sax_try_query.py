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


class PubblicationHandler(S.ContentHandler):
    
    def __init__(self):

        self._currentdata = ''
        self._title = ''
        self._author = ''
        self._date = ''
        self._publisher = ''
        self._journal = ''
        self._booktitle = ''
        self._type = ''
        self.dict = {'title': None, 'author': None, 'date': None, 'publisher': None, 'journal': None, 'booktitle': None, 'type': None}


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
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisismastersthesis += 1
            self.whatis = name
        elif name == 'article':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisarticle += 1
            self.whatis = name
        elif name == 'book':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisbook += 1
            self.whatis = name
        elif name == 'www':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisiswww += 1
            self.whatis = name
        elif name == 'inproceedings':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisinproceedings += 1
            self.whatis = name
        elif name == 'incollection':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisincollection += 1
            self.whatis = name
        elif name == 'proceedings':
            self._date = attrs['mdate']
            self.dict['date'] = self._date
            self.thisisproceedings += 1
            self.whatis = name
    
    


    def endElement(self, name): 


    
            if self.whatis == 'phdthesis':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'phdthesis':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.whatis = None
                    self.dict['type'] = None
                    self._currentdata = ""    
            
            if self.whatis == 'masterthesis':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'masterthesis':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
            
            if  self.whatis == 'article':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type                
                if name == 'article':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
            
            if   self.whatis == 'book':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'book':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
            
            if  self.whatis == 'WWW':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'WWW':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
            
            if  self.whatis == 'incollection':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'phdthesis':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
    

            if  self.whatis == 'inproceed':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'inproceed':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""            
  
        

        
            if  self.whatis == 'proceed':
                if self._currentdata == 'author':
                    self.dict['author'] = self._author
                elif self._currentdata == 'title':
                    self.dict['title'] = self._title
                elif self._currentdata == 'publisher':
                    self.dict['publisher'] = self._publisher
                elif self._currentdata == 'journal':
                    self.dict['journal'] = self._journal
                elif self._currentdata == 'booktitle':
                    self.dict['booktitle'] = self._booktitle
                elif self._currentdata == 'type':
                    self.dict['type'] = self._type
                if name == 'proceed':
                    if not self.dict['author']:
                        self.dict['author'] = 'unknown'
                    writer.add_document(title=self.dict['title'], author=self.dict['author'], year=self.dict['date'], publisher=self.dict['publisher'], journal=self.dict['journal'], booktitle=self.dict['booktitle'], type=self.dict['type'])
                    self.dict['author'] = None
                    self.dict['date'] = None
                    self.dict['title'] = None
                    self.dict['publisher'] = None
                    self.dict['journal'] = None
                    self.dict['booktitle'] = None
                    self.dict['type'] = None
                    self.whatis = None
                    self._currentdata = ""

                    
         

    def characters(self, content):
        
        if self._currentdata == 'author':
            self._author = content
        elif self._currentdata == 'title':
            self._title = content
        elif self._currentdata == 'date':
            self._date = content
        elif self._currentdata == 'publisher':
            self._publisher = content
        elif self._currentdata == 'journal':
            self._journal = content
        elif self._currentdata == 'booktitle':
            self._booktitle = content
        elif self._currentdata == 'type':
            self._type = content




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
                publisher=TEXT(stored=True),
                journal=TEXT(stored=True),
                booktitle=TEXT(stored=True),    
                type=KEYWORD(stored=True))

####### parsing and indexing

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
writer = ix.writer()
parser = S.make_parser()
handler = PubblicationHandler()
parser.setFeature(S.handler.feature_namespaces, 0)
parser.setFeature(S.handler.feature_external_ges, False)
parser.setContentHandler(handler)
parser.parse("dblp1.xml")

###### search

ix=open_dir("indexdir")
print(ix.schema)
with ix.searcher() as searcher:
     query = QueryParser("content", schema=ix.schema).parse(u"title:implementations")
     results = searcher.search(query,limit=None)
     print(len(results))
     for i in results:
         print(i)

###### show all of doc (careful here)
#ix = open_dir('indexdir')
#print(ix.doc_count())
#results = ix.searcher().search(Every('title'))
#print(ix.schema) 
#for result in results:
#    print("Rank: %s Title: %s Author: %s Year: %s Journal: %s" % (result.rank, result['title'], result['author'], result['year'], result['journal']))

end = time.time()
exec_time = end-start
print(exec_time)
