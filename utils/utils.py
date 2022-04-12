import csv
import datetime
from apps.reports.models import CovidRegister


class Utils:

    def __init__(self) -> None:
        pass

    def read_csv(self):
        with open("files/data.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.save_data(row)

    def save_data(self, args):
        date = datetime.datetime.strptime(args['date'], '%Y-%m-%d').date()
        CovidRegister.objects.create(
            iso_code=args['iso_code'],
            continent=args['continent'],
            location=args['location'],
            date=date,
            total_cases=self.validate_value(args["total_cases"]),
            new_cases=self.validate_value(args["new_cases"]),
            new_cases_smoothed=self.validate_value(args["new_cases_smoothed"]),
            total_deaths=self.validate_value(args["total_deaths"]),
            new_deaths=self.validate_value(args["new_deaths"]),
            new_deaths_smoothed=self.validate_value(
                args["new_deaths_smoothed"]),
            total_cases_per_million=self.validate_value(
                args["total_cases_per_million"]),
            new_cases_per_million=self.validate_value(
                args["new_cases_per_million"]),
            new_cases_smoothed_per_million=self.validate_value(
                args["new_cases_smoothed_per_million"]),
            total_deaths_per_million=self.validate_value(
                args["total_deaths_per_million"]),
            new_deaths_per_million=self.validate_value(
                args["new_deaths_per_million"]),
            new_deaths_smoothed_per_million=self.validate_value(
                args["new_deaths_smoothed_per_million"]),
            reproduction_rate=self.validate_value(args["reproduction_rate"]),
            icu_patients=self.validate_value(args["icu_patients"]),
            icu_patients_per_million=self.validate_value(
                args["icu_patients_per_million"]),
            hosp_patients=self.validate_value(args["hosp_patients"]),
            hosp_patients_per_million=self.validate_value(
                args["hosp_patients_per_million"]),
            weekly_icu_admissions=self.validate_value(
                args["weekly_icu_admissions"]),
            weekly_icu_admissions_per_million=self.validate_value(
                args["weekly_icu_admissions_per_million"]),
            weekly_hosp_admissions=self.validate_value(
                args["weekly_hosp_admissions"]),
            weekly_hosp_admissions_per_million=self.validate_value(
                args["weekly_hosp_admissions_per_million"]),
            total_tests=self.validate_value(args["total_tests"]),
            new_tests=self.validate_value(args["new_tests"]),
            total_tests_per_thousand=self.validate_value(
                args["total_tests_per_thousand"]),
            new_tests_per_thousand=self.validate_value(
                args["new_tests_per_thousand"]),
            new_tests_smoothed_per_thousand=self.validate_value(
                args["new_tests_smoothed_per_thousand"]),
            positive_rate=self.validate_value(args["positive_rate"]),
            tests_per_case=self.validate_value(args["tests_per_case"]),
            tests_units=args["tests_units"] or "",
            total_vaccinations=self.validate_value(args["total_vaccinations"]),
            people_vaccinated=self.validate_value(args["people_vaccinated"]),
            people_fully_vaccinated=self.validate_value(
                args["people_fully_vaccinated"]),
            total_boosters=self.validate_value(args["total_boosters"]),
            new_vaccinations=self.validate_value(args["new_vaccinations"]),
            new_vaccinations_smoothed=self.validate_value(
                args["new_vaccinations_smoothed"]),
            total_vaccinations_per_hundred=self.validate_value(
                args["total_vaccinations_per_hundred"]),
            people_vaccinated_per_hundred=self.validate_value(
                args["people_vaccinated_per_hundred"]),
            people_fully_vaccinated_per_hundred=self.validate_value(
                args["people_fully_vaccinated_per_hundred"]),
            total_boosters_per_hundred=self.validate_value(
                args["total_boosters_per_hundred"]),
            new_people_vaccinated_smoothed=self.validate_value(
                args["new_people_vaccinated_smoothed"]),
            new_people_vaccinated_smoothed_per_hundred=self.validate_value(
                args["new_people_vaccinated_smoothed_per_hundred"]),
            stringency_index=self.validate_value(args["stringency_index"]),
            population=self.validate_value(args["population"]),
            population_density=self.validate_value(args["population_density"]),
            median_age=self.validate_value(args["median_age"]),
            aged_65_older=self.validate_value(args["aged_65_older"]),
            aged_70_older=self.validate_value(args["aged_70_older"]),
            gdp_per_capita=self.validate_value(args["gdp_per_capita"]),
            extreme_poverty=self.validate_value(args["extreme_poverty"]),
            cardiovasc_death_rate=self.validate_value(
                args["cardiovasc_death_rate"]),
            diabetes_prevalence=self.validate_value(
                args["diabetes_prevalence"]),
            female_smokers=self.validate_value(args["female_smokers"]),
            male_smokers=self.validate_value(args["male_smokers"]),
            handwashing_facilities=self.validate_value(
                args["handwashing_facilities"]),
            hospital_beds_per_thousand=self.validate_value(
                args["hospital_beds_per_thousand"]),
            life_expectancy=self.validate_value(args["life_expectancy"]),
            human_development_index=self.validate_value(
                args["human_development_index"]),
            excess_mortality_cumulative_absolute=self.validate_value(
                args["excess_mortality_cumulative_absolute"]),
            excess_mortality_cumulative=self.validate_value(
                args["excess_mortality_cumulative"]),
            excess_mortality=self.validate_value(args["excess_mortality"]),
            excess_mortality_cumulative_per_million=self.validate_value(
                args["excess_mortality_cumulative_per_million"]),
        )

    def validate_value(self, value):
        try:
            float(value)
            return value
        except:
            pass
        return 0
