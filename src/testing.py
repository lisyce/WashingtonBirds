'''
Kreslyn Hinds and Cara Lisy
Final Project CSE163
'''
import pandas as pd
import numpy as np
import bird_and_diet_diversity
import basic_stats
from utils.cse163_utils import assert_equals

LOCATION_TEST_DATA = 'testing_data/test_data_location.csv'
DIET_TEST_DATA = 'testing_data/test_data_diet.csv'
CARA_LOCATION_DATA = 'testing_data/compute_bird_frequencies.csv'

def asserts_equals_testing(location_data, diet_data) -> None:
    '''
    to use the asserts equals from class on a data frame, they must first be
        converted to dictionaries'''
    expected_ecoregion_df = pd.read_csv('ecoregion_diversity_testing.csv')
    expected_replaced_float_df = pd.read_csv('expected_replaced_float.csv')
    expected_replaced_df = pd.read_csv('expected_replaced.csv')
    assert_equals([9, 8], basic_stats.get_total_birds(location_data, diet_data))
    assert_equals(15, basic_stats.get_total_foods(diet_data))
    assert_equals(4, basic_stats.get_average_foods(diet_data))
    assert_equals(expected_ecoregion_df.to_dict(), basic_stats.ecoregion_diversity(location_data).to_dict())
    # do we need this????
    # assert_equals(blank, info.ecoregion_common())

    assert_equals(expected_replaced_float_df.to_dict(), basic_stats.birds_replaced_floats(location_data).to_dict())
    # assert_equals(expected_replaced_df.to_dict(), basic_stats.birds_replaced(location_data).to_dict())
    
    # assert_equals(blank, basic_stats.bird_scores())
    # assert_equals(blank, basic_stats.data_diet_summarized(location_data, diet_data))
    '''
     # No asserts equals tests because we return plots
    info.loc_and_diet()
    # We expect 3 dots:

    info.plot())
    # we expect: 
    '''


def test_compute_bird_frequencies(location_data: pd.DataFrame) -> None:
    expected = {
        'name': ['Crow', 'Owl', 'Chicken', 'Crow'],
        'birdweb_society_link': np.full(4, 'url'),
        'ecoregion': ['pacific', 'eastern', 'eastern', 'western'],
        'jan_abundance': [0, 0, 0, 0],
        'feb_abundance': [0, 4, 0, 0],
        'mar_abundance': [0, 0, 0, 0],
        'apr_abundance': [0, 4, 4, 3],
        'may_abundance': [0, 0, 0, 0],
        'jun_abundance': [1, 2, 2, 2],
        'jul_abundance': [0, 0, 0, 0],
        'aug_abundance': [0, 3, 3, 0],
        'sep_abundance': [0, 0, 0, 0],
        'oct_abundance': [0, 2, 2, 2],
        'nov_abundance': [0, 2, 2, 4],
        'dec_abundance': [0, 0, 3, 4],
        'wi_freq': [0, 4/3, 1, 4/3],
        'sp_freq': [0, 4/3, 4/3, 1],
        'su_freq': [1/3, 5/3, 5/3, 2/3],
        'au_freq': [0, 4/3, 4/3, 2]
    }
    expected = pd.DataFrame(expected)

    received = bird_and_diet_diversity.compute_bird_frequencies(location_data)
    assert_equals(expected, received)


def main():
    # testing Kreslyn's functions
    diet_data = pd.read_csv(DIET_TEST_DATA)
    no_Unid = diet_data['item_taxon'].str.contains('Unid.') == False
    diet_data = diet_data[no_Unid]
    location_data = pd.read_csv(LOCATION_TEST_DATA)
    '''
    asserts_equals_testing(location_data, diet_data)
    '''
    
    expected_ecoregion_df = pd.read_csv('testing_data/ecoregion_diversity_testing.csv')
    print(expected_ecoregion_df.to_dict())

    # testing Cara's functions
    cara_test_df = pd.read_csv(CARA_LOCATION_DATA)
    test_compute_bird_frequencies(cara_test_df)

if __name__ == '__main__':
    main()
