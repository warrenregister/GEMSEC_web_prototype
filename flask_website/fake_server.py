from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys, os
sys.path.insert(0, os.path.dirname(sys.path[0]) + '/py_scripts/')
from make_query import query_db

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search_bar']
        rows = query_db(search_query, [NGS, MD], Descriptions)
        if rows != None:
            return render_template('about.html', results=rows)
        else:
            return render_template('about.html')
    else:
        return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)