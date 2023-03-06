'''
Kreslyn Hinds
CSE 163 
diet has no UNIDs.
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BIRD_DIET_DATA = "data/bird-diets-by-order.csv"
BIRD_LOCATION_DATA = "data/bird-locations.csv"


def get_total_birds(location_data, diet_data) -> list:
    '''
    Gets the total number of birds in the locations data set and the
        diet data set
    '''
    birds_location_data = location_data['name'].unique()
    birds_diet_data = diet_data['bird_name'].unique()
    return [len(birds_location_data),len(birds_diet_data)]


def get_total_foods(diet_data) -> int:
    '''
    Gets the total number of different foods/orders in the diet data set
    '''
    foods = diet_data['item_taxon'].unique()
    return len(foods)


def get_average_foods(diet_data) -> float:
    '''
    Gets the average number of foods per birds using the diet data set
    '''
    birds = diet_data.groupby('bird_name')[
        'item_taxon'].count()
    birds_ave = birds.mean()
    return birds_ave


def ecoregion_diversity(location_data) -> pd.DataFrame:
    '''
    Gets the total number of birds in each ecoregion using the
        location data set
    '''
    birds = location_data.groupby('ecoregion')['name'].count().reset_index()
    return birds


def birds_replaced_floats(location_data) -> pd.DataFrame:
    '''
    replaces values in our location data, and calculates scores for
        each season
    '''
    birds = location_data.replace(to_replace='I', value=0)
    birds = birds.replace('C', 4)
    birds = birds.replace('F', 3)
    birds = birds.replace('U', 2)
    birds = birds.replace('R', 1)
    birds['score'] = birds.iloc[:, 3:15].sum(axis=1)
    birds = birds.fillna(0)
    return birds


def birds_replaced(location_data) -> pd.DataFrame:
    '''
    replaces values in our location data, and calculates if a bird appears
        in a certain season
    '''
    birds = location_data.replace(to_replace='I', value=0)
    birds = birds.replace('C', 1)
    birds = birds.replace('F', 1)
    birds = birds.replace('U', 1)
    birds = birds.replace('R', 1)
    birds = birds.fillna(0)
    return birds


def bird_scores(location_data) -> pd.DataFrame:
    ''''
    gives each bird a 0-3 value for if they appear in a certain season
    '''
    birds = birds_replaced(location_data)
    birds['Spring'] = (birds['mar_abundance'] + birds['apr_abundance'] +
                        birds['may_abundance'])
    birds['Summer'] = (birds['jun_abundance'] + birds['jul_abundance'] +
                        birds['aug_abundance'])
    birds['Fall'] = (birds['sep_abundance'] + birds['oct_abundance'] +
                        birds['nov_abundance'])
    birds['Winter'] = (birds['dec_abundance'] + birds['jan_abundance'] +
                        birds['feb_abundance'])
    return birds[['name', 'Spring', 'Summer', 'Fall', 'Winter',
                    'ecoregion']]


def data_diet_summarized(location_data, diet_data) -> pd.Series:
    '''
    Merges the location and diet dataset, joined by
        the name of the bird, then groups birds by ecoregion and
        counts the 3 most popular foods in that region
    '''
    bird_ecoregions = location_data[['name', 'ecoregion']]
    bird_diet = diet_data[['bird_name', 'item_taxon']]
    birds = bird_ecoregions.merge(bird_diet, left_on='name',
                                    right_on='bird_name', how='inner')
    birds = birds.groupby('ecoregion')[
        'item_taxon'].agg(lambda x: x.value_counts().index[0:3])
    return birds


def plot_loc_and_diet_by_region(location_data, diet_data) -> None:
    '''
    merges the location and diet set to find the number birds in each
        ecoregion, and what the average diet diversity of a bird in
        that region is
    Makes a scatter plot with number of birds and diet diversity, each dot
        is colored by region'''
    sns.set()
    sns.set_style('darkgrid')
    diet_counts = diet_data.groupby('bird_name')[
        'item_taxon'].count()
    birds = location_data[['name', 'ecoregion']]
    birds = birds.merge(diet_counts, left_on='name', right_on='bird_name',
                        how='inner')
    diet_ave = birds.groupby('ecoregion')[
        'item_taxon'].mean().reset_index()
    bird_points = birds.groupby('ecoregion')['name'].count().reset_index()
    bird_points = bird_points.merge(diet_ave, left_on='ecoregion',
                                    right_on='ecoregion', how='inner')
    bird_points['ecoregion'] = bird_points['ecoregion'].str.replace('_', ' ')
    bird_points['ecoregion'] = bird_points['ecoregion'].str.title()
    bird_points.columns = ['Ecoregion', 'name', 'item_taxon']
    ax = sns.relplot(bird_points, x='item_taxon', y='name', hue='Ecoregion')
    plt.title('Birds and Diet by Region')
    plt.xlabel('Diet Average')
    plt.ylabel('Number of Birds')
    return bird_points

def plot_species_by_season_and_region(location_data) -> None:
    '''
    Makes a bar plot colored by season with ecoregion on the x axis and
        the number of birds on the y axis.
    '''
    sns.set()
    sns.set_style('ticks')
    birds = bird_scores(location_data)
    birds = birds.replace(2, 1)
    birds = birds.replace(3, 1)
    birds = birds.groupby('ecoregion')[['Spring', 'Summer', 'Fall',
                                       'Winter']].sum().reset_index()
    birds['ecoregion'] = birds['ecoregion'].str.replace('_', ' ')
    birds['ecoregion'] = birds['ecoregion'].str.title()
    birds.rename(columns={'spring': 'Spring', 'summer': 'Summer', 'fall': 'Fall', 'winter': 'Winter'})
    birds.plot(x='ecoregion',kind='bar', stacked=True, color=['red', 'skyblue',
                                                'green', 'purple'])
    plt.title("Number of Bird Species by Region and Season")
    plt.xticks(rotation=-70)
    plt.xlabel('Ecoregion')
    plt.ylabel('Number of Birds')
 


def main():
    diet_data = pd.read_csv(BIRD_DIET_DATA)
    no_Unid = diet_data['item_taxon'].str.contains('Unid.') == False
    diet_data = diet_data[no_Unid]
    location_data = pd.read_csv(BIRD_LOCATION_DATA)
    #Commands Needed For Presentation:
    plot_loc_and_diet_by_region(location_data,diet_data)
    plt.savefig('charts/birds_and_diet_by_region.png', bbox_inches='tight')
    plot_species_by_season_and_region(location_data)
    plt.savefig('charts/number_of_bird_species_by_region_and_season.png', bbox_inches='tight')

    # print('Total birds in [location, diet] data set:' + str(get_total_birds(location_data, diet_data)))
    # print('Total foods/different orders in the diet data set:' + str(get_total_foods(diet_data)))

    # print('Total average different orders per bird in the diet data set:' + str(get_average_foods(diet_data)))

    # print('Number of birds per region' + str(ecoregion_diversity(location_data)))
    # print('most popular foods' + str(data_diet_summarized(location_data, diet_data)))


if __name__ == '__main__':
    main()
