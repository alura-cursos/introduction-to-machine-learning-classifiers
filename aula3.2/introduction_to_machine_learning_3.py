# -*- coding: utf-8 -*-
"""Introduction to Machine Learning - 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1femZm6uBR1H75XvsBQdtSuXQcFqZazSG
"""

!pip install seaborn==0.9.0

import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
data  = pd.read_csv(uri)
data.head()

swap = {
    0 : 1,
    1 : 0
}
data['finished'] = data.unfinished.map(swap)
data.head()

data.tail()

data.finished.hist()

import seaborn as sns

sns.scatterplot(x="expected_hours",y="price",data=data)

sns.scatterplot(x="expected_hours",y="price",
                hue="finished",
                data=data)

"""# Trying to run our basic model"""

x = data[["expected_hours","price"]]
y = data["finished"]

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np

SEED = 20
np.random.seed(SEED)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25,
                                                        stratify=y)
print("Train set lenght %d and test set lenght %d" % (len(train_x), len(test_x)))

model = LinearSVC()
model.fit(train_x, train_y)
predictions = model.predict(test_x)

accuracy = accuracy_score(test_y, predictions) * 100
print("Accuracy %.2f%%"% accuracy)

baseline_predictions = np.ones(540)
baseline_accuracy = accuracy_score(test_y, guilherme_predictions) * 100
print("Baseline Accuracy %.2f%%"% baseline_accuracy)

