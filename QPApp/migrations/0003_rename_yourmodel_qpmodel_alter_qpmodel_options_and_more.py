# Generated by Django 4.2.3 on 2023-07-10 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QPApp', '0002_alter_yourmodel_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YourModel',
            new_name='QPModel',
        ),
        migrations.AlterModelOptions(
            name='qpmodel',
            options={'verbose_name_plural': 'qpmodels'},
        ),
        migrations.AlterModelTable(
            name='qpmodel',
            table='PDF_LINKS',
        ),
    ]