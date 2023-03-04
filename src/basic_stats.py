'''
Kreslyn Hinds
CSE 163 
diet has no UNIDs.
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Basic_Info:

    def __init__(self, diet: str, location: str) -> None:
        self._diet_data = pd.read_csv(diet)
        no_Unid = self._diet_data['item_taxon'].str.contains('Unid.') == False
        self._diet_data = self._diet_data[no_Unid]
        self._location_data = pd.read_csv(location)

    def get_total_birds(self) -> list:
        '''
        Gets the total number of birds in the locations data set and the
            diet data set
        '''
        birds_location_data = self._location_data['name'].unique()
        birds_diet_data = self._diet_data['bird_name'].unique()
        return [len(birds_location_data),len(birds_diet_data)]

    def get_total_foods(self) -> int:
        '''
        Gets the total number of different foods/orders in the diet data set
        '''
        foods = self._diet_data['item_taxon'].unique()
        return len(foods)

    def get_average_foods(self) -> float:
        '''
        Gets the average number of foods per birds using the diet data set
        '''
        birds = self._diet_data.groupby('bird_name')[
            'item_taxon'].count()
        birds_ave = birds.mean()
        return birds_ave

    def ecoregion_diversity(self) -> pd.DataFrame:
        '''
        Gets the total number of birds in each ecoregion using the
            location data set
        '''
        birds = self._location_data.groupby('ecoregion')['name'].count().reset_index()
        return birds

    def ecoregion_common(self) -> int:
        '''
        Gets the total number of common birds in each ecoregion using the
            location data set
        A common bird is considered to have an annual score > 15

        '''
        birds = self.birds_replaced_floats()
        mask_common = birds['score'] > 30
        birds = birds[mask_common]
        birds = birds.groupby('ecoregion')['name'].count()
        return birds

    def birds_replaced_floats(self) -> pd.DataFrame:
        '''
        replaces values in our location data, and calculates scores for
            each season
        '''
        birds = self._location_data.replace(to_replace='I', value=0)
        birds = birds.replace('C', 4)
        birds = birds.replace('F', 3)
        birds = birds.replace('U', 2)
        birds = birds.replace('R', 1)
        birds['score'] = birds.iloc[:, 3:15].sum(axis=1)
        birds = birds.fillna(0)
        return birds

    def birds_replaced(self) -> pd.DataFrame:
        '''
        replaces values in our location data, and calculates if a bird appears
            in a certain season
        '''
        birds = self._location_data.replace(to_replace='I', value=0)
        birds = birds.replace('C', 1)
        birds = birds.replace('F', 1)
        birds = birds.replace('U', 1)
        birds = birds.replace('R', 1)
        birds = birds.fillna(0)
        return birds

    def bird_scores(self) -> pd.DataFrame:
        ''''
        gives each bird a 0 or 1 value for if they appear in a certain season
        '''
        birds = self.birds_replaced()
        birds['spring'] = (birds['mar_abundance'] + birds['apr_abundance'] +
                           birds['may_abundance'])/3
        birds['summer'] = (birds['jun_abundance'] + birds['jul_abundance'] +
                           birds['aug_abundance'])/3
        birds['fall'] = (birds['sep_abundance'] + birds['oct_abundance'] +
                         birds['nov_abundance'])/3
        birds['winter'] = (birds['dec_abundance'] + birds['jan_abundance'] +
                           birds['feb_abundance'])/3
        return birds[['name', 'spring', 'summer', 'fall', 'winter',
                      'ecoregion']]

    def data_diet_summarized(self) -> pd.Series:
        '''
        Merges the location and diet dataset, joined by
            the name of the bird, then groups birds by ecoregion and
            counts the 3 most popular foods in that region
        '''
        bird_ecoregions = self._location_data[['name', 'ecoregion']]
        bird_diet = self._diet_data[['bird_name', 'item_taxon']]
        birds = bird_ecoregions.merge(bird_diet, left_on='name',
                                      right_on='bird_name', how='inner')
        birds = birds.groupby('ecoregion')[
            'item_taxon'].agg(lambda x: x.value_counts().index[0:3])
        return birds

    def loc_and_diet(self) -> None:
        '''
        merges the location and diet set to find the number birds in each
            ecoregion, and what the average diet diversity of a bird in
            that region is
        Makes a scatter plot with number of birds and diet diversity, each dot
            is colored by region'''
        diet_counts = self._diet_data.groupby('bird_name')[
            'item_taxon'].count()
        birds = self._location_data[['name', 'ecoregion']]
        birds = birds.merge(diet_counts, left_on='name', right_on='bird_name',
                            how='inner')
        diet_ave = birds.groupby('ecoregion')[
            'item_taxon'].mean().reset_index()
        bird_points = self.ecoregion_diversity()
        bird_points = bird_points.merge(diet_ave, left_on='ecoregion',
                                        right_on='ecoregion', how='inner')
        sns.relplot(bird_points, x='item_taxon', y='name', hue='ecoregion')
        plt.title('Birds and Diet by Region')
        plt.show()
        plt.savefig('Birds and Diet by Region.png')

    def plot(self) -> None:
        '''
        Makes a bar plot colored by season with ecoregion on the x axis and
            the number of birds on the y axis.
        '''
        birds = self.bird_scores()
        birds = birds.groupby('ecoregion')[['spring', 'summer', 'fall',
                                            'winter']].sum()
        birds.plot(kind='bar', stacked=True, color=['red', 'skyblue',
                                                    'green', 'purple'])
        plt.title("Number of Bird Species by Region and Season")
        plt.xticks(rotation=- 33)
        plt.xlabel('Ecoregion')
        plt.ylabel('Number of Birds')
        plt.show()
        plt.savefig('Number of Bird Species by Region and Season.png')

def main():
    info = Basic_Info(DIET_TEST_DATA, LOCATION_TEST_DATA)
    asserts_equals_testing(info)
    info = Basic_Info(BIRD_DIET_DATA, BIRD_LOCATION_DATA)
    calls_for_writeup(info)
    # print(pd.read_csv(LOCATION_TEST_DATA))



if __name__ == '__main__':
    main()