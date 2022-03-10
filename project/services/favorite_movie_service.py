from project.dao.favorite_movie import FavoriteMovieDAO


class FavoriteMovieService:
    def __init__(self, dao: FavoriteMovieDAO):
        """
        Метод инициализирует DAO

        :param dao: DAO объект
        """
        self.dao = dao

    def create(self, user_id: int, movie_id: int) -> list:
        """
        Метод реализует запись новых данных в базу данных.

        :param movie_id: id фильма.
        :param user_id: id авторизованного пользователя
        """
        return self.dao.create(movie_id=movie_id, user_id=user_id)
