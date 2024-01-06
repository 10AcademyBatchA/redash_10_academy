from flask import request, jsonify
from redash.handlers.base import (
    BaseResource
)
import os
# from openai import OpenAI
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
os.environ['OPENAI_API_KEY'] = os.environ.get("OPENAI_API_KEY")
# client = OpenAI(
#   api_key=VARIABLE_KEY
# )
connection_params = {
  "host": "192.168.43.74",
  "user": "postgres",
  "port": "15432",
  'password': '',
  "database":"redash_open_ai"
}

def get_value_from_llm(question):
    question = "is fanuel present in the database?"
    db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}",
    )
    llm = OpenAI(temperature=0, verbose=False)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)
    answer = db_chain.run(question)
    return answer

class ChatResource(BaseResource):

    def post(self):
        try:
            value = request.get_json()
            question = value.get('question')
            print("Question: "+question)
            answer = get_value_from_llm(question)
            print("Answer: "+answer)
            response_data = {"answer": "Whatever"}
            return jsonify(response_data), 200
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500
        
