################################################################################
# IMPORTS
import os
# import sqlite3
from flask import Flask, request, render_template
# WORD IMPORTS
import string

from secret_keys import CSRF_SECRET_KEY

###############################################################################

app = Flask('shucks') # create the application instance :)
app.config.from_object(__name__) # load config from this file, shucks.py

# Load default config and override config from an environment variable
app.config.update(dict(
 SECRET_KEY=CSRF_SECRET_KEY
))

################################################################################

@app.route('/',)
def default():
    """Load the basic page"""
    error=None
    return render_template('index.html',error=error)
    
@app.route('/results', methods=['POST'])
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
        result_miss=hyphen(q,words)
        if result_miss:
            return render_template('results.html',q=q,result_miss=result_miss)
        else:
            error = "No words found for " + q
            return render_template('results.html',q=q,error=error)
    
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
        return missing[word]
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


