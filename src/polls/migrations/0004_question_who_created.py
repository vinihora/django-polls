# Generated by Django 3.2.3 on 2021-06-05 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='who_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.customer'),
        ),
    ]
