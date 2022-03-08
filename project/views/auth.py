from flask import request, abort
from flask_restx import Namespace, Resource

from project.exceptions import ItemNotFound
from project.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthsRegisterView(Resource):
    """
    Класс CBV для представления /auth/register.
    POST-метод: производит генерацию access и refresh tokens на основе запроса пользователя.
    """

    @auth_ns.response(201, "User created")
    def post(self):
        req_json = request.json
        try:
            auth_service.register_new_user(req_json)
        except Exception:  # Переписать на нормальную ошибку!
            abort(400, "User already registered")

        return "User created", 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    @auth_ns.response(201, 'Tokens created')
    @auth_ns.response(401, "No data")
    def post(self):
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')

        if None in [email, password]:
            abort(401, "No data. Try again")

        tokens = auth_service.generate_token(email, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")

        if refresh_token is None:
            abort(401, "No refresh token data")

        try:
            tokens = auth_service.approve_refresh_token(refresh_token)
            return tokens, 201
        except ItemNotFound:
            abort(404, "User not found")
