from typing import TypedDict


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


class BirdDiet(TypedDict):
    bird_name: str
    item_taxon: str
    diet_percentage: float
