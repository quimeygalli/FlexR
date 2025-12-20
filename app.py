from flask import Flask, session, render_template, request
from flask_session import Session 
from cachelib.file import FileSystemCache

app = Flask(__name__)

# ONLY FOR DEVELOPMENT  ->
#---
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
#---

# Session config ->

app.config['SESSION_TYPE'] = "cachelib"
app.config['SESSION_PERMANENT'] = True
SESSION_CACHELIB = FileSystemCache(threshold=500, cache_dir="/sessions"),
app.config.from_object(__name__)

Session(app)