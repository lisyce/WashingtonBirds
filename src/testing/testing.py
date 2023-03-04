'''
Kreslyn Hinds
Final Project CSE163
Part 1/2 for Basic Stats
'''
import pandas as pd
import data_analysis.basic_stats
from utils.cse163_utils import assert_equals

BIRD_DIET_DATA = "../data_collection/data/bird-diets-by-order.csv"
BIRD_LOCATION_DATA = "../data_collection/data/bird-locations.csv"
LOCATION_TEST_DATA = 'test_data_location.csv'
DIET_TEST_DATA = 'test_data_diet.csv'

def asserts_equals_testing(info: str) -> None:
    '''
    to use the asserts equals from class on a data frame, they must first be
        converted to dictionaries'''
    expected_ecoregion_df = pd.read_csv('ecoregion_diversity_testing.csv')
    expected_replaced_float_df = pd.read_csv('expected_replaced_float.csv')
    # expected_replaced_df = 
    assert_equals([9, 8], info.get_total_birds())
    assert_equals(15, info.get_total_foods())
    assert_equals(4, info.get_average_foods())
    assert_equals(expected_ecoregion_df.to_dict(), info.ecoregion_diversity().to_dict())
    # do we need this????
    # assert_equals(blank, info.ecoregion_common())

    assert_equals(expected_replaced_float_df.to_dict(), info.birds_replaced_floats().to_dict())
    # assert_equals(blank, info.birds_replaced())
    # assert_equals(blank, info.bird_scores())
    # assert_equals(blank, info.data_diet_summarized())
    '''
     # No asserts equals tests because we return plots
    info.loc_and_diet()
    # We expect 3 dots:

    info.plot())
    # we expect: 
    '''

def calls_for_writeup(info: str) -> None:
    #Commands Needed For Presentation:
    # print(info.loc_and_diet())
    # print(info.plot())
    # print('Total birds in [location, diet] data set:' + str(info.get_total_birds()))
    # print('Total foods/different orders in the diet data set:' + str(info.get_total_foods()))

    # print('Total average different orders per bird in the diet data set:' + str(info.get_average_foods()))

    # print('Number of birds per region, counting only birds with an annual score above 15:' + 
          # str(info.ecoregion_common()))
    # print('Number of birds per region' + str(info.ecoregion_diversity()))
    ## most popular foods = info.data_diet_summarized()
    pass


def main():
    # info = Basic_Info(DIET_TEST_DATA, LOCATION_TEST_DATA)
    # asserts_equals_testing(info)
    # info = Basic_Info(BIRD_DIET_DATA, BIRD_LOCATION_DATA)
    # calls_for_writeup(info)
    # print(pd.read_csv(LOCATION_TEST_DATA))
    expected_ecoregion_df = pd.read_csv('ecoregion_diversity_testing.csv')
    print(expected_ecoregion_df.to_dict())



if __name__ == '__main__':
    main()
