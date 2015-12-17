
import numpy as np

import pandas

from sklearn import cross_validation
from sklearn import dummy
from sklearn import feature_extraction
from sklearn import grid_search
from sklearn import linear_model
from sklearn import metrics
from sklearn import naive_bayes
from sklearn import pipeline
from sklearn import preprocessing
from sklearn import svm

def indent(lines, amount, ch=' '):
    #http://stackoverflow.com/questions/8234274/how-to-indent-the-content-of-a-string-in-python
    padding = amount * ch
    return padding + ('\n'+padding).join(lines.split('\n'))

models = [
          naive_bayes.GaussianNB(),
          linear_model.LogisticRegression(random_state=0),
          svm.SVC(random_state=0, kernel='linear'),
         ]

clf_hyp = [
           dict(),
           dict(clf__C=[.00001, .0001, .001, .01, .1, 1., 10.]),
           dict(clf__C=[.00001, .0001, .001, .01, .1, 1., 10.]),
          ]

results = {}

def main():
    essays = pandas.read_csv(r"C:\Users\Craig\Documents\Python Scripts\SMM\labeled_data\essays_all.csv")
    facebook = pandas.read_csv(r"C:\Users\Craig\Documents\Python Scripts\SMM\labeled_data\facebook_all.csv")
    youtube = pandas.read_csv(r"C:\Users\Craig\Documents\Python Scripts\SMM\labeled_data\youtube_all.csv")
    all_data = pandas.read_csv(r"C:\Users\Craig\Documents\Python Scripts\SMM\labeled_data\all_data.csv")
    datasets = {"Essays":essays, "Facebook":facebook, "Youtube":youtube, "All":all_data}

    for d in datasets:
        print("Dataset: ", d)
        data = datasets[d]
        X = data.iloc[:,5:]

        for y in range(0,5):
            print(indent("Personality Factor: ", 2), data.columns.values[y])
            Y = data.iloc[:,y]
            runBaseline = True

            trainX, testX, yTrain, yTest = cross_validation.train_test_split(X,Y,test_size=0.1, random_state=0)

            vectorizer = feature_extraction.text.TfidfVectorizer()
            liwc_scaler = preprocessing.StandardScaler()
            sentiment_scaler = preprocessing.StandardScaler()
            pos_scaler = preprocessing.StandardScaler()

            unigrams = vectorizer.fit_transform(trainX["TEXT"]).toarray()
            liwc = liwc_scaler.fit_transform(trainX.ix[:,"WC":"OtherP"])
            sentiment = sentiment_scaler.fit_transform(trainX.ix[:,"pos_score":"obj_score"])
            pos = pos_scaler.fit_transform(trainX.ix[:, "''":"WRB"])
            allf = np.hstack((unigrams, liwc, sentiment, pos))

            unigrams_t = vectorizer.transform(testX["TEXT"]).toarray()
            liwc_t = liwc_scaler.transform(testX.ix[:,"WC":"OtherP"])
            sentiment_t = sentiment_scaler.transform(testX.ix[:,"pos_score":"obj_score"])
            pos_t = pos_scaler.transform(testX.ix[:, "''":"WRB"])
            allf_t = np.hstack((unigrams_t, liwc_t, sentiment_t, pos_t))

            features = {"Unigrams":(unigrams, unigrams_t), "LIWC":(liwc, liwc_t), "Sentiment":(sentiment, sentiment_t), "POS":(pos, pos_t), "All":(allf, allf_t)}


            for f in features:
                xTrain = features[f][0]
                xTest = features[f][1]

                if runBaseline:
                    baseline = dummy.DummyClassifier(strategy='most_frequent', random_state=0)
                    baseline.fit(xTrain, yTrain)
                    predictions = baseline.predict(xTest)

                    print(indent("Baseline: ", 4))
                    print(indent("Test Accuracy: ", 4), metrics.accuracy_score(yTest, predictions))
                    print(indent(metrics.classification_report(yTest, predictions), 4))
                    print()
                    runBaseline = False

                print(indent("Features: ", 4), f)

                for m, model in enumerate(models):
                    hyp = clf_hyp[m]
                    pipe = pipeline.Pipeline([('clf', model)])

                    if len(hyp) > 0:
                        grid = grid_search.GridSearchCV(pipe, hyp, cv=10, n_jobs=-1)
                        grid.fit(xTrain, yTrain)
                        predictions = grid.predict(xTest)

                        print(indent(type(model).__name__, 6))
                        print(indent("Best hyperparameters: ", 8), grid.best_params_)
                        print(indent("Validation Accuracy: ", 8), grid.best_score_)
                        print(indent("Test Accuracy: ", 8), metrics.accuracy_score(yTest, predictions))
                        print(indent(metrics.classification_report(yTest, predictions), 8))

                    else:
                        grid = model
                        grid.fit(xTrain, yTrain)
                        predictions = grid.predict(xTest)

                        print(indent(type(model).__name__, 6))
                        print(indent("Test Accuracy: ", 8), metrics.accuracy_score(yTest, predictions))
                        print(indent(metrics.classification_report(yTest, predictions), 8))

                print()
            print()
        print()

if __name__ == '__main__':
    main()