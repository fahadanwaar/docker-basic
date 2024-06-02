from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, insert, text
import os

import time

app = Flask(__name__)
print(
    "hello",
    os.getenv("DATABASE_URL"),
    os.getenv("SECRET_KEY"),
    os.getenv("REDIS_URL"),
)
time.sleep(5)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
engine = create_engine("postgresql+psycopg2://postgres:postgres@db:5432/myflaskapp")
# engine = create_engine("postgresql://postgres:postgres@db:5432/myflaskapp")

conn = engine.connect()
api = Api(app)
hash = {1: "hello"}


class Animal(Resource):
    def get(self, id):
        return {"value": hash.get(id)}


class DatabaseQuery(Resource):
    def get(self):
        query = text(
            "INSERT INTO test_table (_name, surname) VALUES ('Fahad', 'Anwaar');"
        )
        conn.execute(query)
        conn.commit()
        print("done")
        return {"status": "completed"}


api.add_resource(Animal, "/animals/<int:id>")
api.add_resource(DatabaseQuery, "/animals/db")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
