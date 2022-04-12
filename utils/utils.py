import csv
import datetime
from reports.models import CovidRegister


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
        total_cases = 0
        new_cases = 0
        new_cases_smoothed = 0
        total_deaths = 0
        new_deaths = 0
        new_deaths_smoothed = 0
        total_cases_per_million = 0
        new_cases_per_million = 0
        new_cases_smoothed_per_million = 0
        total_deaths_per_million = 0
        new_deaths_smoothed_per_million = 0
        reproduction_rate = 0
        icu_patients = 0
        icu_patients_per_million = 0
        total_tests = 0
        total_tests_per_thousand = 0
        new_tests_per_thousand = 0
        new_tests_smoothed_per_thousand = 0
        positive_rate = 0
        tests_per_case = 0
        tests_units = ""
        total_vaccinations = 0
        people_vaccinated = 0
        people_fully_vaccinated = 0
        total_boosters = 0
        new_vaccinations = 0
        new_vaccinations_smoothed = 0
        total_vaccinations_per_hundred = 0
        people_vaccinated_per_hundred = 0
        people_fully_vaccinated_per_hundred = 0
        total_boosters_per_hundred = 0
        new_vaccinations_smoothed_per_hundred = 0
        new_people_vaccinated_smoothed = 0
        new_people_vaccinated_smoothed_per_hundred = 0
        stringency_index = 0
        population = 0
        population_density = 0
        median_age = 0
        aged_65_older = 0
        aged_70_older = 0
        gdp_per_capita = 0
        extreme_poverty = 0
        cardiovasc_death_rate = 0
        diabetes_prevalence = 0
        female_smokers = 0
        male_smokers = 0
        handwashing_facilities = 0
        hospital_beds_per_thousand = 0
        life_expectancy = 0
        human_development_index = 0
        excess_mortality_cumulative = 0
        excess_mortality = 0
        excess_mortality_cumulative_per_million = 0
        excess_mortality_cumulative_absolute = 0
        new_deaths_per_million = 0
        hosp_patients = 0
        hosp_patients_per_million = 0
        weekly_icu_admissions = 0
        weekly_icu_admissions_per_million = 0
        weekly_hosp_admissions = 0
        weekly_hosp_admissions_per_million = 0
        new_tests = 0

        try:
            total_cases = float(args['total_cases'])
        except:
            pass
        try:
            new_cases = float(args['new_cases'])
        except:
            pass
        try:
            new_cases_smoothed = float(args['new_cases_smoothed'])
        except:
            pass
        try:
            total_deaths = float(args['total_deaths'])
        except:
            pass
        try:
            new_deaths = float(args['new_deaths'])
        except:
            pass
        try:
            new_deaths_smoothed = float(args['new_deaths_smoothed'])
        except:
            pass
        try:
            total_cases_per_million = float(args['total_cases_per_million'])
        except:
            pass
        try:
            new_cases_per_million = float(args['new_cases_per_million'])
        except:
            pass
        try:
            new_cases_smoothed_per_million = float(
                args['new_cases_smoothed_per_million'])
        except:
            pass
        try:
            total_deaths_per_million = float(
                args['total_deaths_per_million'])
        except:
            pass
        try:
            new_deaths_per_million = float(args['new_deaths_per_million'])
        except:
            pass
        try:
            new_deaths_smoothed_per_million = float(
                args['new_deaths_smoothed_per_million'])
        except:
            pass
        try:
            reproduction_rate = float(args['reproduction_rate'])
        except:
            pass
        try:
            icu_patients = float(args['icu_patients'])
        except:
            pass
        try:
            icu_patients_per_million = float(
                args['icu_patients_per_million'])
        except:
            pass
        try:
            hosp_patients = float(args['hosp_patients'])
        except:
            pass
        try:
            hosp_patients_per_million = float(
                args['hosp_patients_per_million'])
        except:
            pass
        try:
            weekly_icu_admissions = float(args['weekly_icu_admissions'])
        except:
            pass
        try:
            weekly_icu_admissions_per_million = float(
                args['weekly_icu_admissions_per_million'])
        except:
            pass
        try:
            weekly_hosp_admissions = float(args['weekly_hosp_admissions'])
        except:
            pass
        try:
            weekly_hosp_admissions_per_million = float(
                args['weekly_hosp_admissions_per_million'])
        except:
            pass
        try:
            total_tests = float(args['total_tests'])
        except:
            pass
        try:
            new_tests = float(args['new_tests'])
        except:
            pass
        try:
            total_tests_per_thousand = float(
                args['total_tests_per_thousand'])
        except:
            pass
        try:
            new_tests_per_thousand = float(args['new_tests_per_thousand'])
        except:
            pass
        try:
            new_tests_smoothed_per_thousand = float(
                args['new_tests_smoothed_per_thousand'])
        except:
            pass
        try:
            positive_rate = float(args['positive_rate'])
        except:
            pass
        try:
            tests_per_case = float(args['tests_per_case'])
        except:
            pass
        try:
            tests_units = str(args['tests_units'])
        except:
            pass
        try:
            total_vaccinations = float(args['total_vaccinations'])
        except:
            pass
        try:
            people_vaccinated = float(args['people_vaccinated'])
        except:
            pass
        try:
            people_fully_vaccinated = float(args['people_fully_vaccinated'])
        except:
            pass
        try:
            total_boosters = float(args['total_boosters'])
        except:
            pass
        try:
            new_vaccinations = float(args['new_vaccinations'])
        except:
            pass
        try:
            new_vaccinations_smoothed = float(
                args['new_vaccinations_smoothed'])
        except:
            pass
        try:
            total_vaccinations_per_hundred = float(
                args['total_vaccinations_per_hundred'])
        except:
            pass
        try:
            people_vaccinated_per_hundred = float(
                args['people_vaccinated_per_hundred'])
        except:
            pass
        try:
            people_fully_vaccinated_per_hundred = float(
                args['people_fully_vaccinated_per_hundred'])
        except:
            pass
        try:
            total_boosters_per_hundred = float(
                args['total_boosters_per_hundred'])
        except:
            pass
        try:
            new_vaccinations_smoothed_per_hundred = float(
                args['new_vaccinations_smoothed_per_hundred'])
        except:
            pass
        try:
            new_people_vaccinated_smoothed = float(
                args['new_people_vaccinated_smoothed'])
        except:
            pass
        try:
            new_people_vaccinated_smoothed_per_hundred = float(
                args['new_people_vaccinated_smoothed_per_hundred'])
        except:
            pass
        try:
            stringency_index = float(args['stringency_index'])
        except:
            pass
        try:
            population = float(args['population'])
        except:
            pass
        try:
            population_density = float(args['population_density'])
        except:
            pass
        try:
            median_age = float(args['median_age'])
        except:
            pass
        try:
            aged_65_older = float(args['aged_65_older'])
        except:
            pass
        try:
            aged_70_older = float(args['aged_70_older'])
        except:
            pass
        try:
            gdp_per_capita = float(args['gdp_per_capita'])
        except:
            pass
        try:
            extreme_poverty = float(args['extreme_poverty'])
        except:
            pass
        try:
            cardiovasc_death_rate = float(args['cardiovasc_death_rate'])
        except:
            pass
        try:
            diabetes_prevalence = float(args['diabetes_prevalence'])
        except:
            pass
        try:
            female_smokers = float(args['female_smokers'])
        except:
            pass
        try:
            male_smokers = float(args['male_smokers'])
        except:
            pass
        try:
            handwashing_facilities = float(args['handwashing_facilities'])
        except:
            pass
        try:
            hospital_beds_per_thousand = float(
                args['hospital_beds_per_thousand'])
        except:
            pass
        try:
            life_expectancy = float(args['life_expectancy'])
        except:
            pass

        try:
            human_development_index = float(args['human_development_index'])
        except:
            pass
        try:
            excess_mortality_cumulative = float(
                args['excess_mortality_cumulative'])
        except:
            pass
        try:
            excess_mortality = float(args['excess_mortality'])
        except:
            pass
        try:
            excess_mortality_cumulative_per_million = float(
                args['excess_mortality_cumulative_per_million'])
        except:
            pass
        try:
            excess_mortality_cumulative_absolute = float(
                args['excess_mortality_cumulative_absolute'])
        except:
            pass

        CovidRegister.objects.create(
            iso_code=args['iso_code'],
            continent=args['continent'],
            location=args['location'],
            date=date,
            total_cases=total_cases or 0,
            new_cases=new_cases or 0,
            new_cases_smoothed=new_cases_smoothed or 0,
            total_deaths=total_deaths or 0,
            new_deaths=new_deaths or 0,
            new_deaths_smoothed=new_deaths_smoothed or 0,
            total_cases_per_million=total_cases_per_million or 0,
            new_cases_per_million=new_cases_per_million or 0,
            new_cases_smoothed_per_million=new_cases_smoothed_per_million or 0,
            total_deaths_per_million=total_deaths_per_million or 0,
            new_deaths_per_million=new_deaths_per_million or 0,
            new_deaths_smoothed_per_million=new_deaths_smoothed_per_million or 0,
            reproduction_rate=reproduction_rate or 0,
            icu_patients=icu_patients or 0,
            icu_patients_per_million=icu_patients_per_million or 0,
            hosp_patients=hosp_patients or 0,
            hosp_patients_per_million=hosp_patients_per_million or 0,
            weekly_icu_admissions=weekly_icu_admissions or 0,
            weekly_icu_admissions_per_million=weekly_icu_admissions_per_million or 0,
            weekly_hosp_admissions=weekly_hosp_admissions or 0,
            weekly_hosp_admissions_per_million=weekly_hosp_admissions_per_million or 0,
            total_tests=total_tests or 0,
            new_tests=new_tests or 0,
            total_tests_per_thousand=total_tests_per_thousand or 0,
            new_tests_per_thousand=new_tests_per_thousand,
            new_tests_smoothed_per_thousand=new_tests_smoothed_per_thousand,
            positive_rate=positive_rate,
            tests_per_case=tests_per_case,
            tests_units=tests_units,
            total_vaccinations=total_vaccinations,
            people_vaccinated=people_vaccinated,
            people_fully_vaccinated=people_fully_vaccinated,
            total_boosters=total_boosters,
            new_vaccinations=new_vaccinations,
            new_vaccinations_smoothed=new_vaccinations_smoothed,
            total_vaccinations_per_hundred=total_vaccinations_per_hundred,
            people_vaccinated_per_hundred=people_vaccinated_per_hundred,
            people_fully_vaccinated_per_hundred=people_fully_vaccinated_per_hundred,
            total_boosters_per_hundred=total_boosters_per_hundred,
            new_vaccinations_smoothed_per_hundred=new_vaccinations_smoothed_per_hundred,
            new_people_vaccinated_smoothed=new_people_vaccinated_smoothed,
            new_people_vaccinated_smoothed_per_hundred=new_people_vaccinated_smoothed_per_hundred,
            stringency_index=stringency_index,
            population=population,
            population_density=population_density,
            median_age=median_age,
            aged_65_older=aged_65_older,
            aged_70_older=aged_70_older,
            gdp_per_capita=gdp_per_capita,
            extreme_poverty=extreme_poverty,
            cardiovasc_death_rate=cardiovasc_death_rate,
            diabetes_prevalence=diabetes_prevalence,
            female_smokers=female_smokers,
            male_smokers=male_smokers,
            handwashing_facilities=handwashing_facilities,
            hospital_beds_per_thousand=hospital_beds_per_thousand,
            life_expectancy=life_expectancy,
            human_development_index=human_development_index,
            excess_mortality_cumulative_absolute=excess_mortality_cumulative_absolute,
            excess_mortality_cumulative=excess_mortality_cumulative,
            excess_mortality=excess_mortality,
            excess_mortality_cumulative_per_million=excess_mortality_cumulative_per_million,
        )
