from models.userModel import db, User
from utils.jwt_util import encode_auth_token
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()

    required_fields = [
        'ad', 'soyad', 'ata_adi', 'fin_kod', 'password', 'faculty_id',
        'faculty_name', 'kafedra_id', 'kafedra_name', 'vezife_id', 
        'vezife_name', 'icrayamesulsexs_id'
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
        
    ad = data.get('ad')
    soyad = data.get('soyad')
    ata_adi = data.get('ata_adi')
    fin_kod = data.get('fin_kod')
    password = data.get('password')
    faculty_id = data.get('faculty_id')
    faculty_name = data.get('faculty_name')
    kafedra_id = data.get('kafedra_id')
    kafedra_name = data.get('kafedra_name')
    vezife_id = data.get('vezife_id')
    vezife_name = data.get('vezife_name')
    icrayamesulsexs_id = data.get('icrayamesulsexs_id')

    if User.query.filter_by(fin_kod=fin_kod).first():
        return jsonify({'message': 'User already exists.'}), 400

    user = User(
        ad=ad,
        soyad=soyad,
        ata_adi=ata_adi,
        fin_kod=fin_kod,
        password_hash='',
        faculty_id=faculty_id,
        faculty_name=faculty_name,
        kafedra_id=kafedra_id,
        kafedra_name=kafedra_name,
        vezife_id=vezife_id,
        vezife_name=vezife_name,
        icrayamesulsexs_id=icrayamesulsexs_id
    )
    
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User successfully registered.'}), 201

@auth_bp.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    fin_kod = data.get('fin_kod')
    password = data.get('password')

    user = User.query.filter_by(fin_kod=fin_kod).first()

    if not user:
        return jsonify({'message': 'User not found'}), 401
    if not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = encode_auth_token(user.id, user.fin_kod, user.vezife_name)

    return jsonify({
        'status': 200,
        'message': 'Success',
        # 'data': user.to_dict(), // eger data login de qaytarilmali olsa bu istifade olunacaq 
        'token': token
    }), 200