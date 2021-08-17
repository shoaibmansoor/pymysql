from flask import request
from flask_restful import Resource
from Model import db, DetailsSchema, Details
import json

details_schema = DetailsSchema(many=True)
detail_schema = DetailsSchema()


class DetailsResource(Resource):

    @staticmethod
    def get():
        datails = Details.query.all()
        detailes = details_schema.dump(datails)
        return {'status': 'success', 'data': detailes}, 200

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate data and deserialize inputs
        response = json.dumps(json_data)
        data = detail_schema.loads(response).data
        detail = Details.query.filter_by(address=data['address']).first()

        if detail:
            return {'message': 'Location already exists'}, 400

        detail = Details(
            age=data['age'],
            address=data['address'],
            country_origin=data['country_origin']
        )

        db.session.add(detail)
        db.session.commit()

        result = detail_schema.dump(detail)

        return {'status': 'success', 'data': result}, 201
