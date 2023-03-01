import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from constants import ABUNDANCES, MONTHS, SEASONS

BIRD_LOCS = 'data/bird-locations.csv'
BIRD_DIETS = 'data/bird-diets-by-order.csv'

def compute_bird_frequencies(birds: pd.DataFrame) -> pd.DataFrame:
    # replace all 'I' values with NaN and filter for birds that are at least rare in one month
    filtered = birds.replace('I', math.nan)
    at_least_rare = filtered.loc[:, 'jan_abundance':'dec_abundance'].any(axis='columns')
    filtered = filtered[at_least_rare]
    
    # add additional columns for the numerical values of each abundance
    for month in MONTHS:
        new_name = filtered[month + '_abundance'].name[0:3] + '_abundance_int'
        filtered[new_name] = filtered[month + '_abundance'].apply(lambda x: ABUNDANCES.get(str(x)))

    # compute seasonal frequencies (rounded to 3 decimals)
    for season, months in SEASONS.items():
        filtered[season + '_freq'] = round(sum([filtered[month + '_abundance_int'] for month in months]) / 3, 3)
    
    return filtered

# assumes input df has the columns provided by compute_bird_frequencies
def bird_diversity(locations: pd.DataFrame) -> None:
    # compute sum of bird frequencies in each ecoregion ("bird frequency index")
    wi_freq = locations.groupby('ecoregion')['wi_freq'].sum()
    sp_freq = locations.groupby('ecoregion')['sp_freq'].sum()
    su_freq = locations.groupby('ecoregion')['su_freq'].sum()
    au_freq = locations.groupby('ecoregion')['au_freq'].sum()

    # put all these "frequencies by region" series into one nice df
    freq_df = pd.concat([wi_freq, sp_freq, su_freq, au_freq], axis=1)
    print(freq_df)

def main() -> None:
    sns.set()

    locations = pd.read_csv(BIRD_LOCS)
    locations = compute_bird_frequencies(locations)

    # diets = pd.read_csv(BIRD_DIETS)

    bird_diversity(locations)


if __name__ == '__main__':
    main()