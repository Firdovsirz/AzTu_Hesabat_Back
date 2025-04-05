from models.userModel import db, User
from utils.jwt_util import decode_auth_token
from flask import Blueprint, request, jsonify
from utils.jwt_required import token_required

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/api/profile', methods=['GET'])
@token_required
def profile(user):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'message': 'Token missing'}), 401

    if not auth_header.startswith('Bearer '):
        return jsonify({'message': 'Token format wrong'}), 401

    auth_token = auth_header.split(" ")[1]

    token_data = decode_auth_token(auth_token)

    if not token_data:
        return jsonify({'message': 'Token expired'}), 401

    user_id = token_data.get('user_id')

    if not user_id:
        return jsonify({'message': 'Invalid token'}), 401

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({
        'status': 200,
        'message': 'Success',
        'data': user.to_dict()
    }), 200