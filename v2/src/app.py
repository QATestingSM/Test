# app_vuln.py  (vulnerable a propósito)
import os, ast
from dotenv import load_dotenv
import pyodbc
from flask import Flask, jsonify, request
from modules.database import Database 
from modules.formatter import FormatterAgent

from datetime import datetime

load_dotenv()

app = Flask(__name__)

CONN_STR = Database.build_conn_str(*ast.literal_eval(os.getenv("DBCONN")))
db_agent = Database(CONN_STR)

formatter_agent = FormatterAgent()

@app.route('/')
def index():
    if not db_agent or not db_agent.cursor:
        db_agent.connect()
    
    try:
        table = "dbo.profiles"
        columns = "*"
        c_where = "id = ?"
        params = [10]
        
        sql = formatter_agent.format_select(table, columns, c_where)
        
        db_agent.execute_query(sql, params)
        total = db_agent.cursor.fetchone()[0]

        return jsonify({"status": "ok", "profiles_total": total})
    except Exception as e:
        return jsonify({"error": e}), 500