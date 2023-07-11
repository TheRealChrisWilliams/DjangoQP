from django.db import models


class QPModel(models.Model):
    name = models.CharField(max_length=200, db_column='LINK')

    class Meta:
        app_label = 'QPApp'
        db_table = 'PDF_LINKS'
        verbose_name_plural = "qpmodels"

    def __str__(self):
        return self.name


