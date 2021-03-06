# Generated by Django 3.1.4 on 2020-12-10 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.question')),
            ],
        ),
        migrations.RenameField(
            model_name='quiztaker',
            old_name='score',
            new_name='carbon_footprint',
        ),
        migrations.RenameModel(
            old_name='Answer',
            new_name='Response',
        ),
        migrations.DeleteModel(
            name='UsersAnswer',
        ),
        migrations.AddField(
            model_name='usersresponse',
            name='quiz_taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.quiztaker'),
        ),
        migrations.AddField(
            model_name='usersresponse',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.response'),
        ),
    ]
