from marshmallow import fields, Schema


class FavMovieSchema(Schema):
    movie_id = fields.Int(required=True)
    movie = fields.Str(required=True)
