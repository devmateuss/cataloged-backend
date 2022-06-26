from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#
#     class Meta:
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"
#
#     def __str__(self):
#         return "{} - {} - {}".format(self.pk, self.username, self.email)


class Client(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField()

    # users = models.ManyToManyRel(User, )

    def __str__(self):
        return self.name
