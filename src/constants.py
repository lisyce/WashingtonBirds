from enum import Enum


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

MONTHS = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'aug': 7,
    'sep': 8,
    'oct': 9,
    'nov': 10,
    'dec': 11
}

class Classifications(Enum):
    KINGDOM = 'kingdom'
    PHYLUM = 'phylum'
    CLASS = 'class'
    ORDER = 'order'
    SUBORDER = 'suborder'
    FAMILY = 'family'
    GENUS = 'genus'
    SPECIES = 'species'