To run this website you must have flask, sqlalchemy, flask_sqlalchemy
as well as python 3 installed. If you need python3 the anaconda distribution has
all of these libraries pre installed so I recommend anaconda python 3. 

For the libraries run these commands to get them installed / updated:

+ pip3 install flask
+ pip3 install SQLAlchemy
+ pip3 install flask_sqlalchemy

The fake database requires some first time set up, run setup.py in /website to set it up.

The main file of this repo is fake_server.py in the website folder, to run the server run this python file once first time setup is complete.


If anything breaks for you or it won't run for some reason let me know.

This server takes 6 description files and ties them to with 8 fake MD/NGS files to
show how a fully built search page for the meta data platform might perform.


TODO:

+ Improve search page front end
+ Rewrite query_db so that documents are not indexed for every query
+ More accuartely comment search_engine.py
+ migrate from sqlite to MySQL# GEMSEC_web_protoype
