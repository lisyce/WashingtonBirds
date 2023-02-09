import requests
import csv
from bs4 import BeautifulSoup
from typing import TypedDict

OUTPUT_FILE = './output/bird-locations.csv'
ECOREGIONS = [
    'oceanic',
    'pacific_northwest_coast',
    'puget_trough',
    'north_cascades',
    'west_cascades',
    'east_cascades',
    'okanogan',
    'canadian_rockies',
    'blue_mountains',
    'columbia_plateau'
]

class BirdLocation(TypedDict):
    name: str
    birdweb_society_link: str
    ecoregion: str
    jan_abundance: str
    feb_abundance: str
    mar_abundance: str
    apr_abundance: str
    may_abundance: str
    jun_abundance: str
    jul_abundance: str
    aug_abundance: str
    sep_abundance: str
    oct_abundance: str
    nov_abundance: str
    dec_abundance: str

def bird_data_from_ecoregion(ecoregion: str) -> list[BirdLocation]:
    html = requests.get('http://becomewww.birdweb.org/BIRDWEB/ecoregion/sites/{}/site'.format(ecoregion)).text
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
            "birdweb_society_link": row.th.a['href']
        }
        
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        abundances = [td.string.strip() for td in row.find_all('td')]
        for month, abundance in zip(months, abundances):
            bird[month + '_abundance'] = abundance
             
        all_birds.append(bird)

    return all_birds

def main() -> None:
    full_data = []

    for region in ECOREGIONS:
        region_data = bird_data_from_ecoregion(region)
        full_data.extend(region_data)

    with open(OUTPUT_FILE, 'w', newline='') as csv_file:
        fields = full_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(full_data)



if __name__ == '__main__':
    main()