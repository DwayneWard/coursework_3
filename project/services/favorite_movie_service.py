from project.dao.favorite_movie import FavoriteMovieDAO
from project.exceptions import ItemNotFound


class FavoriteMovieService:
    def __init__(self, dao: FavoriteMovieDAO):
        """
        Метод инициализирует DAO

        :param dao: DAO объект
        """
        self.dao = dao

    def get_one(self, id_: int) -> list:
        """
        Метод получает данные из таблицы по id
        """
        return self.dao.get_one(id_)

    def create(self, user_id: int, movie_id: int) -> None:
        """
        Метод реализует запись новых данных в базу данных.

        :param movie_id: id фильма.
        :param user_id: id авторизованного пользователя
        """
        return self.dao.create(movie_id=movie_id, user_id=user_id)

    def is_movie_id_in(self, movie_id: int) -> bool:
        """
        Метод реализует поиск фильма в таблице с избранными

        :param movie_id: id фильма
        :return: True или эксепшн
        """
        if not self.dao.is_movie_id_in(movie_id):
            raise ItemNotFound
        return True

    def delete(self, id_: int) -> None:
        """
        Метод реализует удаление записи в базе данных.
        :param id_: id записи в базе данных.
        """
        data = self.get_one(id_)
        self.dao.delete(data)

    def get_id(self, movie_id: int, user_id: int):
        data_id = self.dao.get_id(movie_id, user_id)
        if not data_id:
            raise ItemNotFound
        return data_id
