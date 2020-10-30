#import numpy as numpy
#import pandas as pd
#from sklearn.model_selection import train_test_split

#user_train, user_test = train_test_split(users, test_size=0.3, shuffle=True, random_state=34)

#user_train.to_csv(os.path.join('com_cheese_api/user/data', 'train.csv'), index=False)
#user_test.to_csv(os.path.join('com_cheese_api/user/data', 'test.csv'), index=Fa)

import re
import string

document_csv = open('com_cheese_api/user/data/users.csv', 'r')

lists = document_csv.readlines()
document_csv.close()

lists