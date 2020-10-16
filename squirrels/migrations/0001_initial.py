# Generated by Django 3.1.2 on 2020-10-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(help_text='Longitude coordinate for squirrel sighting point', max_length=20)),
                ('Y', models.FloatField(help_text='Latitude coordinate for squirrel sighting point', max_length=20)),
                ('sq_id', models.CharField(help_text='Identification tag for each squirrel sightings', max_length=100)),
                ('Hect', models.CharField(help_text='Hectare of Sighting', max_length=20)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift of Sighting', max_length=2)),
                ('Date', models.DateField(help_text='Date of Sighting')),
                ('Hect_sq_num', models.CharField(help_text='Number within the chronological sequence of squirrel sightings', max_length=20)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of squirrel', max_length=10)),
                ('Primary_color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], help_text='Primary color of squirrel', max_length=10)),
                ('Highlight_color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], help_text='Highlight fur color', max_length=10)),
                ('Combo', models.CharField(blank=True, help_text='Combination of primary and highlight color', max_length=30)),
                ('Color_notes', models.TextField(blank=True, help_text='Color notes of squirrel')),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location of squirrel', max_length=20)),
                ('Above_measure', models.CharField(blank=True, help_text='Above ground sighter measurement of squirrel', max_length=10)),
                ('Specific_loc', models.TextField(blank=True, help_text='Specific location of squirrel')),
                ('Running', models.BooleanField(help_text='Squirrel was seen running')),
                ('Chasing', models.BooleanField(help_text='Squirrel was seen chasing another squirrel')),
                ('Climbing', models.BooleanField(help_text='Squirrel was seen climbing a tree or other environmental landmark')),
                ('Eating', models.BooleanField(help_text='Squirrel was seen eating')),
                ('Foraging', models.BooleanField(help_text='Squirrel was seen foraging for food')),
                ('Other_act', models.TextField(blank=True, help_text='Other activities squirrel was doing')),
                ('Kuks', models.BooleanField(help_text='Squirrel was heard kukking')),
                ('Quass', models.BooleanField(help_text='Squirrel was heard quaaing')),
                ('Moans', models.BooleanField(help_text='Squirrel was heard moaning')),
                ('Tail_flag', models.BooleanField(help_text='Squirrel was seen flagging its tail')),
                ('Tail_twitch', models.BooleanField(help_text='Squirrel was seen twitching its tail')),
                ('Approaches', models.BooleanField(help_text='Squirrel was seen approaching human, seeking food')),
                ('Indifferent', models.BooleanField(help_text='Squirrel was indifferent to human presence')),
                ('Runs_from', models.BooleanField(help_text='Squirrel was seen running from humans, seeing them as a threat')),
                ('Other_interactions', models.TextField(blank=True, help_text='Sighter notes on other types of interactions between squirrels and humans')),
                ('Lat_long', models.CharField(help_text='Latitude and longitude', max_length=100)),
            ],
        ),
    ]