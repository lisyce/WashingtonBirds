"""
Cara Lisy and Kreslyn Hinds
CSE 163
This file contains useful constants applicable throughout
the project including ecoregion names, months of the year,
which months are a part of which season, numerical values
for monthly abundance classifications, and all the taxonomic
classifications that diet data could be collected for.
"""
from enum import Enum


ECOREGIONS = [
    'blue_mountains',
    'canadian_rockies',
    'columbia_plateau',
    'east_cascades',
    'north_cascades',
    'pacific_northwest_coast',
    'puget_trough',
    'oceanic',
    'okanogan',
    'west_cascades',
]

MONTHS = [
    'jan', 'feb', 'mar', 'apr', 'may', 'jun',
    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
]

SEASONS = {
    'wi': ['dec', 'jan', 'feb'],
    'sp': ['mar', 'apr', 'may'],
    'su': ['jun', 'jul', 'aug'],
    'au': ['sep', 'oct', 'nov']
}

ABUNDANCES = {
    'C': 4,
    'F': 3,
    'U': 2,
    'R': 1,
    'I': 0,
    'nan': 0
}


class Classifications(Enum):
    """
    Enum for all of the possible taxonomic classifications
    to collect diet data for
    """
    KINGDOM = 'kingdom'
    PHYLUM = 'phylum'
    CLASS = 'class'
    ORDER = 'order'
    SUBORDER = 'suborder'
    FAMILY = 'family'
    GENUS = 'genus'
    SPECIES = 'species'
