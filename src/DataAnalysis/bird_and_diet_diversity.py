import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BIRD_LOCS = '../DataCollection/output/bird-locations.csv'
BIRD_DIETS = '../DataCollection/output/bird-diets-by-order.csv'

def bird_diversity(location: pd.DataFrame) -> None:
    # generate a frequency score for each bird in each region
    pass


def main() -> None:
    sns.set()

    locations = pd.read_csv(BIRD_LOCS)
    diets = pd.read_csv(BIRD_DIETS)

    bird_diversity(locations)


if __name__ == '__main__':
    main()