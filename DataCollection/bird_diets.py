import requests
import csv
import time
from typing import TypedDict
from enum import Enum
import pandas as pd


class Classifications(Enum):
    KINGDOM = 'kingdom'
    PHYLUM = 'phylum'
    CLASS = 'class'
    ORDER = 'order'
    SUBORDER = 'suborder'
    FAMILY = 'family'
    GENUS = 'genus'
    SPECIES = 'species'


# OUTPUT_FILE from bird_locations.py
INPUT_FILE = './output/bird-locations.csv'
OUTPUT_FILE = './output/bird-diets-by-order.csv'
SELECTED_PREY_CLASSIFICATION = Classifications.ORDER


class BirdDiet(TypedDict):
    bird_name: str
    item_taxon: str
    diet_percentage: float


def diet_for_bird(bird_name: str) -> list[BirdDiet] | None:
    query = {
        "operationName": "GetPreyOf",
        "variables": {
            "name": bird_name,
            "level": SELECTED_PREY_CLASSIFICATION.value
        },
        "query": "query GetPreyOf($name: String!, $level: String) " +
                 "{\n getPreyOf(predatorName: $name, preyLevel: $level) " +
                 "{\n items\n taxon\n wt_or_vol\n} \n}"
    }
    url = 'https://back-end-dept-dietdatabase.cloudapps.unc.edu/graphql'

    data = requests.post(url, json=query).json()['data']['getPreyOf']

    results = []

    # determine what metric to use for diet percentage
    # we prefer the one with more records
    wt_vol_count = 0
    items_count = 0

    for food in data:
        if food['wt_or_vol']:
            wt_vol_count += 1
        if food['items']:
            items_count += 1

    diet_percentage = 'wt_or_vol' if wt_vol_count > items_count else 'items'

    for food in data:
        # if this food doesn't have data in the metric we picked, skip it
        if not food[diet_percentage] or float(food[diet_percentage]) < 1:
            continue

        bird_diet_record = {
            "bird_name": bird_name,
            "item_taxon": food['taxon'],
            "diet_percentage": food[diet_percentage]
        }
        results.append(bird_diet_record)

    return results


def main() -> None:
    input_df = pd.read_csv(INPUT_FILE)
    unique_birds = input_df['name'].drop_duplicates()

    output_data = []

    # "lazy iterator" for all unique birds
    for idx, bird in unique_birds.items():

        # rate limiting to be respectful of the server
        if idx % 5 == 0:
            time.sleep(2)

        records = diet_for_bird(bird)
        print(records)
        output_data.extend(records)

    with open(OUTPUT_FILE, 'w', newline='') as output:
        fields = output_data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_data)


if __name__ == '__main__':
    main()