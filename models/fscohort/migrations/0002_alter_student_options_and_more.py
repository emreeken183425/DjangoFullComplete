# Generated by Django 4.1.1 on 2023-01-03 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fscohort", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["number"], "verbose_name_plural": "Öğrenciler"},
        ),
        migrations.RenameField(
            model_name="student",
            old_name="fisrt_name",
            new_name="first_name",
        ),
    ]
