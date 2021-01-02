# Generated by Django 2.0 on 2021-01-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='style',
            field=models.CharField(choices=[('N', 'Normal'), ('C', 'Color blind')], default='N', help_text='Designates which style will be shown to the user across pages; helpful for people with difficulties distinguishing colors.', max_length=1, verbose_name='style'),
        ),
    ]
