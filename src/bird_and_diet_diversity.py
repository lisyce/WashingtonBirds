import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
from utils.constants import MONTHS, ABUNDANCES, SEASONS, ECOREGIONS

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
def plot_seasonal_bird_diversity(locations: pd.DataFrame) -> None:
    # compute sum of bird frequencies in each ecoregion ("bird frequency index")
    sp_freq = locations.groupby('ecoregion')['sp_freq'].sum()
    su_freq = locations.groupby('ecoregion')['su_freq'].sum()
    au_freq = locations.groupby('ecoregion')['au_freq'].sum()
    wi_freq = locations.groupby('ecoregion')['wi_freq'].sum()

    # do some df reshaping so we can graph it
    reshaped_df = sp_freq.to_frame().reset_index()
    reshaped_df['su_freq'] = su_freq.values
    reshaped_df['au_freq'] = au_freq.values
    reshaped_df['wi_freq'] = wi_freq.values

    # plot the 10 lines with varying line styles
    x_labels = ['Spring', 'Summer', 'Autumn', 'Winter']
    linestyles = ['-', '--', '-.']

    for i in range(len(reshaped_df)):
        label = reshaped_df.loc[i, 'ecoregion'].replace('_', ' ').title()
        plt.plot(x_labels, reshaped_df.loc[i, 'sp_freq':],
                 label=label, linestyle=linestyles[i % 3])

    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.title('Bird Frequency Index of Each Ecoregion by Season')
    plt.xlabel('Season')
    plt.ylabel('Bird Frequency Index')
    
    plt.savefig('charts/seasonal_bird_diversity.png', bbox_inches='tight')

# assumes locations df has the columns provided by compute_bird_frequencies
def plot_seasonal_diet_diversity(locations: pd.DataFrame, diets: pd.DataFrame):
    unique_bird_locs = locations.drop_duplicates(subset=['name'])
    merged = diets.merge(unique_bird_locs, left_on='bird_name', right_on='name', how='left')

    # drop unidentified food rows for this analysis
    identified = ~merged['item_taxon'].str.startswith('Unid.')
    merged = merged[identified]
    
    food_counts = merged.groupby('bird_name')['item_taxon'].count().to_frame().reset_index()
    food_counts.rename(columns={'item_taxon': 'unique_food_count'}, inplace=True)

    # weighted average = sum(# unique foods for bird * bfi for bird) / sum(bfi for bird)
    seasonal_bfis = locations.loc[:, ['name', 'ecoregion', 'wi_freq', 'sp_freq', 'su_freq', 'au_freq']]
    food_and_bfi_data = food_counts.merge(seasonal_bfis, left_on='bird_name', right_on='name', how='left')
    # print(food_and_bfi_data)
    avgs = weighted_avg(food_and_bfi_data)
    
    # need to graph now

    
# takes in df and returns weighted avg of number of unique foods per bird for each ecoregion each season as df
def weighted_avg(df: pd.DataFrame) -> pd.DataFrame | None:
    result = df['ecoregion'].dropna().drop_duplicates().to_frame().reset_index(drop=True)
    result['sp_diet_wavg'] = np.nan
    result['su_diet_wavg'] = np.nan
    result['au_diet_wavg'] = np.nan
    result['wi_diet_wavg'] = np.nan


    for ecoregion in ECOREGIONS:
        # filter to just that ecoregion
        filtered = df[df['ecoregion'] == ecoregion]

        # find a weighted avg for each season
        for season in SEASONS.keys():
            diet_wavg = (filtered[season + '_freq'] * filtered['unique_food_count']).sum() / filtered[season + '_freq'].sum()
            # result.loc[row, season + '_diet_wavg'] = diet_wavg
            idx = result[result['ecoregion'] == ecoregion].index
            result.loc[idx, season + '_diet_wavg'] = diet_wavg
    return result

def main() -> None:
    sns.set()
    sns.set_style('ticks')

    locations = pd.read_csv(BIRD_LOCS)
    locations = compute_bird_frequencies(locations)

    diets = pd.read_csv(BIRD_DIETS)

    # plot_seasonal_bird_diversity(locations)
    plot_seasonal_diet_diversity(locations, diets)


if __name__ == '__main__':
    main()