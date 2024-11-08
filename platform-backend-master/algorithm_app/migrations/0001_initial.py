# Generated by Django 4.1.7 on 2024-06-18 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('algorithm_name', models.CharField(max_length=100)),
                ('indicator_id', models.CharField(max_length=100, null=True)),
                ('cpu_count', models.CharField(max_length=100, null=True)),
                ('mem_limit', models.CharField(max_length=100, null=True)),
                ('container_created', models.BooleanField()),
                ('container_status', models.BooleanField(null=True)),
                ('container_id', models.CharField(max_length=100, null=True)),
                ('container_port', models.CharField(max_length=100, null=True)),
                ('container_ip', models.CharField(max_length=100, null=True)),
                ('dataset_path', models.CharField(max_length=300, null=True)),
                ('is_split', models.BooleanField()),
                ('run_command', models.CharField(max_length=100, null=True)),
                ('train_command', models.CharField(max_length=100, null=True)),
                ('test_command', models.CharField(max_length=100, null=True)),
                ('dataset_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlgorithmType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('template_name', models.CharField(max_length=100)),
                ('indicator_id', models.CharField(max_length=100, null=True)),
                ('create_person', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_evaluate', models.CharField(max_length=100, null=True)),
                ('record_id', models.CharField(max_length=100, null=True)),
                ('algorithm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algorithm_app.algorithm')),
            ],
        ),
        migrations.CreateModel(
            name='TaskExecute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100, null=True)),
                ('dataset_range', models.CharField(max_length=100, null=True)),
                ('execute_type', models.IntegerField()),
                ('execute_status', models.CharField(max_length=100, null=True)),
                ('pid', models.CharField(max_length=100, null=True)),
                ('container_pid', models.CharField(max_length=100, null=True)),
                ('execute_person', models.CharField(max_length=100, null=True)),
                ('execute_result', models.TextField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('create_person', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('train_or_test', models.CharField(max_length=100, null=True)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algorithm_app.tasktemplate')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationIndicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('indicator_name', models.CharField(max_length=100, null=True)),
                ('format_json', models.TextField(null=True)),
                ('algorithm_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algorithm_app.algorithmtype')),
            ],
        ),
        migrations.AddField(
            model_name='algorithm',
            name='algorithm_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algorithm_app.algorithmtype'),
        ),
    ]
