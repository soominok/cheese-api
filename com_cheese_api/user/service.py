import os

from com_cheese_api.util.file import FileReader
import pandas as pandas
import numpy as np
from sklearn.ensemble import RandomForestClassifier #rforest
from sklearn.tree import DecisionTreeClassifier #dtree
from sklearn.naive_bayes import GaussianNB #nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold # k value is understood as count
from sklearn.model_selection import cross_val_score

from pathlib import Path
# dtree, rforest, nb, knn, svm

# service가 정제하는 곳

"""
context: /
fname:
UserId
UserGender
UserAge
CheeseCode
CheeseName
Category : Large Class
Sub1_Category : Middle Class
Sub2_Category : SubClass
Cheese_Add_Name 
Buy_Price : 전체 
Buy_Count : 구매 개수
"""

class UserService:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.abspath("com_cheese_api/user/data")

        self.odf = None

    def hook(self):
        user = 'users.csv'
        this = self.fileReader
        train, test = train_test_split(user, test_size=0.3, random_state=33)
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload

        '''
        Original Model Generation
        '''

        self.odf = pd.DataFrame(
            {
                'user_id': this.train.user_id,
                'user_gender': this.train.user_gender
                'user_age': this.train.user_age
            }
        )

        this.id = this.test['user_id']
        this = self.drop_feature(this, '')



