# Generated by Django 3.0.4 on 2020-03-17 10:47

from django.conf import settings
from django.db import migrations, models
import printutil.models
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('printutil', '0003_auto_20200317_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printrequest',
            name='source',
            field=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=printutil.models.get_file_path, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='printrequest',
            name='username',
            field=models.ForeignKey(on_delete=models.SET(printutil.models.get_sentinel_user), related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
