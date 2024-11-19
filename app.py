from flask import Flask
from services.buses_routes import bus_routes_bp
app = Flask(__name__)
# Create a Flask-RESTX Api object and attach it to the blueprint

# Register the blueprint with the main app
app.register_blueprint(bus_routes_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)