"""
Cara Lisy
CSE 163
This file analyzes and visualizes the location distribution and diet
composition of WA state birds throughout its 10 ecoregions and 4 seasons.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
from utils.constants import MONTHS, ABUNDANCES, SEASONS, ECOREGIONS

BIRD_LOCS = 'data/bird-locations.csv'
BIRD_DIETS = 'data/bird-diets-by-order.csv'


def compute_bird_frequencies(birds: pd.DataFrame) -> pd.DataFrame:
    """
    Accepts a DataFrame of birds and their locational abundances and
    returns a new DataFrame where each monthly abundance is replaced
    with a number from 0-4 where Common (C) = 4, Fairly Common (F) = 3,
    Uncommon (U) = 2, Rare (R) = 1, and Irregular (I) or missing values
    = 0. If a bird is not found at least rarely in at least 1 month of
    the year, it is excluded from the result.

    A seasonal frequency is also computed for each bird and added to the
    result. This is referred to as its "bird frequency index" for a season
    and is equivalent to the bird's monthly frequencies for that season
    summed, divided by 3, and rounded to 3 decimal places.
    """
    # replace all 'I' values with NaN
    # and filter for birds that are at least rare in one month
    filtered = birds.replace('I', math.nan)
    at_least_rare = filtered.loc[:, 'jan_abundance':'dec_abundance']\
        .any(axis='columns')
    filtered = filtered[at_least_rare]

    # replace existing values with ints corresponding to the abundances
    for month in MONTHS:
        col = month + '_abundance'
        filtered[col] = filtered[col]\
            .apply(lambda x: ABUNDANCES.get(str(x)))

    # compute seasonal frequencies (rounded to 3 decimals)
    for season, months in SEASONS.items():
        month_abundance_ints = [filtered[m + '_abundance'] for m in months]
        seasonal_freq = sum(month_abundance_ints) / 3
        filtered[season + '_freq'] = round(seasonal_freq, 3)

    return filtered.reset_index(drop=True)


def filter_and_merge_food_and_bfi(locations: pd.DataFrame,
                                  diets: pd.DataFrame) -> pd.DataFrame:
    """
    Accepts an input DataFrame of birds and their bird frequency indexes
    and an input DataFrame of bird diet data and returns a new DataFrame
    merging these two datasets together. Assumes the provided locations
    DataFrame is an output from the compute_bird_frequencies method.
    Any diet item that begins with 'Unid.' meaning it is unidentified is
    removed from the returned result.
    """
    unique_bird_locs = locations.drop_duplicates(subset=['name'])
    merged = diets.merge(unique_bird_locs, left_on='bird_name',
                         right_on='name', how='inner')

    # drop unidentified food rows for this analysis
    identified = ~merged['item_taxon'].str.startswith('Unid.')
    merged = merged[identified]

    food_counts = merged.groupby('bird_name')['item_taxon'].count()
    food_counts = food_counts.to_frame().reset_index()
    food_counts.rename(columns={'item_taxon': 'unique_food_count'},
                       inplace=True)

    seasonal_bfis = locations.loc[:, ['name', 'ecoregion',
                                      'wi_freq', 'sp_freq',
                                      'su_freq', 'au_freq']]
    food_and_bfi_data = food_counts.merge(seasonal_bfis, left_on='bird_name',
                                          right_on='name', how='left')
    return food_and_bfi_data


def weighted_avg(df: pd.DataFrame) -> pd.DataFrame | None:
    """
    Accepts an input DataFrame of birds and their bird frequency index
    and diet data and returns a new DataFrame with a weighted average
    of each ecoregion's number of unique foods per bird each season.
    The weights in this calculation are the bird frequency indexes.
    """
    result = df['ecoregion'].dropna().drop_duplicates()
    result = result.to_frame().reset_index(drop=True)
    result['sp_diet_wavg'] = np.nan
    result['su_diet_wavg'] = np.nan
    result['au_diet_wavg'] = np.nan
    result['wi_diet_wavg'] = np.nan

    for ecoregion in result['ecoregion'].unique():
        # filter to just that ecoregion
        sub_df = df[df['ecoregion'] == ecoregion]

        # find a weighted avg for each season
        for season in SEASONS.keys():
            num = sub_df[season + '_freq'] * sub_df['unique_food_count']
            den = sub_df[season + '_freq'].sum()
            if (den == 0):
                diet_wavg = 0
            else:
                diet_wavg = num.sum() / den

            idx = result[result['ecoregion'] == ecoregion].index
            result.loc[idx, season + '_diet_wavg'] = diet_wavg

    return result.sort_values('ecoregion').reset_index(drop=True)


def plot_seasonal_diet_diversity(locations: pd.DataFrame, diets: pd.DataFrame):
    """
    Accepts an input DataFrame of birds and their locational abundances
    and a DataFrame of bird diet data and plots each ecoregion's weighted
    average of unique foods per bird each season. Assumes the provided
    locations DataFrame is an output from the compute_bird_frequencies
    method. Saves this chart under 'charts/seasonal_diet_diversity.png'.
    """
    plt.clf()
    food_and_bfi_data = filter_and_merge_food_and_bfi(locations, diets)
    avgs = weighted_avg(food_and_bfi_data)

    # plot graphs
    x_labels = ['Spring', 'Summer', 'Autumn', 'Winter']
    linestyles = ['-', '--', '-.']

    for i in range(len(avgs)):
        label = avgs.loc[i, 'ecoregion'].replace('_', ' ').title()
        plt.plot(x_labels, avgs.loc[i, 'sp_diet_wavg':],
                 label=label, linestyle=linestyles[i % 3])

    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.title('Bird Diet Index of Each Ecoregion by Season')
    plt.xlabel('Season')
    plt.ylabel('Bird Diet Index')

    plt.savefig('charts/seasonal_diet_diversity.png', bbox_inches='tight')


def plot_seasonal_bird_diversity(locations: pd.DataFrame) -> None:
    """
    Accepts an input DataFrame of birds and their locational abundances
    and plots each ecoregion's bird frequency index each season. Assumes
    the provided locations DataFrame is an output from the
    compute_bird_frequencies method.
    Saves this chart under 'charts/seasonal_bird_diversity.png'.
    """
    plt.clf()
    # compute sum of bird frequencies in each ecoregion
    # aka "bird frequency index"
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


def plot_bfi_box_plot(locations: pd.DataFrame) -> None:
    """
    Accepts an input DataFrame of birds and their locational abundances
    and plots distributions of bird frequency indexes in each
    ecoregion in each season. Saves this chart as
    "seasonal_bfi_boxplots.png".
    """
    plt.clf()
    fig, ax = plt.subplots(5, 2, figsize=(12, 15))

    # fill box plots with colors that match their
    # line graph counterparts for continuity
    matching_colors = {
        'blue_mountains': '#1f77b4',
        'canadian_rockies': '#ff7f0e',
        'columbia_plateau': '#2ca02c',
        'east_cascades': '#d62728',
        'north_cascades': '#9467bd',
        'oceanic': '#8c564b',
        'okanogan': '#e377c2',
        'pacific_northwest_coast': '#7f7f7f',
        'puget_trough': '#bcbd22',
        'west_cascades': '#17becf'
    }

    for idx, ecoregion in enumerate(ECOREGIONS):
        filtered = locations[locations['ecoregion'] == ecoregion]
        this_ax = ax[idx % 5, idx % 2]

        boxprops = {'facecolor': matching_colors[ecoregion]}

        this_ax.boxplot(filtered.loc[:, ['wi_freq', 'au_freq',
                                         'su_freq', 'sp_freq']],
                        vert=False, labels=['Winter', 'Autumn',
                                            'Summer', 'Spring'],
                        patch_artist=True, boxprops=boxprops,
                        medianprops={'color': 'k'})

        this_ax.set_title(ecoregion.replace('_', ' ').title())

    fig.suptitle("Distributions of Bird Frequency Indexes")
    fig.tight_layout()
    plt.savefig('charts/seasonal_bfi_boxplots.png')


def main() -> None:
    sns.set()
    sns.set_style('ticks')

    locations = pd.read_csv(BIRD_LOCS)
    locations = compute_bird_frequencies(locations)
    diets = pd.read_csv(BIRD_DIETS)

    plot_seasonal_bird_diversity(locations)
    plot_seasonal_diet_diversity(locations, diets)
    plot_bfi_box_plot(locations)


if __name__ == '__main__':
    main()
