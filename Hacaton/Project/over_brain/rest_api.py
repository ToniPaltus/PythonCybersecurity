from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class TopCharts(Resource):
  def get(self):
      return {1: 4}


api.add_resource(TopCharts, '/top/<>')


if __name__ == "__main__":
  app.run(debug=True)

