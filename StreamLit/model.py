import streamlit as st
import pandas as pd
from sklearn import svm
from sklearn.pipeline import Pipeline
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import string

def doUserTesting(row):
    df = pd.read_excel('Constraint_Train.xlsx')
    df.drop('id', inplace = True, axis = 1)
    # df.loc[df["label"] == "real", "label"] = 1
    # df.loc[df["label"] == "fake", "label"] = 0

    df['length'] = df['tweet'].apply(len)
    y = df['label']
    # y=y.astype('int')

    pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer())
    ])
        
    pipeline.fit(df['tweet'])
    X_train_transformed = pipeline.transform(df['tweet'])
    model_svm = svm.SVC()
    model_svm.fit(X_train_transformed,y)
    X_input = pipeline.transform([row])
    pred_svm_inp = model_svm.predict(X_input)


    return(pred_svm_inp)
