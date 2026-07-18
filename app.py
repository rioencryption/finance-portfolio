from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import yfinance as yf
import os # NEW: Import the OS module to read environment variables

app = Flask(__name__)

# --- DATABASE MIGRATION LOGIC ---
# Grab the database URL from the environment if it exists. 
# If it doesn't exist (like on your local laptop), default to SQLite.
db_url = os.environ.get("DATABASE_URL", "sqlite:///portfolio.db")

# Crucial Fix: SQLAlchemy 1.4+ requires the URL to start with "postgresql://" 
# but many cloud providers still provide URLs starting with "postgres://"
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ... (The rest of your code remains exactly the same!) ...