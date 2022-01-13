from flask import Flask
from flask_restful import Resource, Api
# pip install flask_restful

app = Flask(__name__)

api = Api(app)

people = []

class People(Resource):
    def get(self,value):
        for person in people:
            if person == value:
                return {'person found: ': person}
        return {'result: ':'person not found'}

    def post(self,value):
        person = value
        people.append(person)
        return {'result: ': 'person added successfully'}

    def delete(self,value):
        for index, person in enumerate(people):
            if person == value:
                people.pop(index)
                return {'result: ': 'person deleted successfully'}

class ListPeople(Resource):
    def get(self):
        return {'people: ':people}

api.add_resource(People,'/people/<string:value>')
api.add_resource(ListPeople, '/listPeople')

if __name__ == '__main__':
    app.run(debug=True)
