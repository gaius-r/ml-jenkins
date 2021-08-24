import joblib
model = joblib.load("fiftystartups_model.pk1")
model.predict([[165349.20, 137497.80, 476994.10, 1, 0]])
