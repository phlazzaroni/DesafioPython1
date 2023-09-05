import csv

arquivo_csv = 'example-capitals-pt.csv'

def ler_csv(arquivo):
    with open(arquivo, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            city_en = row["City (en)"]
            city_pt = row["City (pt)"]
            country_en = row["Country (en)"]
            country_pt = row["Country (pt)"]
            country_code = row["Country code"]
            population = row["Population"]
            latitude = row["Latitude"]
            longitude = row["Longitude"]
            region = row["Region"]

            print(f"City (en): {city_en}")
            print(f"City (pt): {city_pt}")
            print(f"Country (en): {country_en}")
            print(f"Country (pt): {country_pt}")
            print(f"Country code: {country_code}")
            print(f"Population: {population}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Region: {region}")
            print("\n")

ler_csv(arquivo_csv)
