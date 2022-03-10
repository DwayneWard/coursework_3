from project.dao.models.user_movie import UserMovie


class FavoriteMovieDAO:
    def __init__(self, session):
        """
        Метод инициализирует поле класса session, как сессию работы с базой данных.

        :param session: Сессия базы данных
        """
        self.session = session

    def create(self, movie_id: int, user_id: int):
        """
        Метод реализует запись новых данных в базу данных.

        :param movie_id: id фильма.
        :param user_id: id авторизованного пользователя
        """
        new_fav = UserMovie(movie_id=movie_id, user_id=user_id)
        self.session.add(new_fav)
        self.session.commit()
