from flask import jsonify, request, abort
from services import bus_routes_bp
from destination_Fares.connection import create_connection # Import the function
import mysql.connector
from mysql.connector import Error

# Route to get all bus routes
@bus_routes_bp.route('/api/bus_routes', methods=['GET'])
def get_bus_routes():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bus_routes")
    routes = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(routes)

# Route to get bus routes by FROM and DESTINATION
@bus_routes_bp.route('/api/bus_routes/search', methods=['GET'])
def search_bus_routes():
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
        return jsonify([]), 404  # No routes found

    return jsonify(routes)
