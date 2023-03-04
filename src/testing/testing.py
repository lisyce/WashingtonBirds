'''
Kreslyn Hinds
Final Project CSE163
'''
import pandas as pd
from .. import basic_stats as Basic_Info
BIRD_DIET_DATA = "../data/bird-diets-by-order.csv"
BIRD_LOCATION_DATA = "../data/bird-locations.csv"
LOCATION_TEST_DATA = 'test_data_location.csv'
DIET_TEST_DATA = 'test_data_diet.csv'
from cse163_utils import assert_equals

def asserts_equals_testing(location_data, diet_data) -> None:
    '''
    to use the asserts equals from class on a data frame, they must first be
        converted to dictionaries'''
    expected_ecoregion_df = pd.read_csv('ecoregion_diversity_testing.csv')
    expected_replaced_float_df = pd.read_csv('expected_replaced_float.csv')
    expected_replaced_df = pd.read_csv('expected_replaced.csv')
    assert_equals([9, 8], Basic_Info.get_total_birds(location_data, diet_data))
    assert_equals(15, Basic_Info.get_total_foods(diet_data))
    assert_equals(4, Basic_Info.get_average_foods(diet_data))
    assert_equals(expected_ecoregion_df.to_dict(), Basic_Info.ecoregion_diversity(location_data).to_dict())
    # do we need this????
    # assert_equals(blank, info.ecoregion_common())

    assert_equals(expected_replaced_float_df.to_dict(), Basic_Info.birds_replaced_floats(location_data).to_dict())
    # assert_equals(expected_replaced_df.to_dict(), Basic_Info.birds_replaced(location_data).to_dict())
    
    # assert_equals(blank, Basic_Info.bird_scores())
    # assert_equals(blank, Basic_Info.data_diet_summarized(location_data, diet_data))
    '''
     # No asserts equals tests because we return plots
    info.loc_and_diet()
    # We expect 3 dots:

    info.plot())
    # we expect: 
    '''


def main():
    diet_data = pd.read_csv(BIRD_DIET_DATA)
    no_Unid = diet_data['item_taxon'].str.contains('Unid.') == False
    diet_data = diet_data[no_Unid]
    location_data = pd.read_csv(BIRD_LOCATION_DATA)
    '''
    asserts_equals_testing(location_data, diet_data)
    '''
    
    expected_ecoregion_df = pd.read_csv('ecoregion_diversity_testing.csv')
    print(expected_ecoregion_df.to_dict())



if __name__ == '__main__':
    main()
