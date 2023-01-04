from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank = True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.IntegerField(blank=True, default=0, validators=[MaxValueValidator(100),MinValueValidator(0)])
    datedue = models.DateTimeField(null=True, blank = True)

    def __str__(self):
        return self.title + " : " + self.user.username
