'''
File contains method for making sql query to database.
'''

import pandas as pd
from document import Document
from search_engine import SearchEngine


def get_descriptions(Descriptions):
    '''
    Returns the code and file path each file in the Descriptions
    table in an SQLite database.
    Arguments ----
    Descriptions: SQLAlchemy object for Descriptions table
    '''
    descs = Descriptions.query.all()
    tups = []
    for desc in descs:
        tups.append((desc.code, desc.file_loc))
    return tups

def get_codes(tables):
    '''
    Returns the result of a query of tables in an SQLite databse for their
    codes and file_ids.
    Arguments ----
    tables: list of SQLAlchemy table objects in SQLite databse.
    '''
    entries = []
    files = []
    for table in tables:
        entries += table.query.all()
    return entries


def generate_documents(files, descs):
    '''
    Returns Document objects generated for files stored in the SQLite
    database based on their associated description files.

    Arguments ----
    files: list of file_ids and codes for files in SQLite database.
    descs: list of codes and file paths for description files stored in
    SQLite database.
    '''
    docs = []
    for file in files:
        codes = file.code
        rel_descs = []
        for desc in descs:
            if desc[0] in codes:
                rel_descs.append(desc[1])
        docs.append(Document(rel_descs, file.code, file))
    return docs
        

def query_results(results, tables):
    '''
    Returns results of query for files which match results of search engine
    query.

    Arguments ----
    results: Output of search engine, ranked list of files based on
    relatedness to inputed search query.
    cursor: SQLlite connection cursor on databse with given information.
    '''
    table_data = []
    tables_str = ['ngs', 'md']
    for id in results:
        for i, table in enumerate(tables):
            if tables_str[i] == id.split('_')[0]:
                result = table.query.filter_by(file_id=id).first()
                table_data.append(result)
    return table_data



def query_db(query, tables, Descriptions):
    files = get_codes(tables)
    desc_files = get_descriptions(Descriptions)
    docs = generate_documents(files, desc_files)


    engine = SearchEngine(docs)
    search_results = engine.search(query)

    return search_results


if __name__ == '__main__':
    query_db('warren register, ngs')

