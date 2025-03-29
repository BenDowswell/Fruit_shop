from flask import Flask, jsonify, session
from auth import auth  # Import the auth blueprint

app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")  # Register the auth blueprint
# ...existing code...

# ...existing code...
