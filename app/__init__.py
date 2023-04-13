"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqc41mbg5e4khrs440-a.oregon-postgres.render.com",
        database="todo_cyxg",
        user="root",
        password="IGqtfwi4u6VHP3MCWpwDDLSL2xr3nufh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
