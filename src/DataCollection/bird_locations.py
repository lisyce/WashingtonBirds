import requests
import csv
from bs4 import BeautifulSoup
from constants import ECOREGIONS, MONTHS
from models import BirdLocation

OUTPUT_FILE = './output/bird-locations.csv'

def bird_data_from_ecoregion(ecoregion: str) -> list[BirdLocation]:
    html = requests.get('http://becomewww.birdweb.org/BIRDWEB/' +
                        'ecoregion/sites/{}/site'.format(ecoregion)).text

    soup = BeautifulSoup(html, 'html.parser')

    all_birds = []

    # the table is wrapped in the 'concern' div
    concern = soup.find(id='concern')
    for row in concern.table:
        # skip the header row
        if not row.td:
            continue

        bird = {
            "name": row.th.a.string,
            "birdweb_society_link": row.th.a['href'],
            "ecoregion": ecoregion
        }

        abundances = [td.string.strip() for td in row.find_all('td')]
        for month, abundance in zip(MONTHS.keys(), abundances):
            bird[month + '_abundance'] = abundance

        all_birds.append(bird)

    return all_birds


def main() -> None:
    full_data = []

    for region in ECOREGIONS:
        region_data = bird_data_from_ecoregion(region)
        full_data.extend(region_data)

    with open(OUTPUT_FILE, 'w', newline='') as output:
        fields = full_data[0].keys()
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(full_data)


if __name__ == '__main__':
    main()
