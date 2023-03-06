'''
Kreslyn Hinds and Cara Lisy
Final Project CSE163
'''
import pandas as pd
import numpy as np
import bird_and_diet_diversity
import basic_stats
from utils.cse163_utils import assert_equals
import testing_data.expected_dictionaries as expected_dicts
import matplotlib.pyplot as plt

LOCATION_TEST_DATA = 'testing_data/test_data_location.csv'
DIET_TEST_DATA = 'testing_data/test_data_diet.csv'
CARA_LOCATION_DATA = 'testing_data/compute_bird_frequencies.csv'

def asserts_equals_testing(location_data, diet_data) -> None:
    '''
    to use the asserts equals from class on a data frame, they must first be
        converted to dictionaries'''

    assert_equals([9, 8], basic_stats.get_total_birds(location_data, diet_data))
    assert_equals(15, basic_stats.get_total_foods(diet_data))
    assert_equals(4, basic_stats.get_average_foods(diet_data))
    assert_equals(expected_dicts.for_ecoregion_diversity(), basic_stats.ecoregion_diversity(location_data).to_dict())
    assert_equals(expected_dicts.for_replaced_float(), basic_stats.birds_replaced_floats(location_data).to_dict())
    assert_equals(expected_dicts.for_replaced(), basic_stats.birds_replaced(location_data).to_dict())
    assert_equals(expected_dicts.for_scores(), basic_stats.bird_scores(location_data).to_dict())
    assert_equals(expected_dicts.for_diet_summarized(), basic_stats.data_diet_summarized(location_data, diet_data).to_dict())


     # No asserts equals tests because we return plots
    basic_stats.plot_loc_and_diet_by_region(location_data, diet_data)
    plt.savefig('testing_data/expected_birds_and_diet_by_region.png', bbox_inches='tight')
    # We expect: 1 dot for each region(cascades, eastern and pacific), the cascades dot should
    # have a species value of 2, and a diet value of 8. The eastern dot should have a species 
    # value of 3 and a diet value of 17/3 which is ~5.7. The pacific dot should have a species 
    # value of 7 and a diet value of 4.
    print(basic_stats.plot_species_by_season_and_region(location_data))
    plt.savefig('testing_data/expected_number_of_bird_species_by_region_and_season.png', bbox_inches='tight')
    # we expect: 1 bar for each region(cascades, eastern and pacific). The cascade bar should have 2 birds for
    # each season. The eastern bar should have 3 birds for eash season, the pacific bar should have 7 birds for
    #  each season except for spring with and fall where they should have 5. 
    


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

    asserts_equals_testing(location_data, diet_data)


    # testing Cara's functions
    cara_test_df = pd.read_csv(CARA_LOCATION_DATA)
    test_compute_bird_frequencies(cara_test_df)


if __name__ == '__main__':
    main()
