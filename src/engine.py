import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib # To save the model

def train_system():
    df = pd.read_csv('data/metadata.csv')
    
    # We build two models: one for Priority, one for Component
    priority_model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', RandomForestClassifier())
    ])
    
    component_model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', RandomForestClassifier())
    ])
    
    priority_model.fit(df['Description'], df['Priority'])
    component_model.fit(df['Description'], df['Component'])
    
    return priority_model, component_model

# Logic to predict
def predict_bug(description, p_model, c_model):
    p = p_model.predict([description])[0]
    c = c_model.predict([description])[0]
    return p, c