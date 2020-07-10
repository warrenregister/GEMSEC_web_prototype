'''
This class implements a basic search engine on local files
'''

from document import Document
import os
import math
import re


class SearchEngine():
    def __init__(self, documents):
        '''
        Method to initialize Search Engine object and analyze each document in
        given directory to create inverse index with the words as keys and
        a list of each document containting each word as the values.
        '''
        self._docs = documents
        self._inverse_index = {}
        for doc in self._docs:
            for word in doc.get_words():
                if word not in self._inverse_index:
                    self._inverse_index[word] = []
                self._inverse_index[word].append(doc)
        self._docs = len(self._docs)

    def _calculate_idf(self, term):
        '''
        Returns the inverse document frequency of a given term in the corpus
        of documents in the directory this object was initialized upon. If the
        given term is not in corpus, returns 0.
        '''
        if term in self._inverse_index:
            return math.log(self._docs / len(self._inverse_index[term]))
        else:
            return 0

    def search(self, terms):
        '''
        Returns a list of all documents containing the given term(s) sorted by
        the Term Frequency * Inverse Document Frequency of the term(s). If the
        given term(s) is / are not in any documents, returns None.
        '''
        terms = [re.sub(r'\W+', '', term.lower()) for term in terms.split()]
        rankings = []
        rel_docs = set()
        for term in terms:
            if term in self._inverse_index.keys():
                rel_docs = set(list(rel_docs) + self._inverse_index[term])

        if len(rel_docs) == 0:
            return None

        for doc in rel_docs:
            tfidf = 0
            for term in terms:
                tfidf += doc.term_frequency(term) * self._calculate_idf(term)
            rankings.append((doc.get_entry(), tfidf))
        rankings.sort(key=lambda x: x[1], reverse=True)
        return([x[0] for x in rankings])