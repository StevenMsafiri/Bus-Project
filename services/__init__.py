from flask import Blueprint

bus_routes_bp = Blueprint('bus_routes', __name__)

from services.fares_api import *
