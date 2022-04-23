# Generated by Django 4.0.3 on 2022-04-23 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=20)),
                ('continent', models.CharField(max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CovidRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('new_deaths_per_million', models.FloatField(default=0)),
                ('total_cases', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_cases', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_cases_smoothed', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_deaths', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_deaths', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_deaths_smoothed', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_cases_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_cases_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_cases_smoothed_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_deaths_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_deaths_smoothed_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('reproduction_rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('icu_patients', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('icu_patients_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('hosp_patients', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('hosp_patients_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('weekly_icu_admissions', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('weekly_icu_admissions_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('weekly_hosp_admissions', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('weekly_hosp_admissions_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_tests', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_tests', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_tests_per_thousand', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_tests_per_thousand', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_tests_smoothed', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_tests_smoothed_per_thousand', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('positive_rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('tests_per_case', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('tests_units', models.CharField(max_length=255)),
                ('total_vaccinations', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('people_vaccinated', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('people_fully_vaccinated', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_boosters', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_vaccinations', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_vaccinations_smoothed', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_vaccinations_per_hundred', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('people_vaccinated_per_hundred', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('people_fully_vaccinated_per_hundred', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_boosters_per_hundred', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_people_vaccinated_smoothed', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('new_people_vaccinated_smoothed_per_hundred', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('stringency_index', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('population', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('population_density', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('median_age', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('aged_65_older', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('aged_70_older', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('gdp_per_capita', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('extreme_poverty', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('cardiovasc_death_rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('diabetes_prevalence', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('female_smokers', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('male_smokers', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('handwashing_facilities', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('hospital_beds_per_thousand', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('life_expectancy', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('human_development_index', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('excess_mortality_cumulative_absolute', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('excess_mortality_cumulative', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('excess_mortality', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('excess_mortality_cumulative_per_million', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.location')),
            ],
            options={
                'db_table': 'covid_register',
            },
        ),
    ]
