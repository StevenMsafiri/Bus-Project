from flask import Flask
from services import bus_routes_bp

app = Flask(__name__)

# Register the bus routes Blueprint
app.register_blueprint(bus_routes_bp)

if __name__ == "__main__":
    app.run(debug=True)
