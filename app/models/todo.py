from tortoise import fields, models


class Todo(models.Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    done = fields.BooleanField(default=False)
    author = fields.ForeignKeyField("models.User", related_name="todos")

    def __str__(self):
        return self.title
