import pandas as pd
from sklearn.model_selection import train_test_split

print "hello"
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']

ratings_base = pd.read_csv('ml-100k/u1.test', sep='\t', names=r_cols, encoding='latin-1')
rate_base = ratings_base.values

X_train, X_test = train_test_split(rate_base, test_size=0.2)
f = open("ux.train", "w")
for r in X_train:
    print >> f, r

f1 = open("ux.test", "w")
for r in X_test:
    print >> f1, r

print X_train.shape
print X_test.shape
