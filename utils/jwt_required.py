from functools import wraps
from flask import request, jsonify
from utils.jwt_util import decode_auth_token

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!', 'status': 403}), 403

        user_id = decode_auth_token(token)

        if user_id is None:
            return jsonify({'message': 'Invalid or expired token!', 'status': 401}), 401

        return f(user_id, *args, **kwargs)

    return decorator