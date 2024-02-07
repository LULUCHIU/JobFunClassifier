from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import pickle


def Classifier_perform_score(_data, TARGET_col, estimators=[], CV = 5):
    entries = []
    
    for estimator in estimators:
        estimator_name = estimator.__class__.__name__
        pipe = Pipeline(
            [
                ("vectorizer",TfidfVectorizer()),
                ("estimator", estimator),
            ],
            verbose = False,
        )
        scores = cross_val_score(pipe, _data["text_clean"], _data[TARGET_col], scoring="accuracy", cv = CV)
        entries.append((estimator_name, scores.mean(), scores.std() *2 ))
    df_metrics = pd.DataFrame(entries, columns = ["estimator_name","mean_accuracy","standard_variation"])

    return df_metrics

class JobFunClassifier_model:
    default_pipe = None
    default_outdir = None
    default_modelname = None
    default_estimator = None
    default_y_test = None
    default_X_test = None
    def __init__(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train
        self._estimator = JobFunClassifier_model.default_estimator
        self._outdir = JobFunClassifier_model.default_outdir
        self._modelname = JobFunClassifier_model.default_modelname
        self._pipe = JobFunClassifier_model.default_pipe
        self._y_test = JobFunClassifier_model.default_y_test
        self._X_test = JobFunClassifier_model.default_X_test

    def build_model(self, estimator):
        self._estimator = estimator
        self._pipe = Pipeline(
            [
                ("vectorizer",TfidfVectorizer()),
                ("estimator",self._estimator)
            ],
            verbose = True
        )
        self._pipe.fit(self._X_train, self._y_train)

    def save_model(self, outdir, modelname):
        self._outdir = outdir
        self._modelname = modelname
        with open(self._outdir + "/" + self._modelname, "wb") as f:
            pickle.dump(self._pipe,f)
    
    def get_accuracy(self, X_test, y_test):
        self._X_test = X_test
        self._y_test = y_test
        y_pred = self._pipe.predict(self._X_test)
        return accuracy_score(self._y_test, y_pred) *100
    
    def get_classification_report(self, X_test, y_test):
        self._X_test = X_test
        self._y_test = y_test
        y_pred = self._pipe.predict(self._X_test)
        return classification_report(self._y_test, y_pred)
    
    def get_confusion_matrix_plot(self, X_test, y_test, plot=False):
        self._X_test = X_test
        self._y_test = y_test
        y_pred = self._pipe.predict(self._X_test)
        cm = confusion_matrix(self._y_test, y_pred)
        if plot == True:
            cm_plot = ConfusionMatrixDisplay(cm, display_labels=self._pipe.classes_ )
            plt.figure(figsize = (8,6))
            cm_plot.plot(xticks_rotation=90)
            plt.show()
            return cm
        else:
            return cm





    

