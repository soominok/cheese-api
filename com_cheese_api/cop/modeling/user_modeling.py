import tensorflow as tf
import numpy as np
import pandas as pd

def user_model():
    users = pd.read_csv("com_cheese_api/cop/machine/data/user_dataset.csv")