from flask import Blueprint, json, request
from regression import regression_blueprint

api_blueprint = Blueprint('api', __name__)

api_blueprint.register_blueprint(regression_blueprint)

