# Generated by Django 5.1.6 on 2025-03-15 16:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_ID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_ID', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_ID', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField(max_length=1020)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('game_picture', models.ImageField(blank=True, null=True, upload_to='game_pictures/')),
                ('genre_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BossRanked.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_ID', models.AutoField(primary_key=True, serialize=False)),
                ('review_text', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('game_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BossRanked.game')),
                ('user_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BossRanked.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAction',
            fields=[
                ('action_ID', models.AutoField(primary_key=True, serialize=False)),
                ('action_type', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BossRanked.admin')),
                ('review_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BossRanked.review')),
            ],
        ),
    ]
