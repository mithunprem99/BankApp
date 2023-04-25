# Generated by Django 4.1.6 on 2023-04-25 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBank', '0003_branchmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('Age', models.CharField(max_length=10)),
                ('Gender', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=500)),
                ('Account', models.CharField(max_length=255)),
                ('Materials', models.CharField(max_length=255)),
                ('Branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBank.branchmodel')),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBank.district')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBank.registermodel')),
            ],
        ),
    ]
