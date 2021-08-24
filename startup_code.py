import joblib
model = joblib.load("fiftystartups_model.pk1")
model.predict([[165349.20, 137478.80, 471784.10, 1, 0]])
