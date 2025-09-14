from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=128)

    def __str__(self):
        return self.username
