# The Data

(Last Updated March 2023)

> **DataCollection/output/bird-diets-by-\order.csv**
> 
> Records of each bird name, an item found in their diet categorized by taxonomic order, and the percentage of their diet made of that item.
>
> Figures are rounded to two decimal places. Any food item that starts with "Unid." means that the specific
> item is unidentified past the classification noted by the researchers.
>
> From [The Avian Diet Database](https://aviandiet.unc.edu/)

---

> **DataCollection/output/bird-locations.csv**
>
> Records of when and where birds are found in the ecoregions of WA state. 348 unique species.
>
> From [Seattle Audubon Society's BirdWeb](http://www.birdweb.org/BIRDWEB/birds)

# Reproducing Results

> :pushpin: All modules should be run from inside the `src` folder in the terminal. Requires at least Python 3.10

1. Install the libraries specified in `requirements.txt`.
2. All data files are already included with this project and can be found in the `data` folder.
However, if you wish to collect the data again, you may first run `bird_locations_collection.py`
and then `bird_diets_collection.py`. **This takes several minutes.**
3. After data has been collected, the analysis and visualization can be run. You may run
`basic_stats.py` and then `bird_and_diet_diversity.py`. Any charts generated from the analysis
will be outputted to the `charts` folder.
4. Test cases can be run by running `testing.py`.