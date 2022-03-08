import jwt
from flask import request, current_app


def get_email_from_token():
    """
    Функция производит получение email для дальнейшеного поиска в базе данных авторизованного пользователя из токена,
    который передает пользователь
    """

    data = request.headers["Authorization"]
    token = data.split("Bearer ")[-1]
    user_data = jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=[current_app.config["JWT_ALGORITHM"]])

    return user_data['email']
