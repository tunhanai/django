# Generated by Django 4.2.1 on 2023-06-17 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_nguoidat_datphong_nd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttkhach',
            old_name='nguoidat',
            new_name='nguoidung',
        ),
        migrations.RemoveField(
            model_name='datphong',
            name='nd',
        ),
        migrations.AddField(
            model_name='datphong',
            name='nguoidung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.nguoidung'),
        ),
    ]