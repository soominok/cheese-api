#import numpy as numpy
#import pandas as pd
#from sklearn.model_selection import train_test_split

#user_train, user_test = train_test_split(users, test_size=0.3, shuffle=True, random_state=34)

#user_train.to_csv(os.path.join('com_cheese_api/user/data', 'train.csv'), index=False)
#user_test.to_csv(os.path.join('com_cheese_api/user/data', 'test.csv'), index=Fa)

import re
import string

frequency = {}
document_csv = open('com_cheese_api/user/data/users.csv', 'r')

text_string = document_csv.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print (words, frequency[words])
