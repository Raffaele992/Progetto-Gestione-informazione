# uncompyle6 version 3.2.4
# Python bytecode 3.5 (3350)
# Decompiled from: Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
# [GCC 5.4.0 20160609]
# Embedded file name: /home/riccardo/Lev_dist.py
# Compiled at: 2018-12-19 15:46:22
# Size of source mod 2**32: 1675 bytes

import stringdist
from nltk import tokenize, pos_tag
from nltk.corpus import stopwords
import time


Personaltokenizer = tokenize.RegexpTokenizer('\\w+')
possible_results = []

def evaluate_query(query, R, pos, vocab):

    start = time.clock()
    
    if len(query) <= 85 and len(query) > 0:
        query = query.lower()
        query = Personaltokenizer.tokenize(query)
        print('Query as inserted lower case: ', query)
        filtered_query = [word for word in query if word not in stopwords.words('english')]
        print('Filtered query : ', filtered_query)
        filtered_tagged_query = pos_tag(filtered_query)
        print('Tagged query : ', filtered_tagged_query)
        pt_of_interest_q = [word for word, tag in filtered_tagged_query if tag.startswith('VB') or tag.startswith('N')]
        print('Interested : --->   ', pt_of_interest_q)

        if R / len(filtered_query) <= 10:
            pass
        end = time.clock()
        print(end-start)
        return possible_results

    else:
        print('Insert a new query')
        end = time.clock()
        print(end-start)
        return possible_results

evaluate_query("Amazing we love Marco, zitronen und hub, love_man 2 be4re!",0,0,0)

# okay decompiling /home/riccardo/__pycache__/Lev_dist.cpython-35.pyc
