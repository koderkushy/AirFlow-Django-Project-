# Generated by Django 3.2.9 on 2021-11-12 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airflow', '0009_auto_20211112_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_n', models.IntegerField()),
                ('total_fare', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Confirmed'), (1, 'Pending')], default=0)),
                ('fl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airflow.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]