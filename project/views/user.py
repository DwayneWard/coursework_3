from flask import request, abort
from flask_restx import Namespace, Resource

from project.exceptions import PasswordError
from project.implemented import user_service
from project.schemas.user import UserSchema
from project.tools.decode_token import get_email_from_token
from project.tools.decorators import auth_required

users_ns = Namespace('user')


@users_ns.route('/')
class UserView(Resource):
    """
    Class-Based View для отображения конкретного пользователя из БД.
    """

    @auth_required
    @users_ns.response(200, "OK")
    def get(self):
        """
        Метод реализует отправку GET-запроса на /users/id.

        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        email = get_email_from_token()
        user = user_service.get_by_email(email)
        return UserSchema().dump(user), 200

    @auth_required
    @users_ns.response(204, "OK")
    @users_ns.response(404, "Something went wrong")
    def patch(self):
        email = get_email_from_token()
        data = request.json
        try:
            user_service.partial_update(email, data) # Не обновляется favorite_genre
        except Exception:
            abort(404, "Something went wrong")
        return "Update success", 204


@users_ns.route("/password")
class PasswordUpdateView(Resource):
    """
    Class-Based View для обновления конкретным пользователем пароля.
    """

    @auth_required
    def put(self):
        # password_1 - старый пароль
        # password_2 - новый пароль
        email = get_email_from_token()
        req_json = request.json

        old_password = req_json.get('password_1')
        new_password = req_json.get('password_2')

        try:
            user_service.update_password(email, old_password, new_password)
            return "OK", 200
        except PasswordError:
            abort(401, "Password is incorrect")
