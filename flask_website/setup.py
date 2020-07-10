from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys, os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class NGS(db.Model):
    '''
    SQLAlchemy Table schema descriptor class for NGS files
    '''
    file_id = db.Column(db.String(10), primary_key=True, nullable=False)
    code = db.Column(db.String(15), nullable=False)
    file_loc = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return'<NGS %r>' % self.file_loc
    
    def __str__(self):
        return 'ngs'


class MD(db.Model):
    '''
    SQLAlchemy Table schema descriptor class for MD files
    '''
    file_id = db.Column(db.String(10), primary_key=True, nullable=False)
    code = db.Column(db.String(15), nullable=False)
    file_loc = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return'<MD %r>' % self.file_loc
    
    def __str__(self):
        return 'md'


class Descriptions(db.Model):
    '''
    SQLAlchemy Table schema descriptor class for Description files
    '''
    code = db.Column(db.String(10), primary_key=True, nullable=False)
    file_loc = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return'<Description %r>' % self.file_loc
    
    def __str__(self):
        return ('descriptions')


def do_insert():
    '''
    Calls insert into function with parameters below.
    '''
    directory = os.path.dirname(sys.path[0])
    ids = ['ngs_0', 'ngs_1', 'md_0', 'md_1', 'md_2', 'md_3', 'md_4']
    paths = ['./ngs/ngs0.csv', './ngs/ngs1.csv', './md/md0.md', './md/md1.md',
            './md/md2.md', './md/md3.md', './md/md4.md',
            directory + '/descriptions/ngs_description.txt', 
            directory + '/descriptions/md_description.txt',
            directory + '/descriptions/parameters_A.txt',
            directory + '/descriptions/parameters_B.txt', 
            directory + '/descriptions/jackson_frank.txt',
            directory + '/descriptions/warren_register.txt']
    codes = ['code1_code5', 'code1_code6', 'code2_code3_code5', 'code2_code3_code6',
            'code2_code4_code5', 'code2_code4_code6', 'code2_code3_code5', 'code1', 
            'code2', 'code3', 'code4', 'code5', 'code6']

    insert_into(ids, paths, codes)


def insert_into(ids, file_paths, codes) :
    '''
    Function which creates test databse by taking in a set number of file
    ids, paths, and codes.
    '''

    for index, path in enumerate(file_paths):
        entry = None
        if index < 2:  # NGS files
            entry = NGS(file_id=ids[index], code=codes[index], file_loc=path)
        elif index < 7:  # MD files
            entry = MD(file_id=ids[index], code=codes[index], file_loc=path)
        else:  # Description files
            entry = Descriptions(code=codes[index], file_loc=path)
        db.session.add(entry)
        db.session.commit()


def main():
    db.create_all()
    do_insert()


if __name__ == '__main__':
    main()