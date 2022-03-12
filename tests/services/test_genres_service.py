from unittest.mock import Mock, patch, MagicMock

import pytest

from project.dao.genre import GenreDAO
from project.dao.models.genre import Genre
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.genres_service import GenreService
from project.setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)
    g1 = Genre(name='Боевик')
    g2 = Genre(name='Триллер')
    g3 = Genre(name='Ужастик')

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.get_by_page = MagicMock()  # TODO Как мокировать не понимаю


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None


# class TestGenresService:
#     @pytest.fixture(autouse=True)
#     def service(self, db):
#         self.service = GenreService(db.session)
#
#     @pytest.fixture
#     def genre(self):
#         return Genre(id=1, name="genre_1")
#
#     @pytest.fixture
#     def genre_dao_mock(self, genre):
#         with patch("project.services.genres_service.GenreDAO") as mock:
#             mock.return_value = Mock(
#                 get_one=Mock(return_value=GenreSchema().dump(genre)),
#                 get_all=Mock(return_value=GenreSchema(many=True).dump([genre])),
#             )
#             yield mock
#
#     def test_get_all_genres(self, genre_dao_mock, genre):
#         assert self.service.get_all() == GenreSchema(many=True).dump([genre])
#         genre_dao_mock().get_all.assert_called_once()
#
#     def test_get_item_by_id(self, genre_dao_mock, genre):
#         assert self.service.get_one(genre.id) == GenreSchema().dump(genre)
#         genre_dao_mock().get_by_id.assert_called_once_with(genre.id)
#
#     def test_get_item_by_id_not_found(self, genre_dao_mock):
#         genre_dao_mock().get_by_id.return_value = None
#
#         with pytest.raises(ItemNotFound):
#             self.service.get_one(1)
