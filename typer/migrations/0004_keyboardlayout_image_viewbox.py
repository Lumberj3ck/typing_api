# Generated by Django 4.2.3 on 2023-10-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typer', '0003_alter_level_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboardlayout',
            name='image_viewbox',
            field=models.CharField(default='0 0 82 66', max_length=200),
            preserve_default=False,
        ),
    ]
