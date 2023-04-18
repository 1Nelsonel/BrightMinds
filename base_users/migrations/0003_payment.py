# Generated by Django 4.0.5 on 2023-04-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_users', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('reference', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('status_description', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
