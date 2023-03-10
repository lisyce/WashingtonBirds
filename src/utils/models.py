"""
Cara Lisy and Kreslyn Hinds
CSE 163
This class provides some useful TypedDicts for type annotations
throughout the project. Has types for bird location data
and bird diet data.
"""
from typing import TypedDict


class BirdLocation(TypedDict):
    """
    Represents location data about a bird in one particular ecoregion
    as represented at birdweb.org
    """
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
    """
    Represents one item of a particular bird's diet as
    represented at aviandiet.unc.edu
    """
    bird_name: str
    item_taxon: str
    diet_percentage: float
