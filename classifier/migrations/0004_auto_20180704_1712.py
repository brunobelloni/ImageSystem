# Generated by Django 2.0.6 on 2018-07-04 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_auto_20180626_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Insect',
                'verbose_name_plural': 'Insects',
            },
        ),
        migrations.CreateModel(
            name='Trap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Trap',
                'verbose_name_plural': 'Traps',
            },
        ),
        migrations.CreateModel(
            name='Trap_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='publication date')),
                ('image', models.CharField(max_length=100)),
                ('trap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Trap')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Trap_Image_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('cordX', models.IntegerField()),
                ('cordY', models.IntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Trap_Image')),
                ('insect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Insect')),
            ],
            options={
                'verbose_name': 'Insect_Data',
                'verbose_name_plural': 'Insect_Data',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Variable',
                'verbose_name_plural': 'Variables',
            },
        ),
        migrations.RemoveField(
            model_name='dado',
            name='inseto',
        ),
        migrations.RemoveField(
            model_name='inseto',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='inseto',
            name='imagem',
        ),
        migrations.DeleteModel(
            name='Dado',
        ),
        migrations.DeleteModel(
            name='Especie',
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.DeleteModel(
            name='Inseto',
        ),
        migrations.AddField(
            model_name='trap_image_data',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Variable'),
        ),
    ]
