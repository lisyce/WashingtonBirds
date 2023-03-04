import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from utils.constants import MONTHS, ABUNDANCES, SEASONS

BIRD_LOCS = '../data_collection/data/bird-locations.csv'
BIRD_DIETS = '../data_collection/data/bird-diets-by-order.csv'

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
def plot_seasonal_diet_diversity(locations: pd.DataFrame, diets: pd.DataFrame) -> None:
    expect = {
        ""
    }


def main() -> None:
    sns.set()
    sns.set_style('ticks')

    locations = pd.read_csv(BIRD_LOCS)
    locations = compute_bird_frequencies(locations)

    diets = pd.read_csv(BIRD_DIETS)

    plot_seasonal_bird_diversity(locations)


if __name__ == '__main__':
    main()