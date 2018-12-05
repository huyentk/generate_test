import pandas as pd
from sklearn.model_selection import train_test_split

print "hello"
r_cols = 'user_id', 'viewed_id', 'clicked_id', 'num_click'

ratings_base = pd.read_csv('ad.base', sep='\t', names=r_cols, encoding='latin-1')
rate_base = ratings_base.values

X_train, X_test = train_test_split(rate_base, test_size=0.3)
f = open("ux.train", "w")
for r in X_train:
    print >> f, r

f1 = open("ux.test", "w")
for r in X_test:
    print >> f1, r

print X_train.shape
print X_test.shape
