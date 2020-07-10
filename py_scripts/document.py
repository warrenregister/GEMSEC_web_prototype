'''
This class implements the Document class which provides functionality for
understanding and analyzing the contents of local documents.
'''

import re


class Document():
    def __init__(self, file_names, code, entry):
        '''
        Initializes Document object with a dictionary of each unique token
        in the given file and its frequency in that file.

        name: file path of a document
        '''
        self._file_names = file_names
        self._terms = {}
        self._code = code
        self._entry = entry
        for file_name in self._file_names:
            with open(file_name) as f:
                words = f.read().split()
                for word in words:
                    word = self._ignore_case_punct(word)
                    if word not in self._terms:
                        self._terms[word] = 0
                    self._terms[word] += 1 / len(words)

    def term_frequency(self, term):
        '''
        Returns the frequency of a given term in the docment initialized upon,
        if the term isn't in the document, returns 0.
        '''
        term = self._ignore_case_punct(term)
        return(self._terms[term] if term in self._terms else 0)

    def get_path(self):
        '''
        Returns the path of the document.
        '''
        return self._file_name

    def get_words(self):
        '''
        Returns a list of the unique terms in the document.
        '''
        return list(self._terms.keys())
    
    def get_code(self):
        '''
        Returns description file code.
        '''
        return self._code

    def get_file_id(self):
        '''
        Returns file_id for file being represented by description files.
        '''
        return self._entry.file_id

    def get_entry(self):
        '''
        Returns row object from database.
        '''
        return self._entry

    def _ignore_case_punct(self, word):
        '''
        Takes in a string and returns the string in lower case with any
        punctuation removed.
        '''
        return re.sub(r'\W+', '', word.lower())