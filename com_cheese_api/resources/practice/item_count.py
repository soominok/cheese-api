import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns


users = pd.read_csv("com_cheese_api/resources/data/users.csv")
# print(users)

def category_Count():
    sub_count = users['sub1_category'].value_counts()
    item_category = sub_count.index
    item_count = sub_count.values

    item_count_plot = sns.barplot (x = item_category.value_counts().index, y = item_count, data = users)
    # plt.show()
    print(sub_count)
    return item_category

# category_Count()

def item_count():
    # for category_num in range(len(category_lists)):
    #     if data_category_list in category_lists[category_num]:
    item_size = users['sub1_category'].groupby(users['cheese_name']).size()
    print(item_size)

item_count()

# def item_change():
#     category_count = category_Count()
#     category_lists = np.array(category_count)
#     print('-' * 100)
#     print(category_lists)
#     for data_category_list in users['sub1_category']:
#         for category_num in range(len(category_lists)):
#             if data_category_list in category_lists[category_num]:
#                 print()
#         print(category_list)
#         if category_list in 


