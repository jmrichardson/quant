from tpot import TPOTClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import pickle
from loguru import logger

# Set current directory
try:
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
except NameError:
    import os
    os.chdir('d:/projects/quant/model/tpot')

# Load dataset
logger.info("Loading dataset ...")
with open('../../data/fundamental/simfin/quarterly_dataset.pickle', 'rb') as handle:
    data = pickle.load(handle)

#

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target,
                                                    train_size=0.75, test_size=0.25)

tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export('tpot_mnist_pipeline.py')