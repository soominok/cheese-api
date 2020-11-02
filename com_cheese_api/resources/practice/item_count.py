import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

users = pd.read_csv("com_cheese_api/resources/data/users.csv")
# print(users)

def list_count():
    # sub1 = users.loc[:,['sub1_category']]
    sub1 = users['sub1_category']
    print(sub1)
    
    sub1_count = sub1.value_counts()
    # counts_cols = ['sub1_category', 'counts']
    sub1_count.columns = ["sub1_category","counts"]

    #print(sub1_count)
    return sub1_count

def make_countplot():
    counts = list_count()
    print(counts)
    # sns.barplot (x = counts, data = users)
    # plt.title("아이템 카테고리별 빈도 수")
    # plt.show()

#list_count()
make_countplot()