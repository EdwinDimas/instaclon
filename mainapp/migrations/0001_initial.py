# Generated by Django 4.0.2 on 2022-02-14 07:56

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
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('mensaje', models.CharField(max_length=250)),
                ('foto', models.FileField(upload_to='profile_pics/')),
                ('esPrivado', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seguidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seguidor_perfil', to='mainapp.perfil')),
                ('seguidor_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seguidor', to='mainapp.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Seguido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seguido_perfil', to='mainapp.perfil')),
                ('seguido_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='seguido', to='mainapp.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='post_pics/')),
                ('mensaje', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('perfil_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.perfil')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('perfil_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.perfil')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainapp.post')),
            ],
        ),
    ]
