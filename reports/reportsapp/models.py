from django.utils import timezone
from django.db import models


class Report(models.Model):
    creation_date = models.DateField('Дата создания',
                                         default=timezone.now)
    content = models.TextField('Содержимое')
