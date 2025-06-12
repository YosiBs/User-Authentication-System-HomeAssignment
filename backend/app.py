from flask import Flask, jsonify
from flask_cors import CORS
from .routes import auth_routes

from .utils.limiter import limiter


app = Flask(__name__)
CORS(app)
limiter.init_app(app)

# Register the authentication routes
app.register_blueprint(auth_routes)


# Rate Limiting for login attempts --Start
@limiter.request_filter
def exempt_static():
    return False

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Too many login attempts. Please wait a minute."}), 429
# Rate Limiting for login attempts --End

if __name__ == "__main__":
    app.run(debug=True)