# Generated by Django 3.1.6 on 2021-03-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210327_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_type', models.TextField(choices=[('deposit', 'deposit'), ('withdraw', 'withdraw')])),
                ('amount', models.FloatField()),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
    ]
