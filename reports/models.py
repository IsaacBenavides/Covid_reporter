from django.db import models


class CovidRegister(models.Model):

    iso_code = models.CharField(max_length=20, blank=False, null=False)
    continent = models.CharField(max_length=255, blank=False, null=False)
    location = models.CharField(
        max_length=255, blank=False, null=False, default="")
    new_deaths_per_million = models.FloatField(
        blank=False, null=False, default=0)
    new_vaccinations_smoothed_per_hundred = models.FloatField(
        blank=False, null=False, default=0)
    date = models.DateField(blank=False, null=False)
    total_cases = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_cases = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_cases_smoothed = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_deaths = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_deaths = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_deaths_smoothed = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_cases_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_cases_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_cases_smoothed_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_deaths_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_deaths_smoothed_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    reproduction_rate = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    icu_patients = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    icu_patients_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    hosp_patients = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    hosp_patients_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    weekly_icu_admissions = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    weekly_icu_admissions_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    weekly_hosp_admissions = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    weekly_hosp_admissions_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_tests = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_tests = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_tests_per_thousand = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_tests_per_thousand = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_tests_smoothed = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_tests_smoothed_per_thousand = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    positive_rate = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    tests_per_case = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    tests_units = models.CharField(max_length=255, blank=False, null=False)
    total_vaccinations = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    people_vaccinated = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    people_fully_vaccinated = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_boosters = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_vaccinations = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_vaccinations_smoothed = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_vaccinations_per_hundred = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    people_vaccinated_per_hundred = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    people_fully_vaccinated_per_hundred = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    total_boosters_per_hundred = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_people_vaccinated_smoothed = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    new_people_vaccinated_smoothed_per_hundred = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    stringency_index = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    population = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    population_density = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    median_age = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    aged_65_older = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    aged_70_older = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    gdp_per_capita = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    extreme_poverty = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    cardiovasc_death_rate = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    diabetes_prevalence = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    female_smokers = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    male_smokers = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    handwashing_facilities = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    hospital_beds_per_thousand = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    life_expectancy = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    human_development_index = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    excess_mortality_cumulative_absolute = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    excess_mortality_cumulative = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    excess_mortality = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)
    excess_mortality_cumulative_per_million = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.location

    class Meta:
        db_table = 'covid_register'
