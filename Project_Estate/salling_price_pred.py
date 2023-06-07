import pickle
import pandas as pd
import numpy as np
import sklearn

def data_processing(sample):
    cat_cols = ['status','city','propertyType','stories','Heating','Parking','state']
    
    with open('Project_Estate/model/one_hot_enc1.pkl', 'rb') as f:
        one_hot_enc = pickle.load(f)

    sample_cat = pd.DataFrame(
        one_hot_enc.transform(sample[cat_cols]).toarray(),
        columns=one_hot_enc.get_feature_names_out())

    sample = pd.concat([sample, sample_cat], axis=1)
    sample = sample.drop(cat_cols, axis=1)
    return sample


def prediction(sample):
    with open('Project_Estate\model\Estate_cat.pkl', 'rb') as pkl_file: 
        model = pickle.load(pkl_file)

    sample = data_processing(sample)

    sample_pred = model.predict(sample)

    return sample_pred
