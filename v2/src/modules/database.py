DB_DRIVER = "ODBC Driver 18 for SQL Server"
DB_SERVER = "localhost"            # o "host,port"
DB_NAME = "demo_api"
DB_ENCRYPT = "no"                       # para pruebas locales: "no"
# DB_ENCRYPT = "yes;TrustServerCertificate=yes"  # alternativa con cifrado auto-firmado

import pyodbc
import re
from box import Box
from jinja2 import Template
from enum import Enum

from modules.formatter import FormatterAgent

formatter_agent = FormatterAgent()

class Database:
    def __init__(self, conn_str=None):
        self.conn_str = conn_str
        self.conn = None
        self.cursor = None

    @staticmethod
    def build_conn_str(user: str, password: str):
        return (
            f"DRIVER={{{DB_DRIVER}}};"
            f"SERVER={DB_SERVER};"
            f"DATABASE={DB_NAME};"
            f"UID={user};PWD={password};"
            f"Encrypt={DB_ENCRYPT};"
        )

    def connect(self):
        if self.conn is None:
            self.conn = pyodbc.connect(self.conn_str, timeout=5)
            self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None