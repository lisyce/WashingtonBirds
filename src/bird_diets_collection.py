"""
Cara Lisy
CSE 163
This program collects data about bird's diets based on
an input file of birds. Data is collected from
aviandiet.unc.edu.
"""
import requests
import csv
import time
import pandas as pd
from utils.constants import Classifications
from utils.models import BirdDiet


# INPUT_FILE here is OUTPUT_FILE from bird_locations.py
INPUT_FILE = 'data/bird-locations.csv'
OUTPUT_FILE = 'data/bird-diets-by-order.csv'
SELECTED_PREY_CLASSIFICATION = Classifications.ORDER


def diet_for_bird(bird_name: str) -> list[BirdDiet]:
    """
    Accepts a bird's name as a string and collects data
    from aviandiet.unc.edu regarding that bird's diet.
    If there are multiple metrics in the database
    to measure the composition of the bird's diet,
    selects the one with the most records.
    Returns this data as a list of BirdDiets
    """
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
        if not food[diet_percentage]:
            continue

        bird_diet_record = {
            "bird_name": bird_name,
            "item_taxon": food['taxon'],
            "diet_percentage": round(float(food[diet_percentage]), 2)
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
        output_data.extend(records)

    with open(OUTPUT_FILE, 'w', newline='') as output:
        fields = output_data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_data)


if __name__ == '__main__':
    main()
