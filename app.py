from flask import Flask, session, render_template, request
from flask_session import Session 
from cachelib.file import FileSystemCache

app = Flask("flexr")

# ONLY FOR DEVELOPMENT  ->
#---
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
#---

# Session config ->

app.config['SESSION_TYPE'] = "cachelib"
app.config['SESSION_PERMANENT'] = True
SESSION_CACHELIB = FileSystemCache(
    cache_dir="./sessions",
    threshold=500, # A maximum of cached sessions
    default_timeout=10 # Seconds a session will last
    ),
app.config.from_object("flexr")

Session(app)

@app.after_request(response)