################################################################################
# IMPORTS
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# WORD IMPORTS
import string

###############################################################################

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file, shucks.py

# Load default config and override config from an environment variable
app.config.update(dict(
 SECRET_KEY='development key'
))

################################################################################

@app.route('/',)
def default():
    """Load the basic page"""
    error=None
    return render_template('layout.html',error=error)
    
@app.route('/', methods=['POST'])
def get_query():
    error=None
    
    q = request.form['q']
    q = q.lower()
    
    wordsfile = file("static/newSCOWL.txt")
    words = wordsfile.readlines()
    words = [i.split('\n',1)[0] for i in words]
    for i in words:
        i = i.lower()
    
    # SPACES
    if " " in q:
        error = q + " contains a space."
        return render_template('results.html',error=error)
    
    # HYPHENS
    elif "-" in q:
        result_miss, length=hyphen(q,words)
        if result_miss:
            return render_template('results.html',result_miss=result_miss,length=length)
        else:
            result_miss = "No words found for " + q
            return render_template('results.html',result_miss=result_miss)
    
    # VALID WORD
    else:
        result_anag=anagram(q,words)
        if not in_dict(q,words):
            error=q + " is not in the word list."
            return render_template('results.html',q=q,error=error,result_anag=result_anag)
        else:
            return render_template('results.html',val_q=q,q=q,result_anag=result_anag)
        
        
################################################################################
# WORD FUNCTIONS
def valid_char(word):
    # 'word' must be all lowercase
    for i in list(word):
        if i in string.ascii_lowercase:
            return True
        else:
            return False

def in_dict(word, words):
    # 'word' must be all lowercase
    if word in words:
        return True
    else:
        return False
        
def hyphen(word, words):
    hyphens = []
    for i in range(len(word)):
        if word[i] == '-':
            hyphens.append(i)
    missing = {}
    for i in words:
        if len(i) == len(word):
            key = list(i)
            for j in hyphens:
                key[j] = '-'
            key = ''.join(key)
            key = key.lower()
            if key in missing:
                missing[key].append(i)
            else:    
                missing[key] = [i]
    if word in missing:
        return [missing[word],len(missing[word])]
    else:
        return

def anagram(word, words):
    anag = {}
    
    for i in words:
        key = list(i)
        key.sort()
        key = ''.join(key)
        key = key.lower()
        if key not in anag:
            anag[key] = [i]
        else:
            anag[key].append(i)
    
    tmp = list(word)
    tmp.sort()
    tmp = ''.join(tmp)
    
    if tmp in anag:
        result = anag[tmp]
        if word in anag[tmp]:
            result.remove(word)
    else:
        result=[]

    return result


################################################################################
# FLASKR FUNCTIONS

#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#
# def connect_db():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv
#
# def init_db():
#     db = get_db()
#     with app.open_resource('schema.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#
# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print('Initialized the database.')
#

# @app.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     db = get_db()
#     db.execute('insert into entries (title, text) values (?, ?)',
#                  [request.form['title'], request.form['text']])
#     db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('show_entries'))
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html', error=error)
#
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('show_entries'))
#
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db
#
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()