from types import MethodDescriptorType
from flask import Flask, render_template, request, url_for, redirect
from numpy.core.numeric import indices
from pandas.core.indexes.base import Index
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import joblib
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend(reg, tour):

    # imported data
    df = pd.read_csv(r"tour.csv", encoding='unicode_escape')
    #tourist = df['tourist_info'].values

    dff = df.loc[df['Category'] == reg]

    # vectorization
    tf = TfidfVectorizer(analyzer="word", ngram_range=(
        1, 2), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(dff['Category'])
    tfidf_matrix.shape

    # similarity cosine
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    tourist_info = dff['tourist_info']
    indices = pd.Series(dff.index, index=dff['tourist_info'])

    idx = indices[tour]
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    dff_indices = [i[0] for i in sim_scores]

    return tourist_info.iloc[dff_indices]



