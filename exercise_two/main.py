from flask import Flask
from controller import Routes
from repository import Repository
from connector import ConnectorDatabase

if __name__ == '__main__':
    app = Flask(__name__)

    connector = ConnectorDatabase(
        host="localhost",
        user="root",
        password="root",
        database="estudiantes",
        port=3307
    )

    repository = Repository(connector)

    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=8080)
