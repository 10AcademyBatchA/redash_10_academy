import psycopg2
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

class ConnectToPostgres:
    load_dotenv()
    db_host = os.getenv("POSTGRES_HOST")
    db_user = os.getenv("POSTGRES_USER")
    db_port = os.getenv("POSTGRES_PORT")
    db_database = os.getenv("POSTGRES_DB")
    db_params = {
    'host': db_host,
    'user': db_user,
    'port': db_port,
    'database': db_database
    }

    def __init__(self):
        try:
            self.engine = create_engine(f"postgresql+psycopg2://{self.db_params['user']}@{self.db_params['host']}:{self.db_params['port']}/{self.db_params['database']}")
        except Exception as error:
            raise Exception("Cannot connect to the database, Please try again")
    def get_engine(self):
        return self.engine
