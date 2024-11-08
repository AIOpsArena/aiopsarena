# Generated by Django 4.1.7 on 2024-05-15 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKeyToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='key')),
                ('is_active', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('lastGetTime', models.DateTimeField(auto_now=True, null=True, verbose_name='最近查询时间')),
                ('countTimes', models.IntegerField(blank=True, default=0, verbose_name='key使用次数')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.user')),
            ],
        ),
    ]
