from flask_restful import Resource, Api
from app import app
from models import db, Category

api = Api(app)

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return {'categories': [ {
            'id': category.id,
            'name': category.name
        } for category in categories]
        }
        

api.add_resource(CategoryResource, '/api/category')