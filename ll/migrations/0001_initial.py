# Generated by Django 3.2 on 2023-03-09 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=10)),
                ('project_name', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=30)),
                ('project_location', models.CharField(max_length=100)),
                ('market_sector', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projectnumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projectname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Projectlocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Marketsector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('projectlocation', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('division', models.CharField(max_length=20)),
                ('marketsector', models.CharField(max_length=255)),
                ('discipline', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=100)),
                ('memo', models.CharField(max_length=255)),
                ('linkfile', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('projectnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ll.projectnumber')),
            ],
        ),
    ]
