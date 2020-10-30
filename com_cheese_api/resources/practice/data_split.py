import pandas as pd
from sklearn.model_selection import train_test_split

import os

users = pd.read_csv("com_cheese_api/resources/data/users.csv")
user_train, user_test = train_test_split(users, test_size=0.3, random_state = 32)

user_train.to_csv(os.path.join('com_cheese_api/resources/data', 'user_train.csv'), index=False)
user_test.to_csv(os.path.join('com_cheese_api/resources/data', 'user_test.csv'), index=False)