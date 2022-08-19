# Generated by Django 4.0.6 on 2022-08-04 19:36

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
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, verbose_name='Token')),
                ('quantity', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Quantity')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Purchase_price')),
                ('purchased_at', models.DateTimeField(verbose_name='Purchased_at')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Sale_price')),
                ('sold_at', models.DateTimeField(blank=True, null=True, verbose_name='Sold_at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'token',
                'verbose_name_plural': 'tokens',
                'ordering': ['token'],
            },
        ),
    ]