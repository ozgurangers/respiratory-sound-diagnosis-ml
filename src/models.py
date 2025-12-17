from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def get_bayesian_model():
    return GaussianNB()

def get_svm_model():
    return SVC(kernel='linear')
