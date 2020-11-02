import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

users = pd.read_csv("com_cheese_api/resources/data/users.csv")
# print(users)

def itemList_count():
    sns.barplot (x = users['sub1_category'].value_counts().index, y = users['sub1_category'].value_counts().values, data = users)
    plt.title("아이템 카테고리별 빈도 수")
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.show()

#list_count()
itemList_count()