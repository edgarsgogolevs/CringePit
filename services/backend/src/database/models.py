from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    points = fields.IntField(default=0)
    yellow_cards = fields.IntField(default=0, null=True)
    red_cards = fields.IntField(default=0, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Reviews(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    type = fields.CharField(max_length=30, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    
    # foreign keys
    author = fields.ForeignKeyField("models.Users", related_name="reviews")

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"
    
class Movies(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    overview = fields.TextField(null=True)
    runtime = fields.IntField(null=True)
    release_date = fields.DatetimeField(null=True)
    genres = fields.JSONField(null=True)

    poster_path = fields.CharField(null=True, max_length=300)
    backdrop_path = fields.CharField(null=True, max_length=300)

class MovieReviews(models.Model):
    id = fields.IntField(pk=True)
    score = fields.IntField()
    comment = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    # foreign keys
    author = fields.ForeignKeyField("models.Users", related_name="movieReviews", on_delete='CASCADE')
    movie = fields.ForeignKeyField("models.Movies", related_name="movieReviews", on_delete='CASCADE')
