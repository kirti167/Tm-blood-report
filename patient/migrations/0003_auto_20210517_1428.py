# Generated by Django 3.2.3 on 2021-05-17 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20210517_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='document',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.document'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
