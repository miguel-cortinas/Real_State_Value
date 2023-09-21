import joblib

def predict(data, model):
    
    if model == 'Random Forest Regression':
        model = joblib.load('random_forest_model.pkl')

    pipeline = joblib.load("full_pipeline.pkl")
    data = pipeline.transform(data)
    
    return model.predict(data)