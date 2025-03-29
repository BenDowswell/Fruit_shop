from flask import Blueprint, jsonify, session

auth = Blueprint("auth", __name__)
# ...existing code...


@auth.route("/me", methods=["GET"])
def me():
    # Assuming user information is stored in the session
    user = session.get("user", {})
    username = user.get("username", "Guest")
    role = user.get("role", "Unknown")
    return jsonify({"username": username, "role": role})


# ...existing code...
