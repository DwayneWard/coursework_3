from flask import request, abort
from flask_restx import Namespace, Resource

from project.exceptions import PasswordError, ItemNotFound
from project.implemented import user_service, favorite_movie_service, movie_service
from project.schemas.user import UserSchema
from project.tools.decode_token import get_email_from_token
from project.tools.decorators import auth_required

favorites_ns = Namespace('favorites')


@favorites_ns.route('/movies/<int:movie_id>')
class FavoriteMovieView(Resource):
    """
    Class-Based View для отображения профиля авторизованного пользователя.
    """

    # @auth_required
    # @favorites_ns.response(201, "Created")
    # @favorites_ns.response(404, "Movie not found")
    def post(self, movie_id: int):
        """

        """
        movie = movie_service.get_one(movie_id)
        # if movie is None:
        #     raise ItemNotFound
        # email = get_email_from_token()
        # user = user_service.get_by_email(email)
        # user_id = user.id
        #
        # favorite_movie_service.create(movie_id, user_id)
        return 'Created', 201



#
#
#
#     @auth_required
#     @favorites_ns.response(204, "OK")
#     def patch(self):
#         """
#         Метод производит частичное обновление данных в профиле авторизованного пользователя (имя, фамилия, любимый жанр)
#         путем отправления PATCH-запроса на /user.
#         """
#         email = get_email_from_token()
#         data = request.json
#
#         user_service.partial_update(email, data)
#         return "Update success", 204
#
#
# @favorites_ns.route("/password")
# class PasswordUpdateView(Resource):
#     """
#     Class-Based View для обновления авторизованным пользователем пароля.
#     """
#
#     @auth_required
#     @favorites_ns.response(200, "OK")
#     @favorites_ns.response(401, "Password is incorrect")
#     def put(self):
#         """
#         Метод реализует изменение пароля авторизованного пользователя. Для обновления необходимо отправить
#         новый пароль и старый пароль путем отправления PUT-запроса на /user/password.
#         """
#         # password_1 - старый пароль
#         # password_2 - новый пароль
#         email = get_email_from_token()
#         req_json = request.json
#
#         old_password = req_json.get('password_1')
#         new_password = req_json.get('password_2')
#
#         try:
#             user_service.update_password(email, old_password, new_password)
#             return "OK", 200
#         except PasswordError:
#             abort(401, "Password is incorrect")
