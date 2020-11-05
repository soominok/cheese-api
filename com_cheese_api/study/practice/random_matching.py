import numpy as np
import pandas as pd

def cheeseData():
    cheese_data = pd.read_csv("com_cheese_api/resources/data/cheese_data.csv")
    return cheese_data


def matching_kind():
    cheese_data = cheeseData()
    # matchings = np.array(cheese_data['matching'].tolist())
    # # print(matchings)
    # matching_list = ','.join(matchings)
    # # print(matching_list)
    
    # matching_lists = matching_list.split(', , ')
    # # print(matching_lists)
    # print(type(matching_lists))

    # match_set = set(matching_lists)
    # match_only_list = list(match_set)
    # print('-' * 50)
    # print(match_only_list)

    matchings = np.array(cheese_data['matching'].tolist())
    # # print(matchings)
    # print(type(matchings))
    matching_list = ' '.join(matchings)
    print(matching_list)
    
matching_kind()

#def make_random_matching():

