from django.db import models
from django.conf import settings

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(
        max_length=10, unique=True
    )  # by default, this will be used as index because it is Unique
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "lecturer"},
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
