from importlib import reload
import simfin
out = reload(simfin)
from simfin import *
from config import *
import pandas as pd

# Extract and flaten simfin data set
if not os.path.isfile('tmp/extract.zip'):
    simfin = SimFin().extract().flatten()
else:
    simfin = SimFin().flatten()

# simfin = simfin.query(['FLWS','TSLA','A','AAPL','ADB','FB'])
# simfin = simfin.query(['AA','FLWS'])
# simfin = simfin.query(['FLWS', 'WSCO'])
# simfin = simfin.query(['WSCO'])

simfin = simfin.target(field='Flat_SPQA', type='class', lag=-1)


simfin = simfin.process(impute=False)

simfin = simfin.split()

df = simfin.data_df
# df.to_pickle('tmp/df.pkl')

X_train = simfin.X_train
y_train = simfin.y_train
groups = simfin.groups





X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.2, random_state=1)

X_test = simfin.X_test
y_test = simfin.y_test












# Add target
work = 'tmp/final_target'
if not os.path.isfile(work):
    simfin = simfin.target(field='Flat_SPQA', type='class', lag=-1).save(work)
else:
    simfin = SimFin().load(work)


simfin = simfin.process()





#-------------- Example snips

# Add predicted key features
# for feature in key_features:
# log.info(f"Feature {feature} ...")
# simfin = simfin.random_forest(field=feature, lag=-1, type='reg', thresh=None, max_depth=10, max_features="sqrt", min_samples_leaf=5, n_estimators=100)
# simfin = simfin.random_forest(field=feature, lag=-1, type='class', thresh=None, max_depth=10, max_features="sqrt", min_samples_leaf=5, n_estimators=100)


# simfin.csv()
# df = simfin.data_df


search.save_model('tmp/model')
