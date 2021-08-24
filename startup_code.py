import joblib
model = joblib.load("fiftystartups_model.pk1")
print(model.predict([[142107.20, 91391.80, 366168.10, 0, 1]]))
