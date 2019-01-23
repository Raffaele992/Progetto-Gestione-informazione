import os
import xml.sax
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, BOOLEAN
from whoosh.writing import BufferedWriter
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
import time


class ArticleHandler(xml.sax.ContentHandler):

    papertypes = ['article', 'book', 'inproceedings', 'incollection', 'proceedings', 'phdthesis',
                  'mastersthesis']

    def __init__(self):

        self.authors = []
        self.year = None
        self.text = ''
        self.title = ''
        ###
        self.booktitle = ''
        self.crossref = ''
        self.publisher = []
        self.key = ''
        self.journaled = False
        ###

        self.whatis = ''

        self.sumtimea = 0.0

        self.write = False

        self.dict = {'article': 0, 'book': 0, 'inproceedings': 0, 'incollection': 0, 'proceedings': 0, 'phdthesis': 0,
                     'mastersthesis': 0}

        self.neededinfo = []

        self._PhMthesis = ['author', 'year', 'title']
        self._Book = ['title', 'publisher', 'author']
        self._Incoll = ['author', 'year', 'title', 'crossref']
        self._Inpr = ['title', 'booktitle', 'author', 'crossref']
        self._Proc = ['title', 'publisher', 'crossref']
        self._Artic = ['title', 'year', 'author', 'publisher', 'crossref']  # manca il journal

    def startElement(self, name, attrs):

        if name in self.papertypes:

            if name == 'book' or name == 'proceedings':
                self.key = attrs['key']

            self.whatis = name
            self.authors = []

            ####
            self.title = ''
            self.booktitle = ''
            self.crossref = ''
            self.publisher = []
            ############
            self.text = ''
            ############
            ###

            self.year = None
            self.write = True

            if name == 'article':
                self.neededinfo = self._Artic
            elif name == 'book':
                self.neededinfo = self._Book
            elif name == 'phdthesis' or name == 'mastersthesis':
                self.neededinfo = self._PhMthesis
            elif name == 'incollection':
                self.neededinfo = self._Incoll
            elif name == 'inproceedings':
                self.neededinfo = self._Inpr
            elif name == 'proceedings':
                self.neededinfo = self._Proc

        elif name in self.neededinfo:
            self.text = ''

    def add_DBType(self, authors, year, title, booktitle, crossref, publisher, key, booljournal, string):

        authors = ','.join(authors)
        start_a = time.clock()

        if string == 'article':
            publisher = ','.join(publisher)
            writer.add_document(title=title, author=authors, year=year,
                                publisher=publisher, crossref=crossref,
                                journal=booljournal, typeb=string)

        elif string == 'inproceedings':
            writer.add_document(title=title, author=authors,
                                booktitle=booktitle, crossref=crossref,
                                typeb=string)

        elif string == 'incollection':
            writer.add_document(title=title, author=authors, year=year,
                                crossref=crossref, typeb=string)

        elif string == 'proceedings':
            publisher = ','.join(publisher)
            writer.add_document(title=title, publisher=publisher, thekey=key,
                                crossref=crossref, typeb=string)

        elif string == 'book':
            publisher = ','.join(publisher)
            writer.add_document(title=title, author=authors, publisher=publisher,
                                thekey=key, typeb=string)

        else:  # PHD and Masters
            writer.add_document(title=title, author=authors, year=year,
                                typeb=string)

        end_a = time.clock()
        self.sumtimea += (end_a - start_a)

        if string in self.dict:
            self.dict[string] += 1

    def endElement(self, name):

        if self.write:
            if name == 'author':
                self.authors.append(self.text)

            elif name == 'title':
                self.title = self.text

            elif name == 'year':
                self.year = self.text

            elif name == 'booktitle':
                self.booktitle = self.text

            elif name == 'crossref':
                self.crossref = self.text

            elif name == 'publisher':
                self.publisher.append(self.text)

            elif name == 'journal':
                self.journaled = True

            elif name == self.whatis:
                self.write = False
                self.add_DBType(self.authors, self.year, self.title,
                                self.booktitle, self.crossref,
                                self.publisher, self.key, self.journaled, self.whatis)
                self.key = ''
                self.journaled = False

    def characters(self, chars):
        if self.write:
            self.text += chars

    def endDocument(self):
        print('---------------------------------------------------------------')
        start_c = time.clock()
        writer.commit()
        end_c = time.clock()
        print('Add Time : ', self.sumtimea)
        print("Commit time : ", end_c - start_c)
        print("\n\nDict .....>>>", self.dict)


start = time.clock()
# just a try for now
schema = Schema(title=TEXT(stored=True),
                year=KEYWORD(stored=True),
                author=TEXT(stored=True),
                booktitle=TEXT(stored=True),
                crossref=TEXT(stored=True),
                publisher=TEXT(stored=True),
                thekey=TEXT(stored=True),
                journal=BOOLEAN(stored=True),
                typeb=KEYWORD(stored=True))

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
writer = ix.writer(nproc=4, multisegment=True)
parser = xml.sax.make_parser()
handler = ArticleHandler()
parser.setDTDHandler("dblp.dtd")
parser.setContentHandler(handler)
parser.parse("dblp.xml")
end = time.clock()
print("Total time : ", end-start)
print("IX.count : ", ix.doc_count())
