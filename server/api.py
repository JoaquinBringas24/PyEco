from flask import Blueprint
from regression import regression_blueprint
from ai import ai_blueprint
api_blueprint = Blueprint('api', __name__)

api_blueprint.register_blueprint(regression_blueprint)
api_blueprint.register_blueprint(ai_blueprint)
