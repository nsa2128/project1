#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)



# XXX: The Database URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@<IP_OF_POSTGRE_SQL_SERVER>/<DB_NAME>
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@<IP_OF_POSTGRE_SQL_SERVER>/postgres"
#
# For your convenience, we already set it to the class database

# Use the DB credentials you received by e-mail
DB_USER = "nsa2128"
DB_PASSWORD = "s9xyf567"

DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"

DATABASEURI = "postgresql://nsa2128:s9xyf567@w4111.cisxo09blonu.us-east-1.rds.amazonaws.com/w4111"


#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)


# Here we create a test table and insert some values in it
engine.execute("""DROP TABLE IF EXISTS test;""")
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")

#login and logout script
def login(client, username, password):
    return client.post('/login', data=dict(
        username=test,
        password=test
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)

#USERS
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Users (id User_ID PRIMARY KEY VARCHAR(255), Location VARCHAR(255), Email VARCHAR(255), Name VARCHAR(255))")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Users (User_ID, Location, Email, Name) VALUES (%s, %s, %s, %s)"
val = [
  ('1607021983999', 'New York, NY', 'auctor.velit@fringillaornare.edu','Erich Shepherd'),
  ('1674102716999', 'Trenton, NJ','turpis.nec.mauris@Nullamvitaediam.com','Kadeem Chen'),
  ('1629061975899', 'Hartford, CT','turpis.In.condimentum@Aliquam.com','Nadine Morgan'),
  ('1623070645399', 'Pittsburgh, PA','velit.dui@est.co.uk','Alec Massey'),
  ('1666112356499', 'Brooklyn, NY','elit.erat@magnaSed.ca','Hedwig Guzman'),
  ('1655081999499', 'Queens, New York','ultricies@odio.net','Kirk Estrada'),
  ('1670022307799', 'Staten Island, NY','consequat.enim.diam@sed.edu','Quinn Cameron'),
  ('1625050981299', 'Bronx, NY','Quisque.varius.Nam@fermentummetus.com','Abel Monroe'),
  ('1662091137999', 'Montpelier, VT','vestibulum@dolor.net','Destiny Hayden'),
  ('1641062295399', 'Augusta, ME','risus@magnisdisparturient.edu','Shad Stanley'),
]

mycursor.executemany(sql, val)

mydb.commit()

#Elected Officials
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Elected_Official(id User_ID PRIMARY KEY VARCHAR(255), Area_Represented VARCHAR(255), Date_Elected VARCHAR(255), Name VARCHAR(255), Reelection_Date VARCHAR(255), Voting_Record VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Elected_Official (Name, Area_Represented, Date_Elected, Reelection_Date, Voting_Record, User_ID) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
  ('Joy Dunn','New York, NY','Jul 29, 2018','Aug 10, 2020','Votes with President Trump 10% of time','1611011500199'), 
  ('Quamar Mccullough','Hartford, CT','Dec 6, 2017','Sep 2, 2020','Votes with President Trump 22% of time','1649041495499'),
  ('Chelsea Salazar','Concord, NH','Apr 2, 2018','Apr 27, 2020','Votes with President Trump 81% of time','1685121867299'),
  ('Guinevere Watts','Pittsburgh, PA','Apr 6, 2018','May 12, 2020','Votes with President Trump 54% of time','1673080540299'),
  ('Noah Wright','Brooklyn, NY','Nov 21, 2017','Nov 6, 2019','Votes with President Trump 18% of time','1609052156299'),
  ('Theodore Mcclure','Staten Island, NY','Dec 19, 2017','May 20, 2020','Votes with President Trump 60% of time','1655031946399'),   ('Theodore Ramsey','Bronx, NY','Jul 29, 2018','Jun 23, 2020','Votes with President Trump 90% of time','1656092668799'),
  ('Plato Warren','Montpelier, VT','Aug 28, 2018','Feb 25, 2020','Votes with President Trump 28% of time','1631100493399'),
  ('Lani Cortez','Augusta, ME','May 9, 2018','Mar 29, 2020','Votes with President Trump 60% of time','1652032782899'),
  ('Halee Velez','Trenton, NJ','Dec 4, 2017','Aug 10, 2020','Votes with President Trump 95% of time','1681041285299'),
]

mycursor.executemany(sql, val)

mydb.commit()


#Candidate
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Candidate (id User_ID PRIMARY KEY VARCHAR(255), Biography VARCHAR(255), Name VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Candidate (Biography, Name, User_ID) VALUES (%s, %s, %s)"
val = [
  ('Dale Higgins is a Republican from New York.','Dale Higgins','1683121782299'),
  ('Gray Love is a Democrat from New Jersey.','Gray Love','1626012009099'),
  ('Nita Alford is an Independent from Maine.','Nita Alford','1693013074799'),
  ('Burton Watkins is a Democrat from Vermont.','Burton Watkins','1694022326299'),
  ('Edan Valenzuela is a Democrat from New York.','Edan Valenzuela','1660041338099'),
  ('Steven Holloway is a Republican from New Jersey.','Steven Holloway','1642120713599'),
  ('Herrod Alford is an Independent from New York.','Herrod Alford','1638041876699'),
  ('Zane Cooper is a Democrat from New York.','Zane Cooper','1689050694199'),
  ('Madeson Santana is a Republican from Connecticut.','Madeson Santana','1674082738899'),
  ('Vielka Conley is a Democrat from New York.','Vielka Conley','1665020853899')
]

mycursor.executemany(sql, val)

mydb.commit()


#Voter
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Voter (id User_ID PRIMARY KEY VARCHAR(255), Voter_ID VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Voter (User_ID, Voter_ID) VALUES (%s, %s)"
val = [
  ('22313673099','1601021471299'),
  ('35851273299','1679122048599'), 
  ('85286035299','1643121220899'), 
  ('48656916499','1653082526899'),
  ('03291258699','1680091382599'), 
  ('97970750399','1649081252599'),
  ('29777992599','1619021367499'), 
  ('35950233099','1657101651299'), 
  ('29647432199','1667071401599'), 
  ('40641032299','1668051827099')

]

mycursor.executemany(sql, val)

mydb.commit()


#Political Party
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Political_Party (id Name_of_Party PRIMARY KEY VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Political_Party (Name_of_Party) VALUES (%s)"
val = [
  ('Democrat'),
  ('Republican'),
  ('Independent'),
]

mycursor.executemany(sql, val)

mydb.commit()


#User Party Affiliation
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE User_Party_Affiliation (id User_ID PRIMARY KEY VARCHAR(255), Name_of_Party VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO User_Party_Affiliation (Name_of_Party, User_ID) VALUES (%s, %s)"
val = [
  ('Republican','1647112658699'),
  ('Democrat','1644110133199'),
  ('Independent','1663081568199'),
  ('Republican','1653052616099'), 
  ('Independent','1620090721699'), 
  ('Democrat','1649070683199'), 
  ('Republican','1650100895499'),
  ('Independent','1603080366699'),
  ('Democrat','1673040411199'), 
  ('Republican','1605051122199')
]

mycursor.executemany(sql, val)

mydb.commit()


#Election
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Election (id Location PRIMARY KEY VARCHAR(255), Date VARCHAR(255), Type VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Election (Location, Date, Type) VALUES (%s, %s, %s)"
val = [
  ('1690 Tellus Ave','2020-11-03','Presidential'),
  ('283 Dictum Road','2020-11-03','Presidential'), 
  ('732 Risus. Rd.','2020-11-03','Presidential'), 
  ('7021 Arcu. Ave','2018-11-06','Midterm'),
  (' 5000 Nec St.','2020-11-03','Presidential'), 
  (' 5071 Mauris Av.','2018-11-06','Midterm'), 
  ('4870 Dui. Rd.','2018-11-06','Midterm'), 
  ('4258 Sodales St.','2018-11-06','Midterm'), 
  (' 3061 Vitae Rd.','2020-11-03’, ‘Presidential’), 
  (' 9297 Donec Rd.','2018-11-06','Midterm')


mycursor.executemany(sql, val)

mydb.commit()


#Participates In
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Participates_In (id User_ID PRIMARY KEY VARCHAR(255), Location VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Participates_In (User_ID, Location) VALUES (%s, %s)"
val = [
  ('1607021983999','New York, NY'), 
  ('1674102716999','Trenton, NJ'), 
  ('1629061975899','Hartford, CT'), 
  ('1623070645399','Pittsburgh, PA'), 
  ('1666112356499','Brooklyn, NY'), 
  ('1655081999499','Queens, New York'), 
  ('1670022307799','Staten Island, NY'), 
  ('1625050981299','Bronx, NY'), 
  ('1662091137999','Montpelier, VT'), 
  ('1641062295399','Augusta, ME')
]

mycursor.executemany(sql, val)

mydb.commit()


#Discussion Thread
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Discussion_Thread (id Topic PRIMARY KEY VARCHAR(255), Category VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Discussion_Thread (Topic, Category) VALUES (%s, %s)"
val = [
 ('Voting Rights','Will Florida vote to restore voting rights to those formerly convicted of crimes?'),
 ('Climate Change', 'UN climate Change Report'),
 ('Electoral College','Should we get rid of the Electoral College?'), 
 ('The Supreme Court','Did Brett Kavanaugh deserve to be confirmed?'),
 ('Climate Change','What can we do to help mitigate climate change?'), 
 ('Affirmative Action','Harvard Anti-Asian Bias Case'), 
 ('Party Division','Do true Independents still exist?'), 
 ('Gender Equality','The Wage Gap'), 
 ('Healthcare','Will Republicans vote to repeal Obamacare if they keep the House after the midterm elections?'),
 ('Immigration','Trump’s Travel Ban 3.0')

]

mycursor.executemany(sql, val)

mydb.commit()


#User Posts Messages
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE User_Posts_Messages (id Topic PRIMARY KEY VARCHAR(255), User_ID VARCHAR(255), Name VARCHAR(255), Category VARCHAR(255), Time datetime)")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO User_Posts_Messages (User_ID, Name, Category, Topic, Time) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('1607021983999','Erich Shepherd','Voting Rights','Will Florida vote to restore voting rights to those formerly convicted of crimes?', '8:00 AM'),
  ('1674102716999','Kadeem Chen','Climate Change', 'UN Climate Change Report', '9:00 AM'),
  ('1629061975899','Nadine Morgan','Electoral College','Should we get rid of the Electoral College?', '10:00 AM'),
  ('1623070645399','Alec Massey','The Supreme Court','Did Brett Kavanaugh deserve to be confirmed?', '11:00 AM'),
  ('1666112356499','Hedwig Guzman','Climate Change','What can we do to help mitigate climate change?','12:00 PM'),
  ('1655081999499','Kirk Estrada','Affirmative Action','Harvard Anti-Asian Bias Case', '1:00 PM'),
  ('1670022307799','Quinn Cameron','Party Division','Do true Independents still exist?', '2:00 PM'),
  ('1625050981299','Abel Monroe','Gender Equality','The Wage Gap', '3:00 PM'),
  ('1662091137999','Destiny Hayden','Healthcare','Will Republicans vote to repeal Obamacare if they keep the House after the midterm elections?','4:00 PM'),
  ('1641062295399','Shad Stanley','Immigration','Trump’s Travel Ban 3.0', '5:00 PM')
]

mycursor.executemany(sql, val)

mydb.commit()


#Rates
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Rates (id Name PRIMARY KEY VARCHAR(255), Rating PRIMARY KEY INT, User_ID VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Rates (Name, User_ID, Rating) VALUES (%s, %s, %s)"
val = [
  ('Dale Higgins','1683121782299','1') 
  ('Gray Love','35851273299', '1'), 
  ('Nita Alford','85286035299', '2'), 
  ('Burton Watkins','48656916499', '2'), 
  ('Edan Valenzuela','03291258699', '3'),
  ('Steven Holloway','97970750399', '3'), 
  ('Herrod Alford','29777992599', '4'), 
  ('Zane Cooper', '35950233099', '4'), 
  ('Madeson Santana','29647432199', '5'), 
  ('Vielka Conley','40641032299', '5')

]

mycursor.executemany(sql, val)

mydb.commit()


#Represented By
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Represented_By (id User_ID PRIMARY KEY VARCHAR(255), Area_Represented PRIMARY KEY VARCHAR(255), Name VARCHAR(255))")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nsa2128",
  passwd="s9xyf567",
  database="w4111"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Represented_By (Voter_ID, Area_Represented VALUES (%s, %s)"
val = [
  ('22313673099','New York, NY'), 
  ('35851273299','Hartford, CT'), 
  ('85286035299','Concord, NH'), 
  ('48656916499','Pittsburgh, PA'), 
  ('03291258699','Brooklyn, NY'), 
  ('97970750399','Staten Island, NY'),
  ('29777992599','Bronx, New York'), 
  ('35950233099','Montpelier, VT'), 
  ('29647432199','Augusta, ME'), 
  ('40641032299','Trenton, NJ')
]

mycursor.executemany(sql, val)

mydb.commit()


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to e.g., localhost:8111/foobar/ with POST or GET then you could use
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print request.args


  #
  # example of a database query
  #
  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #
  context = dict(data = names)


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html", **context)

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another
#
# notice that the functio name is another() rather than index()
# the functions for each app.route needs to have different names
#
@app.route('/another')
def another():
  return render_template("anotherfile.html")


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  print name
  cmd = 'INSERT INTO test(name) VALUES (:name1), (:name2)';
  g.conn.execute(text(cmd), name1 = name, name2 = name);
  return redirect('/')


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
