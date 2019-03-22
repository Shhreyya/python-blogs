# Generated by Django 2.1.7 on 2019-03-22 04:08

from django.db import migrations, models
import gsoc.models


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0008_auto_20190322_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_used', models.BooleanField(default=False, editable=False)),
                ('reglink_id', models.CharField(default=gsoc.models.gen_uuid_str, editable=False, max_length=36)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
