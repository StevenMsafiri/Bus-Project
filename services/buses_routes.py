from flask import Blueprint,jsonify, request, abort
from flask_restx import Api, Resource,fields
from destination_Fares.connection import create_connection # Import the function

bus_routes_bp = Blueprint('bus_routes', __name__)

# Create a Flask-RESTX Api object and attach it to the blueprint
api = Api(bus_routes_bp, version='1.0', title='Bus Routes API',
          description='API for managing and searching bus routes')

# Model for Swagger documentation
bus_route_model = api.model('BusRoute', {
    'FROM': fields.String(description='Starting location'),
    'DESTINATION': fields.String(description='Destination location'),
    'ROUTE': fields.String(description='Road path used'),
    'ORDINARY_BUS_FARE_TSH': fields.String(description='Cost of using a Ordinary Bus'),
    'SEMI_LUXURY_BUS_FARE_TSH': fields.String(description='Cost of using a Luxury Bus'),
    'DISTANCE_KM': fields.String(description='Travelled distance')

})

# Define a resource for all bus routes
@api.route('/bus_routes')
class BusRoutes(Resource):
    @api.marshal_list_with(bus_route_model)
    def get(self):
        """Retrieve all bus routes"""
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bus_routes")
        routes = cursor.fetchall()
        cursor.close()
        connection.close()
        return routes

# Define a resource for searching bus routes
@api.route('/bus_routes/search')
class BusRouteSearch(Resource):
    @api.doc(params={'from': 'Starting location', 'destination': 'Destination location'})
    @api.marshal_with(bus_route_model, as_list=True)
    def get(self):
        """Search for bus routes by starting location and destination"""
        from_location = request.args.get('from')
        destination = request.args.get('destination')
        if not from_location or not destination:
            abort(400, "Missing 'from' or 'destination' query parameters")

        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT * FROM bus_routes WHERE `FROM` = %s AND `DESTINATION` = %s
        """
        cursor.execute(query, (from_location, destination))
        routes = cursor.fetchall()
        cursor.close()
        connection.close()

        if not routes:
            return [], 404  # No routes found

        return routes