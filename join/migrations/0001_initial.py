# Generated by Django 2.2.6 on 2019-10-15 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.College')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(max_length=15, unique=True)),
                ('sex', models.CharField(blank=True, choices=[('O', '其他'), ('B', '男'), ('G', '女')], max_length=1, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Y', '未入社'), ('M', '已入社'), ('NP', '未付款')], default='Y', max_length=2)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='join.Lesson')),
                ('positions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='join.Position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='memberuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.Degree'),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('sex', models.CharField(blank=True, choices=[('O', '其他'), ('B', '男'), ('G', '女')], max_length=1, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Y', '未入社'), ('M', '已入社'), ('NP', '未付款')], default='Y', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attendeeuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
