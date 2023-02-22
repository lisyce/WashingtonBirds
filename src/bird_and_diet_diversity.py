import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from constants import ABUNDANCES

BIRD_LOCS = 'data/bird-locations.csv'
BIRD_DIETS = 'data/bird-diets-by-order.csv'

# note that this updates the original df
def compute_bird_frequencies(birds: pd.DataFrame) -> None:
    # birds['spring_freq'] = birds['']
    pass


def bird_diversity(locations: pd.DataFrame) -> None:
    pass


def main() -> None:
    sns.set()

    locations = pd.read_csv(BIRD_LOCS)
    compute_bird_frequencies(locations)
    print(locations.head())
    diets = pd.read_csv(BIRD_DIETS)

    bird_diversity(locations)


if __name__ == '__main__':
    main()